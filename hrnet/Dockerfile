FROM pytorch/pytorch:1.8.1-cuda10.2-cudnn7-devel


# MMCV installieren
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
    mim install 'mmcv-full<=1.6.0rc'

# HigherHRNet installieren
WORKDIR /app
RUN git clone https://github.com/open-mmlab/mmpose.git
WORKDIR /app/mmpose
RUN git checkout v0.25.1 &&\
    sed -i "s/get_version(),/'0.25.1',/g" setup.py &&\
    pip install -e . &&\
    wget https://download.openmmlab.com/mmpose/bottom_up/higher_hrnet32_coco_512x512-8ae85183_20200713.pth &&\
    wget https://raw.githubusercontent.com/open-mmlab/mmpose/refs/heads/master/configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py -O configs/body/2d_kpt_sview_rgb_img/associative_embedding/coco/higherhrnet_w32_coco_512x512.py
COPY exec.sh .

CMD ["/bin/bash", "exec.sh"]