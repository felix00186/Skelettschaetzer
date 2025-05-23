import argparse
import logging
import time
import cv2
import numpy as np
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator-Video')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation Video Processor')
    parser.add_argument('--video', type=str, required=True, help='Input video path')
    parser.add_argument('--output', type=str, required=True, help='Output video path')
    parser.add_argument('--resolution', type=str, default='432x368', help='network input resolution')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--show-process', type=bool, default=False, help='debug: slow inference')
    parser.add_argument('--showBG', type=bool, default=True, help='Show background')
    args = parser.parse_args()

    w, h = model_wh(args.resolution)
    if w == 0 or h == 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h))

    cap = cv2.VideoCapture(args.video)
    if not cap.isOpened():
        logger.error(f"Cannot open video file: {args.video}")
        exit(1)

    # Video writer setup
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 'mp4v' for .mp4
    out = cv2.VideoWriter(args.output, fourcc, fps, (frame_width, frame_height))

    logger.info(f"Processing video: {args.video}")
    logger.info(f"Saving output to: {args.output}")

    frame_count = 0
    start_time = time.time()
    while cap.isOpened():
        ret, image = cap.read()
        if not ret:
            break

        humans = e.inference(image, upsample_size=4.0)
        if not args.showBG:
            image = np.zeros(image.shape)
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        out.write(image)
        frame_count += 1

    cap.release()
    out.release()
    logger.info(f"Finished processing {frame_count} frames in {time.time() - start_time:.2f} seconds.")
