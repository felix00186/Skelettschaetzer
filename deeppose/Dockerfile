FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


# MMCV installieren
COPY requirements_1.txt .
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update && apt-get install -y \
        libgl1=1.0.0-2ubuntu2.3 \
        libglib2.0-0=2.56.4-0ubuntu0.18.04.9 \
        libgtk2.0-dev=2.24.32-1ubuntu1 \
        pkg-config=0.29.1-0ubuntu2 \
        git \
        wget &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -r requirements_1.txt &&\
    mim install 'mmcv-full==1.4.0'

# MMpose installieren
WORKDIR /app
COPY requirements_2.txt .
RUN pip install -r requirements_2.txt &&\
    git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
RUN git checkout v0.20.0 &&\
    pip install . &&\
    sed -i "s/cv2.waitKey(1) & 0xFF == ord('q')/False/g" demo/top_down_pose_tracking_demo_with_mmdet.py &&\
    sed -i "s/cv2.destroyAllWindows()//g" demo/top_down_pose_tracking_demo_with_mmdet.py

# Herunterladen des Modells
RUN wget https://download.openmmlab.com/mmpose/top_down/deeppose/deeppose_res50_coco_256x192-f6de6c0e_20210205.pth &&\
    wget https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth
COPY exec.sh .


CMD ["/bin/bash", "exec.sh"]