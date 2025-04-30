FROM python:3.10-slim

WORKDIR /app

# Grundpakete installieren
RUN apt-get update && \
    apt-get install -y --no-install-recommends git ffmpeg libsm6 libxext6 wget ca-certificates coreutils && \
    rm -rf /var/lib/apt/lists/*

# Python-Bibliotheken installieren
RUN pip install torch torchvision opencv-python pycocotools

# Lightweight HRNet-Repo klonen
RUN git clone https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git pose_estimation
WORKDIR /app/pose_estimation

# Pretrained Modell herunterladen
RUN wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth -O models/checkpoint_iter_370000.pth

# Unser eigenes Skript kopieren
WORKDIR /app
COPY lw.py .

CMD ["python", "lw.py", "--checkpoint-path", "/app/pose_estimation/models/checkpoint_iter_370000.pth", "--video", "/data/input.mp4", "--output-video", "/data/lightweight.mp4", "--cpu"]