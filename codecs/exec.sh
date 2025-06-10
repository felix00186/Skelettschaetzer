#!/bin/bash


BASE_DIR="/data"

# Alle .mp4-Dateien in zweiter Ebene durchgehen, Ordner "input" ignorieren
find "$BASE_DIR" -mindepth 2 -maxdepth 2 -type f -name "*.mp4" ! -path "*/input/*" | while read -r file; do
  dir=$(dirname "$file")
  base=$(basename "$file" .mp4)
  tmp_output="${dir}/${base}_tmp.mp4"

  echo "Konvertiere: $file"

  # Konvertieren mit FFmpeg
  ffmpeg -y -i "$file" -vcodec libx264 -crf 23 -pix_fmt yuv420p "$tmp_output"

  # Wenn erfolgreich, ersetze Original
  if [ -f "$tmp_output" ]; then
    mv "$tmp_output" "$file"
    echo "Erfolgreich überschrieben: $file"
  else
    echo "Fehlgeschlagen: $file"
  fi
done
