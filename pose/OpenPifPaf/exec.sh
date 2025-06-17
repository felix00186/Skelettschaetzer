#!/bin/bash

INPUT_DIR="/data/input"
OUTPUT_DIR="/data/OpenPifPaf"

mkdir -p "$OUTPUT_DIR"

for video in "$INPUT_DIR"/*.mp4; do
  if [[ -f "$video" ]]; then
    echo "Verarbeite: $video"
    filename=$(basename "$video")
    python3 -m openpifpaf.video --source "$video" --video-output "$OUTPUT_DIR/$filename"
  fi
done
