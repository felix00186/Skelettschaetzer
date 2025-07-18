#!/bin/bash

# Verzeichnis mit den Videos
INPUT_DIR="/data/input"
OUTPUT_DIR="/data/HybrIK"
CACHE_DIR="cache"

# Über alle MP4-Dateien im Eingabeordner iterieren
for VIDEO_PATH in "$INPUT_DIR"/*.mp4; do
  # Nur weitermachen, wenn Datei existiert
  [ -e "$VIDEO_PATH" ] || continue
  echo "Verarbeite $VIDEO_PATH ..."

  # Dateiname ohne Verzeichnis und Endung
  FILENAME=$(basename "$VIDEO_PATH" .mp4)
  OUTPUT_PATH="$OUTPUT_DIR/$FILENAME.mp4"

  python scripts/demo_video_x.py --video-name "$VIDEO_PATH" --out-dir "$CACHE_DIR"

done

mkdir -p "$OUTPUT_DIR"
mv $CACHE_DIR/* "$OUTPUT_DIR"
