#!/bin/bash

INPUT_DIR="/data/input"
OUTPUT_DIR="/data/OpenPifPaf"
JSON_OUTPUT_DIR="/cache"

mkdir -p "$OUTPUT_DIR"
mkdir -p "$JSON_OUTPUT_DIR"

for video in "$INPUT_DIR"/*.mp4; do
  if [[ -f "$video" ]]; then
    echo "Verarbeite: $video"
    filename=$(basename "$video")
    video_output_file="$OUTPUT_DIR/$filename"
    rm -f "$video_output_file"
    python3 -m openpifpaf.video \
            --source "$video" \
            --video-output "$video_output_file" \
            --json-output "$JSON_OUTPUT_DIR/$filename.json"
    width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 "$video")
    height=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 "$video")
    python3 json_transformer.py "$width" "$height" "$JSON_OUTPUT_DIR/$filename.json"
  fi
done
