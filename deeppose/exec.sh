#!/bin/bash

INPUT_DIR="/data/input"
OUTPUT_DIR="/data/deeppose"
mkdir -p "$OUTPUT_DIR"

# Durchlaufe alle .mp4-Dateien im Eingabeordner
for VIDEO in "$INPUT_DIR"/*.mp4; do
    echo "Verarbeite $VIDEO..."

    python demo/top_down_pose_tracking_demo_with_mmdet.py \
        demo/mmdetection_cfg/faster_rcnn_r50_fpn_coco.py \
        faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth \
        configs/body/2d_kpt_sview_rgb_img/deeppose/coco/res50_coco_256x192.py \
        ./deeppose_res50_coco_256x192-f6de6c0e_20210205.pth \
        --video-path "$VIDEO" \
        --out-video-root "$OUTPUT_DIR"

    mv "$OUTPUT_DIR/vis_$VIDEO" "$OUTPUT_DIR/$VIDEO"
done

echo "Alle Videos wurden verarbeitet."
