import os
import json
import cv2
from mmpose.apis import MMPoseInferencer

# Lade die Namen der Gelenke
with open("./joint_names.json", "r") as f:
    joint_names = json.load(f)

# Initialisiere den Inferencer
dataset_path = os.environ["DATASET_PATH"]
pose_model_config = os.environ["POSE_CONFIG"]
pose_model_weights = dataset_path + os.environ["POSE_CHECKPOINT"]

det_model_config = dataset_path + os.environ["DET_CONFIG"]
det_model_weights = dataset_path + os.environ["DET_CHECKPOINT"]

inferencer = MMPoseInferencer(
    pose2d=pose_model_config,
    pose2d_weights=pose_model_weights,
    det_model=det_model_config,
    det_weights=det_model_weights
)

# Verzeichnisse
input_dir = "/data/input"
output_dir = "/data/cpm"
os.makedirs(output_dir, exist_ok=True)

# Alle MP4-Videos im Input-Ordner
input_files = [f for f in os.listdir(input_dir) if f.endswith(".mp4")]

# Verarbeite jedes Video einzeln
for file_name in input_files:
    input_path = os.path.join(input_dir, file_name)
    cap = cv2.VideoCapture(input_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()

    output_path = os.path.join(output_dir, file_name)
    writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    keypoints_json = []
    result_generator = inferencer(input_path, return_vis=True)

    for result in result_generator:
        vis_frame = result["visualization"]
        writer.write(vis_frame)

        frame_keypoints = []
        instances = result["predictions"][0]["keypoints"]
        for person in instances:
            person_dict = {
                joint_names[i]: {"x": float(x), "y": float(y)}
                for i, (x, y, score) in enumerate(person)
                if score >= 0.1  # nur wenn erkennbar
            }
            frame_keypoints.append(person_dict)

        keypoints_json.append(frame_keypoints)

    writer.release()

    # Speichere Keypoints als JSON
    json_path = os.path.join(output_dir, file_name.replace(".mp4", ".json"))
    with open(json_path, "w") as f:
        json.dump(keypoints_json, f)
