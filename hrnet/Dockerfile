FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


# MMCV installieren
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update && apt-get install -y libgl1 libglib2.0-0 git wget &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install -U openmim &&\
    mim install 'mmcv-full<=1.6.0rc'

# HigherHRNet installieren
WORKDIR /app
RUN git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
RUN git checkout v0.25.1 &&\
    pip install -r requirements.txt &&\
    sed -i "s/get_version(),/'0.25.1',/g" setup.py &&\
    pip install -e . &&\
    wget https://download.openmmlab.com/mmpose/bottom_up/higher_hrnet32_coco_512x512-8ae85183_20200713.pth &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmpose/refs/heads/master/configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py -O configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py

CMD ["sh", "-c", "python demo/bottom_up_pose_tracking_demo.py configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py ./higher_hrnet32_coco_512x512-8ae85183_20200713.pth --video-path /data/input.mp4 --out-video-root /data && mv /data/vis_input.mp4 /data/hrnet.mp4"]