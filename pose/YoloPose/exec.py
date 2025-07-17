import os
import cv2
import json
from ultralytics import YOLO

INPUT_DIR = '/data/input'
OUTPUT_DIR = '/data/YoloPose'
MODEL_PATH = 'yolov8x-pose.pt'

with open("./joint_names.json", "r") as f:
    JOINT_NAMES = json.load(f)

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for file in os.listdir(OUTPUT_DIR):
        os.remove(os.path.join(OUTPUT_DIR, file))

def is_video_file(file):
    return file.lower().endswith('.mp4')

def process_video(video_path, model):
    video_name = os.path.splitext(os.path.basename(video_path))[0]
    out_video_path = os.path.join(OUTPUT_DIR, f'{video_name}.mp4')
    out_json_path = os.path.join(OUTPUT_DIR, f'{video_name}.json')
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    writer = cv2.VideoWriter(out_video_path, fourcc, fps, (width, height))
    frame_idx = 0
    all_frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        writer.write(annotated_frame)
        keypoints_batch = results[0].keypoints
        frame_data = []
        person_count = len(keypoints_batch.conf) if keypoints_batch.conf is not None else 0
        for i_person in range(person_count):
            person_data = {}
            for i_joint in range(len(keypoints_batch.conf[i_person])):
                person_data[JOINT_NAMES[i_joint]] = {
                    "x": float(keypoints_batch.xyn[i_person][i_joint][0]),
                    "y": float(keypoints_batch.xyn[i_person][i_joint][1]),
                    "conf": float(keypoints_batch.conf[i_person][i_joint])
                }
            frame_data.append(person_data)
        all_frames.append(frame_data)
        frame_idx += 1
    cap.release()
    writer.release()
    with open(out_json_path, 'w') as f:
        json.dump(all_frames, f)

def main():
    ensure_output_dir()
    model = YOLO(MODEL_PATH)
    for file in os.listdir(INPUT_DIR):
        if is_video_file(file):
            input_path = os.path.join(INPUT_DIR, file)
            print(f'Verarbeite Video: {input_path}')
            process_video(input_path, model)

if __name__ == '__main__':
    main()
