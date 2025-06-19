#!/bin/bash

python exec.py

MAX_PIXELS=307200
dir="/data/input"

for file in $dir/*.mp4; do
  # Prüfen, ob Datei existiert
  [ -e "$file" ] || continue

  echo "Verarbeite: $file"

  # Aktuelle Breite und Höhe mit ffprobe ermitteln
  read width height <<< $(ffprobe -v error -select_streams v:0 \
    -show_entries stream=width,height \
    -of "csv=p=0:s=' '" "$file")

  # Berechne aktuelle Pixelanzahl
  current_pixels=$((width * height))

  if [ "$current_pixels" -le "$MAX_PIXELS" ]; then
    echo "  → Auflösung ist kleiner oder gleich $MAX_PIXELS px, überspringe."
    continue
  fi

  # Neue Höhe und Breite berechnen, sodass neue_breite * neue_höhe <= MAX_PIXELS
  aspect_ratio=$(echo "scale=10; $width / $height" | bc)

  new_height=$(echo "scale=10; sqrt($MAX_PIXELS / $aspect_ratio)" | bc)
  new_height=$(echo "$new_height / 2" | bc)
  new_height=$(echo "$new_height * 2" | bc)
  new_height=${new_height%.*}

  new_width=$(echo "scale=10; $new_height * $aspect_ratio" | bc)
  new_width=$(echo "$new_width / 2" | bc)
  new_width=$(echo "$new_width * 2" | bc)
  new_width=${new_width%.*}

  echo "  → Neue Auflösung: ${new_width}x${new_height}"

  # Ausgabedatei
  basename="$(basename $file)"
  output=$dir/scaled_$basename

  # ffmpeg zum Skalieren
  ffmpeg -i "$file" -vf "scale=${new_width}:${new_height}" -c:a copy "$output"
  mv $output $file
done
