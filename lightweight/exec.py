# QUELLE: https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch/blob/master/demo.py (geändert)

import sys
import argparse
import os
import json

import cv2
import numpy as np
import torch

sys.path.append("/app/pose_estimation")
from models.with_mobilenet import PoseEstimationWithMobileNet
from modules.keypoints import extract_keypoints, group_keypoints
from modules.load_state import load_state
from modules.pose import Pose, track_poses
from val import normalize, pad_width


JOINT_NAME_TRANSLATE = {
    "nose": "NOSE",
    "neck": "NECK",
    "r_sho": "SHOULDER_RIGHT",
    "r_elb": "ELBOW_RIGHT",
    "r_wri": "WRIST_RIGHT",
    "l_sho": "SHOULDER_LEFT",
    "l_elb": "ELBOW_LEFT",
    "l_wri": "WRIST_LEFT",
    "r_hip": "HIP_RIGHT",
    "r_knee": "KNEE_RIGHT",
    "r_ank": "ANKLE_RIGHT",
    "l_hip": "HIP_LEFT",
    "l_knee": "KNEE_LEFT",
    "l_ank": "ANKLE_LEFT",
    "r_eye": "EYE_RIGHT",
    "l_eye": "EYE_LEFT",
    "r_ear": "EAR_RIGHT",
    "l_ear": "EAR_LEFT"
}


class VideoReader(object):
    def __init__(self, file_name):
        self.file_name = file_name
        try:  # OpenCV needs int to read from webcam
            self.file_name = int(file_name)
        except ValueError:
            pass

    def __iter__(self):
        self.cap = cv2.VideoCapture(self.file_name)
        if not self.cap.isOpened():
            raise IOError("Video {} cannot be opened".format(self.file_name))
        return self

    def __next__(self):
        was_read, img = self.cap.read()
        if not was_read:
            raise StopIteration
        return img

    def get_fps(self):
        return self.cap.get(cv2.CAP_PROP_FPS)


def infer_fast(net, img, net_input_height_size, stride, upsample_ratio, cpu,
               pad_value=(0, 0, 0), img_mean=np.array([128, 128, 128], np.float32), img_scale=np.float32(1 / 256)):
    height, width, _ = img.shape
    scale = net_input_height_size / height
    scaled_img = cv2.resize(img, (0, 0), fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
    scaled_img = normalize(scaled_img, img_mean, img_scale)
    min_dims = [net_input_height_size, max(scaled_img.shape[1], net_input_height_size)]
    padded_img, pad = pad_width(scaled_img, stride, pad_value, min_dims)
    tensor_img = torch.from_numpy(padded_img).permute(2, 0, 1).unsqueeze(0).float()
    if not cpu:
        tensor_img = tensor_img.cuda()
    stages_output = net(tensor_img)
    stage2_heatmaps = stages_output[-2]
    heatmaps = np.transpose(stage2_heatmaps.squeeze().cpu().data.numpy(), (1, 2, 0))
    heatmaps = cv2.resize(heatmaps, (0, 0), fx=upsample_ratio, fy=upsample_ratio, interpolation=cv2.INTER_CUBIC)
    stage2_pafs = stages_output[-1]
    pafs = np.transpose(stage2_pafs.squeeze().cpu().data.numpy(), (1, 2, 0))
    pafs = cv2.resize(pafs, (0, 0), fx=upsample_ratio, fy=upsample_ratio, interpolation=cv2.INTER_CUBIC)
    return heatmaps, pafs, scale, pad


def run_demo(net, image_provider, height_size, cpu, track, smooth, output_path=None):
    net = net.eval()
    if not cpu:
        net = net.cuda()

    stride = 8
    upsample_ratio = 4
    num_keypoints = Pose.num_kpts
    previous_poses = []

    writer = None
    data = []

    for img in image_provider:
        orig_img = img.copy()
        heatmaps, pafs, scale, pad = infer_fast(net, img, height_size, stride, upsample_ratio, cpu)

        total_keypoints_num = 0
        all_keypoints_by_type = []
        for kpt_idx in range(num_keypoints):  # 19th for bg
            total_keypoints_num += extract_keypoints(heatmaps[:, :, kpt_idx], all_keypoints_by_type, total_keypoints_num)

        pose_entries, all_keypoints = group_keypoints(all_keypoints_by_type, pafs)
        for kpt_id in range(all_keypoints.shape[0]):
            all_keypoints[kpt_id, 0] = (all_keypoints[kpt_id, 0] * stride / upsample_ratio - pad[1]) / scale
            all_keypoints[kpt_id, 1] = (all_keypoints[kpt_id, 1] * stride / upsample_ratio - pad[0]) / scale
        current_poses = []
        for n in range(len(pose_entries)):
            if len(pose_entries[n]) == 0:
                continue
            pose_keypoints = np.ones((num_keypoints, 2), dtype=np.int32) * -1
            for kpt_id in range(num_keypoints):
                if pose_entries[n][kpt_id] != -1.0:
                    pose_keypoints[kpt_id, 0] = int(all_keypoints[int(pose_entries[n][kpt_id]), 0])
                    pose_keypoints[kpt_id, 1] = int(all_keypoints[int(pose_entries[n][kpt_id]), 1])
            pose = Pose(pose_keypoints, pose_entries[n][18])
            current_poses.append(pose)

        # strukturierte Daten bilden
        frame_data = []
        for pose in current_poses:
            pose_data = {}
            for i, joint_name in enumerate(pose.kpt_names):
                joint_data = {}
                if pose.keypoints[i][0] == -1:
                    continue
                joint_data["x"] = int(pose.keypoints[i][0])
                joint_data["y"] = int(pose.keypoints[i][1])
                joint_data["sigma"] = float(pose.sigmas[i])
                joint_data["var"] = float(pose.vars[i])
                pose_data[JOINT_NAME_TRANSLATE[joint_name]] = joint_data
            frame_data.append(pose_data)
        data.append(frame_data)

        # tracken
        if track:
            track_poses(previous_poses, current_poses, smooth=smooth)
            previous_poses = current_poses

        # zeichnen
        for pose in current_poses:
            pose.draw(img)
        img = cv2.addWeighted(orig_img, 0.6, img, 0.4, 0)
        for pose in current_poses:
            cv2.rectangle(img, (pose.bbox[0], pose.bbox[1]),
                          (pose.bbox[0] + pose.bbox[2], pose.bbox[1] + pose.bbox[3]), (0, 255, 0))
            if track:
                cv2.putText(img, "id: {}".format(pose.id), (pose.bbox[0], pose.bbox[1] - 16),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 255))

        # Initialisiere VideoWriter beim ersten Frame
        if output_path and writer is None:
            height, width = img.shape[:2]
            fourcc = cv2.VideoWriter_fourcc(*"mp4v")
            writer = cv2.VideoWriter(output_path, fourcc, image_provider.get_fps(), (width, height))

        writer.write(img)

    if writer:
        writer.release()

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="""Lightweight human pose estimation python demo.
                       This is just for quick results preview.
                       Please, consider c++ demo for the best performance.""")
    parser.add_argument("--checkpoint-path", type=str, required=True, help="path to the checkpoint")
    parser.add_argument("--height-size", type=int, default=256, help="network input layer height size")
    parser.add_argument("--video", type=str, default="", help="path to video file or camera id")
    parser.add_argument("--cpu", action="store_true", help="run network inference on cpu")
    parser.add_argument("--track", type=int, default=1, help="track pose id in video")
    parser.add_argument("--smooth", type=int, default=1, help="smooth pose keypoints")
    parser.add_argument("--output-video", type=str, default="", help="path to save output video")
    args = parser.parse_args()

    net = PoseEstimationWithMobileNet()
    checkpoint = torch.load(args.checkpoint_path, map_location="cpu")
    load_state(net, checkpoint)

    files = os.listdir(args.video)
    mp4_files = list(filter(lambda s: s.endswith(".mp4"), files))
    os.makedirs(args.output_video, exist_ok=True)
    for file_name in mp4_files:
        frame_provider = VideoReader(os.path.join(args.video, file_name))
        data = run_demo(net, frame_provider, args.height_size, args.cpu, args.track, args.smooth, os.path.join(args.output_video, file_name))
        with open(os.path.join(args.output_video, file_name+".json"), "w") as f:
            json.dump(data, f)
