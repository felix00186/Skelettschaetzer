#!/bin/bash

# Verzeichnis mit den Videos
INPUT_DIR="/data/input"
OUTPUT_DIR="/data/openpose"
JSON_DIR="/cache"
mkdir -p $OUTPUT_DIR
mkdir -p $JSON_DIR

# OpenPose-Binärpfad
OPENPOSE_BIN="build/examples/openpose/openpose.bin"

# Über alle MP4-Dateien im Eingabeordner iterieren
for VIDEO_PATH in "$INPUT_DIR"/*.mp4; do
  # Nur weitermachen, wenn Datei existiert
  [ -e "$VIDEO_PATH" ] || continue

  # Dateiname ohne Verzeichnis und Endung
  FILENAME=$(basename "$VIDEO_PATH" .mp4)

  # Zielpfad für JSON-Dateien
  JSON_PATH="$JSON_DIR/$FILENAME"
  OUTPUT_PATH="$OUTPUT_DIR/$FILENAME.mp4"

  echo "Verarbeite: $VIDEO_PATH → $JSON_PATH"

  "$OPENPOSE_BIN" \
    --video "$VIDEO_PATH" \
    --write_json "$JSON_PATH" \
    --write_video "$OUTPUT_PATH" \
    --display 0 \
    --render_pose 1

  width=$(ffprobe -v error -select_streams v:0 -show_entries stream=width -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH")
  height=$(ffprobe -v error -select_streams v:0 -show_entries stream=height -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH")
  python3 json_transform.py "$width" "$height" "$FILENAME"
done
