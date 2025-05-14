# Quelle: https://github.com/me-X-us/simple-HRNet-docker/blob/master/Dockerfile (bearbeitet)
FROM ubuntu:20.04
RUN apt-get update &&\
    DEBIAN_FRONTEND=noninteractive \
    apt-get install -y --no-install-recommends git python3-pip ffmpeg libsm6 libxext6 curl unzip wget &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip3 install gdown &&\
    git clone https://github.com/stefanopini/simple-HRNet.git &&\
    pip3 install -r /simple-HRNet/requirements.txt
WORKDIR /simple-HRNet/models_
RUN python3 -c "import gdown;gdown.download(id='1assh2z-rVLZRSiNZ-2EE7MedRDqwodeP', output='pytorch.zip')" &&\
    unzip pytorch.zip -d ./pytorch &&\
    rm ./pytorch.zip &&\
    mkdir /simple-HRNet/weights &&\
    python3 -c "import gdown;gdown.download(id='1UoJhTtjHNByZSm96W3yFTfU5upJnsKiS', output='/simple-HRNet/weights/pose_hrnet_w48_384x288.pth')"
WORKDIR /simple-HRNet/models_/detectors
RUN rm -d yolo &&\
    wget https://github.com/eriklindernoren/PyTorch-YOLOv3/archive/47b7c912877ca69db35b8af3a38d6522681b3bb3.zip -O yolo.zip &&\
    unzip yolo.zip -d ./yolo &&\
    rm ./yolo.zip &&\
    mv yolo/*/* yolo &&\
    pip3 install -r yolo/requirements.txt
WORKDIR /simple-HRNet/models_/detectors/yolo/weights
RUN chmod 777 download_weights.sh &&\
    ./download_weights.sh
WORKDIR /simple-HRNet
CMD python3 scripts/live-demo.py --filename /data/input.mp4 --save_video &&\
    mv output.avi /data/hrnet.avi