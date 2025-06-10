#!/bin/bash

BASE_DIR="/data"

# Finde alle MP4-Dateien (außerhalb von input-Verzeichnissen) und speichere sie in einer temporären Liste
exec 3< <(find "$BASE_DIR" -mindepth 2 -maxdepth 2 -type f -name "*.mp4" ! -path "*/input/*")
while read -r file <&3; do
  dir=$(dirname "$file")
  base=$(basename "$file" .mp4)
  tmp_output="${dir}/${base}_tmp.mp4"

  echo "Konvertiere: $file"

  ffmpeg -y -i "$file" -vcodec libx264 -crf 23 -pix_fmt yuv420p "$tmp_output"

  if [ -f "$tmp_output" ]; then
    mv "$tmp_output" "$file"
    echo "Erfolgreich überschrieben: $file"
  else
    echo "Fehlgeschlagen: $file"
  fi
done
