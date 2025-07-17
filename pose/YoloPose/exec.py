import os
import cv2
import json
from ultralytics import YOLO

INPUT_DIR = '/data/input'
OUTPUT_DIR = '/data/YoloPose'
MODEL_PATH = 'yolov8x-pose.pt'

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
    pose_data = []
    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        annotated_frame = results[0].plot()
        writer.write(annotated_frame)
        keypoints = results[0].keypoints
        for i, kp in enumerate(keypoints.data.cpu().numpy()):
            pose_data.append({
                'frame': frame_idx,
                'person_id': i,
                'keypoints': kp.tolist()
            })
        frame_idx += 1
    cap.release()
    writer.release()
    with open(out_json_path, 'w') as f:
        json.dump(pose_data, f, indent=2)

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
