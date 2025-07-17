FROM pytorch/pytorch:2.0.0-cuda11.7-cudnn8-devel

RUN rm /etc/apt/sources.list.d/cuda.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update &&\
    apt-get install -y \
      ffmpeg \
      git \
      wget &&\
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt &&\
    wget https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8x-pose.pt
COPY exec.py .
COPY joint_names.json .


CMD ["python", "exec.py"]