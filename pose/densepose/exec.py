import os
import argparse
import glob
import cv2

from detectron2.config import get_cfg
from detectron2.engine import DefaultPredictor
from densepose import add_densepose_config
from detectron2.utils.visualizer import Visualizer
from detectron2.data import MetadataCatalog

def setup_cfg():
    cfg = get_cfg()
    add_densepose_config(cfg)
    cfg.merge_from_file("detectron2/projects/DensePose/configs/densepose_rcnn_R_50_FPN_WC1M_s1x.yaml")
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
    cfg.MODEL.WEIGHTS = "https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_WC1M_s1x/217144516/model_final_48a9d9.pkl"
    cfg.MODEL.DEVICE = "cuda"
    return cfg

def process_video(video_path, output_path, predictor):
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    metadata = MetadataCatalog.get("detectron2_dataset_train")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        outputs = predictor(frame)
        v = Visualizer(frame[:, :, ::-1], metadata=metadata)
        result = v.draw_instance_predictions(outputs["instances"].to("cpu"))

        out.write(result.get_image()[:, :, ::-1])

    cap.release()
    out.release()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", required=True)
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    cfg = setup_cfg()
    predictor = DefaultPredictor(cfg)

    os.makedirs(args.output_dir, exist_ok=True)
    video_files = glob.glob(os.path.join(args.input_dir, "*.mp4"))

    for video_path in video_files:
        filename = os.path.basename(video_path)
        output_path = os.path.join(args.output_dir, filename)
        print(f"Processing {filename}...")
        process_video(video_path, output_path, predictor)
