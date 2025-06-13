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
        wget \
        rsync &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements.txt --use-deprecated=legacy-resolver &&\
    mim install "mmcv==2.2.0" &&\
    mim install mmengine &&\
    mim install mmdet &&\
    git clone https://github.com/open-mmlab/mmdetection.git &&\
    cd mmdetection && git reset --hard cfd5d3a985b0249de009b67d04f37263e11cdf3d && cd .. &&\
    git clone https://github.com/open-mmlab/mmpose.git &&\
    cd mmpose && git reset --hard 71ec36ebd63c475ab589afc817868e749a61491f && cd .. &&\
    rsync -a mmpose/ mmdetection/ &&\
    rm -rd mmpose
WORKDIR /app/mmdetection
ENV POSE_CONFIG=configs/body_2d_keypoint/topdown_heatmap/coco/td-hm_cpm_8xb32-210e_coco-384x288.py
ENV POSE_CHECKPOINT=td-hm_cpm_8xb32-210e_coco-384x288-165487b8_20221011.pth
ENV DET_CONFIG=configs/faster_rcnn/faster-rcnn_x101-64x4d_fpn_ms-3x_coco.py
ENV DET_CHECKPOINT=faster-rcnn_x101-64x4d_fpn_ms-3x_coco
RUN pip install -e . &&\
    wget https://download.openmmlab.com/mmpose/v1/body_2d_keypoint/topdown_heatmap/coco/$POSE_CHECKPOINT &&\
    wget https://download.openxlab.org.cn/models/mmdetection/FasterR-CNN/weight/faster-rcnn_x101-64x4d_fpn_ms-3x_coco
COPY exec.py .
COPY joint_names.json .


CMD ["python", "exec.py"]
