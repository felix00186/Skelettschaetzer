import os
import json
import cv2
import mmcv
from mmpose.apis import MMPoseInferencer

# Lade die Namen der Gelenke
with open("./joint_names.json", "r") as f:
    joint_names = json.load(f)

# Initialisiere den Inferencer
pose_model_config = os.environ["POSE_CONFIG"]
pose_model_weights = os.environ["POSE_CHECKPOINT"]

inferencer = MMPoseInferencer(
    pose2d=pose_model_config,
    pose2d_weights=pose_model_weights
)

# Verzeichnisse
input_dir = "/data/input"
output_dir = f"/data/{os.environ['OUTPUT_DIR']}"
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
        vis_frame = cv2.cvtColor(result["visualization"][0], cv2.COLOR_RGB2BGR)
        writer.write(vis_frame)

        frame_keypoints = []
        instances = result["predictions"][0]
        for person in instances:
            person_dict = {
                str(i): {"x": float(point[0]), "y": float(point[1])}
                for i, (point, score) in enumerate(zip(person["keypoints"], person["keypoint_scores"]))
                if score > 0.5
            }
            frame_keypoints.append(person_dict)

        keypoints_json.append(frame_keypoints)

    writer.release()

    # Speichere Keypoints als JSON
    json_path = os.path.join(output_dir, file_name.replace(".mp4", ".json"))
    with open(json_path, "w") as f:
        json.dump(keypoints_json, f)
