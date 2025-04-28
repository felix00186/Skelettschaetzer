import os
import cv2
import torch
import numpy as np
import sys
sys.path.append('/app/pose_estimation')
from pose_estimation.models.with_mobilenet import PoseEstimationWithMobileNet
from pose_estimation.modules.load_state import load_state
from pose_estimation.modules.pose import Pose, track_poses
from pose_estimation.val import normalize, pad_width
from pose_estimation.modules.keypoints import extract_keypoints, group_keypoints, inter_fast

input_path = '/data/input.mp4'
output_path = '/data/lightweight.mp4'

if not os.path.exists(input_path):
    raise FileNotFoundError(f"{input_path} wurde nicht gefunden.")

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

net = PoseEstimationWithMobileNet()
checkpoint = torch.load('pose_estimation/models/checkpoint_iter_370000.pth', map_location=device)
load_state(net, checkpoint)

net = net.to(device)
net.eval()

cap = cv2.VideoCapture(input_path)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (int(cap.get(3)), int(cap.get(4))))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    orig_img = frame.copy()
    img = normalize(orig_img)
    img = torch.from_numpy(img).permute(2, 0, 1).unsqueeze(0).float()
    img = img.to(device)

    heatmaps, pafs, scale, pad = infer_fast(net, img, 256, stride=8, upsample_ratio=4, cpu=(device == 'cpu'))

    total_keypoints = 0
    all_keypoints_by_type = []
    num_keypoints = Pose.num_joints

    for kpt_idx in range(num_keypoints):
        total_keypoints += extract_keypoints(heatmaps[:, :, kpt_idx], all_keypoints_by_type, total_keypoints)

    pose_entries, all_keypoints = group_keypoints(all_keypoints_by_type, pafs)

    for pose_entry in pose_entries:
        if len(pose_entry) == 0:
            continue

        pose = Pose(all_keypoints, pose_entry, 0)
        pose.draw(frame)

    out.write(frame)

cap.release()
out.release()
