#!/bin/bash

INPUT_DIR="/data/input"
OUTPUT_DIR="/data/higher-hrnet"
mkdir -p "$OUTPUT_DIR"

# Durchlaufe alle .mp4-Dateien im Eingabeordner
for VIDEO in "$INPUT_DIR"/*.mp4; do
    echo "Verarbeite $VIDEO..."

    python demo/bottom_up_pose_tracking_demo.py \
        configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py \
        ./higher_hrnet32_coco_512x512-8ae85183_20200713.pth \
        --video-path "$VIDEO" \
        --out-video-root "$OUTPUT_DIR"

done

for f in "$OUTPUT_DIR"/*; do
    new_name="$(basename "$f" | sed 's/vis_//g')"
    mv "$f" "$(dirname "$f")/$new_name"
done

echo "Alle Videos wurden verarbeitet."
