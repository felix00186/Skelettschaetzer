FROM python:3.10-slim

WORKDIR /app
COPY requirements.txt .
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        ffmpeg=7:5.1.6-0+deb12u1 \
        libsm6=2:1.2.3-1 \
        libxext6=2:1.3.4-1+b1 \
        wget \
        ca-certificates=20230311 \
        coreutils=9.1-1 && \
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements.txt &&\
    git clone https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git pose_estimation
WORKDIR /app/pose_estimation
RUN wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth -O models/checkpoint_iter_370000.pth
WORKDIR /app
COPY exec.py .

CMD ["python", "exec.py", \
     "--checkpoint-path", "/app/pose_estimation/models/checkpoint_iter_370000.pth", \
     "--video", "/data/input", \
     "--output-video", "/data/lightweight"]