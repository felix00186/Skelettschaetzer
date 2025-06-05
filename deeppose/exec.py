import os
import cv2
import json

from mmpose.apis import (get_track_id, inference_top_down_pose_model,
                         init_pose_model, process_mmdet_results,
                         vis_pose_tracking_result)
from mmpose.datasets import DatasetInfo
from mmdet.apis import inference_detector, init_detector


JOINT_NAMES = [
    "NOSE",
    "EYE_LEFT",
    "EYE_RIGHT",
    "EAR_LEFT",
    "EAR_RIGHT",
    "SHOULDER_LEFT",
    "SHOULDER_RIGHT",
    "ELBOW_LEFT",
    "ELBOW_RIGHT",
    "WRIST_LEFT",
    "WRIST_RIGHT",
    "HIP_LEFT",
    "HIP_RIGHT",
    "KNEE_LEFT",
    "KNEE_RIGHT",
    "ANKLE_LEFT",
    "ANKLE_RIGHT"
]

# Input-Daten
det_config = os.environ["DET_CONFIG"]
det_checkpoint = os.environ["DET_CHECKPOINT"]
pose_config = os.environ["POSE_CONFIG"]
pose_checkpoint = os.environ["POSE_CHECKPOINT"]
input_dir = "/data/input"
output_dir = "/data/deeppose"
os.makedirs(output_dir, exist_ok=True)
input_files = list(filter(lambda f: f.endswith(".mp4"), os.listdir(input_dir)))
device = "cuda:0"

# Modelle initialisieren
det_model = init_detector(det_config, det_checkpoint, device=device)
pose_model = init_pose_model(pose_config, pose_checkpoint, device=device)
dataset = pose_model.cfg.data["test"]["type"]
dataset_info = pose_model.cfg.data["test"].get("dataset_info", None)
if dataset_info is not None:
    dataset_info = DatasetInfo(dataset_info)

# Video-Dateien durchgehen
for file_name in input_files:
    cap = cv2.VideoCapture(os.path.join(input_dir, file_name))
    assert cap.isOpened(), f"Faild to load video file {file_name}"
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    videoWriter = cv2.VideoWriter(os.path.join(output_dir, file_name), fourcc, fps, size)
    next_id = 0
    pose_results = []
    data = []
    while (cap.isOpened()):
        pose_results_last = pose_results
        flag, img = cap.read()
        if not flag:
            break
        mmdet_results = inference_detector(det_model, img)
        person_results = process_mmdet_results(mmdet_results, 1)

        pose_results, returned_outputs = inference_top_down_pose_model(
            pose_model,
            img,
            person_results,
            bbox_thr=0.3,
            format="xyxy",
            dataset=dataset,
            dataset_info=dataset_info,
            return_heatmap=False,
            outputs=None)

        pose_results, next_id = get_track_id(
            pose_results,
            pose_results_last,
            next_id,
            use_oks=False,
            tracking_thr=0.3,
            use_one_euro=False,
            fps=fps)

        # strukturierte Daten
        frame_data = []
        humans = [*pose_results]
        humans.sort(key=lambda human: human["track_id"])
        for human in humans:
            frame_data.append({JOINT_NAMES[i]:
                {
                    "x": float(info[0]),
                    "y": float(info[1])
                }
                for i, info in enumerate(human["keypoints"])})
        data.append(frame_data)

        # Bilder einzeichnen
        vis_img = vis_pose_tracking_result(
            pose_model,
            img,
            pose_results,
            radius=4,
            thickness=1,
            dataset=dataset,
            dataset_info=dataset_info,
            kpt_score_thr=0.3,
            show=False)
        videoWriter.write(vis_img)
    cap.release()
    videoWriter.release()

    with open(os.path.join(output_dir, file_name+".json"), "w") as f:
        json.dump(data, f)
