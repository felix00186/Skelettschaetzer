import os
import cv2
import json

from mmpose.apis import get_track_id, inference_bottom_up_pose_model, init_pose_model, vis_pose_tracking_result
from mmpose.core import Smoother
from mmpose.datasets import DatasetInfo


with open("./joint_names.json", "r") as f:
    joint_names = json.load(f)

# Input-Daten
pose_config = os.environ["POSE_CONFIG"]
pose_checkpoint = os.environ["POSE_CHECKPOINT"]
input_dir = "/data/input"
input_files = list(filter(lambda s: s.endswith(".mp4"), os.listdir(input_dir)))
output_dir = "/data/higher-hrnet"
os.makedirs(output_dir, exist_ok=True)
device = "cuda:0"

# Initialisierung des Netzwerkes
pose_model = init_pose_model(pose_config, pose_checkpoint, device=device.lower())
dataset = pose_model.cfg.data['test']['type']
dataset_info = pose_model.cfg.data['test'].get('dataset_info', None)
if dataset_info is None:
    assert (dataset == 'BottomUpCocoDataset')
else:
    dataset_info = DatasetInfo(dataset_info)

# Videos laden
for file_name in input_files:
    cap = cv2.VideoCapture(os.path.join(input_dir, file_name))
    assert cap.isOpened(), f'Faild to load video file {file_name}'
    fps = cap.get(cv2.CAP_PROP_FPS)
    size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
            int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videoWriter = cv2.VideoWriter(os.path.join(output_dir, file_name), fourcc, fps, size)
    output_layer_names = None
    next_id = 0
    pose_results = []
    data = []
    while cap.isOpened():
        flag, img = cap.read()
        if not flag:
            break
        pose_results_last = pose_results

        pose_results, returned_outputs = inference_bottom_up_pose_model(
            pose_model,
            img,
            dataset=dataset,
            dataset_info=dataset_info,
            pose_nms_thr=0.9,
            return_heatmap=False,
            outputs=output_layer_names)

        # get track id for each person instance
        pose_results, next_id = get_track_id(
            pose_results,
            pose_results_last,
            next_id,
            use_oks=False,
            tracking_thr=0.3,
            use_one_euro=False,
            fps=fps)

        # strukturierte Daten erstellen
        frame_data = []
        humans = [*pose_results]
        humans.sort(key=lambda human: human["track_id"])
        for human in humans:
            frame_data.append({joint_names[i]:
               {
                   "x": float(info[0]),
                   "y": float(info[1])
               }
            for i, info in enumerate(human["keypoints"])})
        data.append(frame_data)

        # Bild generieren
        vis_img = vis_pose_tracking_result(
            pose_model,
            img,
            pose_results,
            radius=4,
            thickness=1,
            dataset=dataset,
            dataset_info=dataset_info,
            kpt_score_thr=0.5,
            show=False)
        videoWriter.write(vis_img)

    cap.release()
    videoWriter.release()

    with open(os.path.join(output_dir, file_name.replace(".mp4", ".json")), "w") as f:
        json.dump(data, f)
