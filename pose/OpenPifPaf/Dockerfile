FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


ENV CHECKPOINT=shufflenetv2k30
RUN pip3 install matplotlib openpifpaf==0.12.14 opencv-python
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update &&\
    apt-get install -y wget \
                       libgl1 \
                       libglib2.0-0
WORKDIR /app
RUN mkdir -p /root/.cache/torch/hub/checkpoints &&\
    wget http://github.com/vita-epfl/openpifpaf-torchhub/releases/download/v0.12.6/shufflenetv2k30-210409-024202-cocokp-o10s-f4fb0807.pkl -O /root/.cache/torch/hub/checkpoints/shufflenetv2k30-210409-024202-cocokp-o10s-f4fb0807.pkl
COPY exec.py .


CMD ["python", "exec.py"]