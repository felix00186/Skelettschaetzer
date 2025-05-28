FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


# MMCV installieren
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update && apt-get install -y libgl1 \
        libglib2.0-0 \
        libgtk2.0-dev \
        pkg-config \
        git \
        wget &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -U pip setuptools wheel openmim &&\
    mim install 'mmcv-full==1.4.0' &&\
    pip install mmdet==2.25.1 \
        opencv-python-headless \
        numpy \
        scipy \
        tqdm \
        pillow \
        matplotlib \
        scikit-learn

# MMpose installieren
WORKDIR /app
RUN git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
RUN git checkout v0.20.0 &&\
    pip install -r requirements.txt &&\
    pip install -e . &&\
    sed -i "s/cv2.waitKey(1) & 0xFF == ord('q')/False/g" demo/top_down_pose_tracking_demo_with_mmdet.py &&\
    sed -i "s/cv2.destroyAllWindows()//g" demo/top_down_pose_tracking_demo_with_mmdet.py &&\
    mkdir /output

# Herunterladen des Modells
RUN wget https://download.openmmlab.com/mmpose/top_down/deeppose/deeppose_res50_coco_256x192-f6de6c0e_20210205.pth &&\
    wget https://download.openmmlab.com/mmdetection/v2.0/faster_rcnn/faster_rcnn_r50_fpn_1x_coco/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth


CMD ["sh", "-c", "python demo/top_down_pose_tracking_demo_with_mmdet.py demo/mmdetection_cfg/faster_rcnn_r50_fpn_coco.py faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth configs/body/2d_kpt_sview_rgb_img/deeppose/coco/res50_coco_256x192.py ./deeppose_res50_coco_256x192-f6de6c0e_20210205.pth --video-path /data/input.mp4 --out-video-root /output && mv /output/vis_input.mp4 /data/deeppose.mp4"]