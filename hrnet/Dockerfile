# Quelle: https://github.com/me-X-us/simple-HRNet-docker/blob/master/Dockerfile (bearbeitet)
FROM ubuntu:20.04
RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends git \
                                                                              python3-pip \
                                                                              ffmpeg \
                                                                              libsm6 \
                                                                              libxext6 \
                                                                              curl \
                                                                              unzip \
                                                                              wget &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip3 install gdown &&\
    git clone https://github.com/stefanopini/simple-HRNet.git
WORKDIR /simple-HRNet
RUN pip3 install -r requirements.txt
WORKDIR /simple-HRNet/models_
RUN python3 -c "import gdown;gdown.download(id='1assh2z-rVLZRSiNZ-2EE7MedRDqwodeP', output='pytorch.zip')" &&\
    unzip pytorch.zip -d ./pytorch && rm ./pytorch.zip
WORKDIR /simple-HRNet
RUN mkdir weights
WORKDIR /simple-HRNet/weights
RUN python3 -c "import gdown;gdown.download(id='1zYC7go9EV0XaSlSBjMaiyE_4TcHc_S38', output='pose_hrnet_w48_384x288.pth')"
WORKDIR /simple-HRNet/models_/detectors
# TODO: https://github.com/eriklindernoren/PyTorch-YOLOv3/tree/47b7c912877ca69db35b8af3a38d6522681b3bb3 herunterladen
RUN rm -d yolo &&\
    git clone https://github.com/eriklindernoren/PyTorch-YOLOv3 &&\
    mv PyTorch-YOLOv3 yolo &&\
    pip3 install numpy torch>=1.0 torchvision matplotlib tensorflow tensorboard terminaltables pillow tqdm
WORKDIR /simple-HRNet/models_/detectors/yolo
RUN wget https://raw.githubusercontent.com/eriklindernoren/PyTorch-YOLOv3/47b7c912877ca69db35b8af3a38d6522681b3bb3/models.py
WORKDIR /simple-HRNet/models_/detectors/yolo/weights
RUN chmod 777 download_weights.sh &&\
    ./download_weights.sh
WORKDIR /simple-HRNet
#CMD ls /simple-HRNet/models_/detectors/yolo
CMD python3 scripts/live-demo.py --filename /data/input.mp4