FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


# MMCV installieren
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
    mim install "mmcv==2.2.0" &&\
    mim install mmengine &&\
    mim install mmdet &&\
    git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
ENV BASE_PATH=/app/mmpose/configs/_base_/
ENV POSE_CONFIG=configs/body_2d_keypoint/topdown_heatmap/coco/td-hm_cpm_8xb32-210e_coco-384x288.py
ENV POSE_CHECKPOINT=td-hm_cpm_8xb32-210e_coco-384x288-165487b8_20221011.pth
ENV DET_CONFIG=rtmdet_s_8xb32-300e_coco.py
ENV DET_CHECKPOINT=cspnext-s_imagenet_600e.pth
RUN pip install -e . &&\
    mkdir models &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmpose/refs/heads/dev-1.x/$POSE_CONFIG -O $POSE_CONFIG
WORKDIR $BASE_PATH
RUN wget https://download.openmmlab.com/mmpose/v1/body_2d_keypoint/topdown_heatmap/coco/$POSE_CHECKPOINT &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmdetection/621b8c8dc1bed2d6116eed8b741d8d356e3f372a/configs/rtmdet/$DET_CONFIG &&\
    sed -i "s=https://download.openmmlab.com/mmdetection/v3.0/rtmdet/cspnext_rsb_pretrain/cspnext-s_imagenet_600e.pth=$DET_CHECKPOINT=g" $DET_CONFIG &&\
    wget https://download.openmmlab.com/mmdetection/v3.0/rtmdet/cspnext_rsb_pretrain/$DET_CHECKPOINT &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmdetection/621b8c8dc1bed2d6116eed8b741d8d356e3f372a/configs/rtmdet/rtmdet_l_8xb32-300e_coco.py &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmdetection/621b8c8dc1bed2d6116eed8b741d8d356e3f372a/configs/_base_/datasets/coco_detection.py -O datasets/coco_detection.py &&\
    mkdir schedules &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmdetection/4dd2c3daa2a352f331f2649248586e3ea9b7d1ea/configs/_base_/schedules/schedule_1x.py -O schedules/schedule_1x.py
WORKDIR /app/mmpose
COPY exec.py .
COPY joint_names.json .


CMD ["python", "exec.py"]
