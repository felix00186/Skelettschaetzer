#!/bin/bash

# Verzeichnis mit den Videos
INPUT_DIR="/data/input"
OUTPUT_DIR="/data/AlphaPose"

# Über alle MP4-Dateien im Eingabeordner iterieren
for VIDEO_PATH in "$INPUT_DIR"/*.mp4; do
  # Nur weitermachen, wenn Datei existiert
  [ -e "$VIDEO_PATH" ] || continue

  # Dateiname ohne Verzeichnis und Endung
  FILENAME=$(basename "$VIDEO_PATH" .mp4)
  OUTPUT_PATH="$OUTPUT_DIR/$FILENAME.mp4"

  python scripts/demo_inference.py \
         --video "$VIDEO_PATH" \
         --outdir "$OUTPUT_DIR" \
         --cfg "$CFG" \
         --checkpoint checkpoint.pth \
         --save-video --showbox

done
