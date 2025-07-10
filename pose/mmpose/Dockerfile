FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


WORKDIR /app
COPY requirements.txt .
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update && apt-get install -y \
        libgl1=1.0.0-2ubuntu2.3 \
        libglib2.0-0=2.56.4-0ubuntu0.18.04.9 \
        git \
        wget &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements.txt --use-deprecated=legacy-resolver &&\
    mim install "mmcv==2.0.0" &&\
    mim install mmengine &&\
    mim install mmdet &&\
    git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
RUN git checkout 71ec36ebd63c475ab589afc817868e749a61491f &&\
    pip install -e .
COPY exec.py .
ARG POSE_CHECKPOINT_DOWNLOAD
RUN wget "${POSE_CHECKPOINT_DOWNLOAD}" &&\
    mkdir _joint_names
ARG JOINT_NAMES
COPY _joint_names _joint_names
RUN mv ./_joint_names/${JOINT_NAMES}.json joint_names.json &&\
    rm -rd _joint_names


CMD ["python", "exec.py"]
