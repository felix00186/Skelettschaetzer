FROM python:3.11-slim

WORKDIR /app

# Installiere notwendige Pakete
RUN apt-get update &&\
    apt-get install -y ffmpeg libsm6 libxext6 &&\
    pip install mediapipe opencv-python

# Kopiere das Python-Skript
COPY blazepose.py .

# Starte das Skript beim Containerstart
CMD ["python", "blazepose.py"]