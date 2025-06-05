import argparse
import logging
import time
import cv2
import numpy as np
import os
import json
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh


JOINT_NAMES_TRANSLATE = {
    "CocoPart.LAnkle": "ANKLE_LEFT",
    "CocoPart.RWrist": "WRIST_RIGHT",
    "CocoPart.RElbow": "ELBOW_RIGHT",
    "CocoPart.LElbow": "ELBOW_LEFT",
    "CocoPart.Nose": "NOSE",
    "CocoPart.RShoulder": "SHOULDER_RIGHT",
    "CocoPart.REye": "EYE_RIGHT",
    "CocoPart.LEye": "EYE_LEFT",
    "CocoPart.RKnee": "KNEE_RIGHT",
    "CocoPart.RAnkle": "ANKLE_RIGHT",
    "CocoPart.LEar": "EAR_LEFT",
    "CocoPart.Neck": "NECK",
    "CocoPart.LHip": "HIP_LEFT",
    "CocoPart.RHip": "HIP_RIGHT",
    "CocoPart.LShoulder": "SHOULDER_LEFT",
    "CocoPart.REar": "EAR_RIGHT",
    "CocoPart.LKnee": "KNEE_RIGHT",
    "CocoPart.LWrist": "WRIST_LEFT"
}


logger = logging.getLogger("TfPoseEstimator-Video")
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="tf-pose-estimation Video Processor")
    parser.add_argument("--video", type=str, required=True, help="Input video path")
    parser.add_argument("--output", type=str, required=True, help="Output video path")
    parser.add_argument("--resolution", type=str, default="432x368", help="network input resolution")
    parser.add_argument("--model", type=str, default="mobilenet_thin", help="cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small")
    parser.add_argument("--show-process", type=bool, default=False, help="debug: slow inference")
    parser.add_argument("--showBG", type=bool, default=True, help="Show background")
    args = parser.parse_args()
    w, h = model_wh(args.resolution)
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    # durch Videos iterieren
    os.makedirs(args.output, exist_ok=True)
    files = os.listdir(args.video)
    mp4_files = list(filter(lambda x: x.endswith(".mp4"), files))
    for file_name in mp4_files:
        cap = cv2.VideoCapture(os.path.join(args.video, file_name))
        data = []

        if not cap.isOpened():
            logger.error(f"Cannot open video file: {args.video}")
            exit(1)

        # Video writer setup
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # "mp4v" for .mp4
        out = cv2.VideoWriter(os.path.join(args.output, file_name), fourcc, fps, (frame_width, frame_height))

        logger.info(f"Processing video: {args.video}")
        logger.info(f"Saving output to: {args.output}")

        frame_count = 0
        start_time = time.time()
        while cap.isOpened():
            ret, image = cap.read()
            if not ret:
                break

            frame_data = []
            humans = e.inference(image, upsample_size=4.0)

            # Ausgabe der strukturierten Daten als JSON
            for human in humans:
                human_data = {JOINT_NAMES_TRANSLATE[str(body_part.get_part_name())]: {
                    "x": body_part.x,
                    "y": body_part.y,
                    "score": body_part.score
                } for body_part_id, body_part in human.body_parts.items()}
                frame_data.append(human_data)
            data.append(frame_data)

            # Ausgabe des Bildes
            if not args.showBG:
                image = np.zeros(image.shape)
            image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)
            out.write(image)

            frame_count += 1

        cap.release()
        out.release()

        with open(f"{args.output}/{file_name}.json", "w") as f:
            json.dump(data, f)

        logger.info(f"Finished processing {frame_count} frames in {time.time() - start_time:.2f} seconds.")
