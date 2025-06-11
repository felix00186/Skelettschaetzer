FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel

WORKDIR /app
COPY requirements.txt .
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update && \
    apt-get install -y --no-install-recommends \
        git \
        ffmpeg \
        libsm6 \
        libxext6 \
        wget \
        ca-certificates \
        coreutils && \
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements.txt &&\
    git clone https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git pose_estimation
WORKDIR /app/pose_estimation
RUN wget https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth -O models/checkpoint_iter_370000.pth
WORKDIR /app
COPY exec.py .
COPY joint_names.json .

CMD ["python", "exec.py", \
     "--checkpoint-path", "/app/pose_estimation/models/checkpoint_iter_370000.pth", \
     "--video", "/data/input", \
     "--output-video", "/data/lightweight"]