FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


WORKDIR /app
ENV CHECKPOINT=shufflenetv2k30
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update &&\
    apt-get install -y wget \
                       ffmpeg &&\
    pip3 install matplotlib openpifpaf==0.12.14 opencv-python-headless
COPY exec.sh .


CMD ["/bin/bash", "exec.sh"]