#!/bin/bash

mkdir -p /data/PoseNet

for file in /data/input/*.mp4; do
  if [ -f "$file" ]; then
    echo "Verarbeite $file"
    node process.js "$file"
  fi
done
