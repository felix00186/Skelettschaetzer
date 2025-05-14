FROM python:3.6-slim
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
RUN apt-get update &&\
    apt-get install -y --no-install-recommends git ffmpeg libsm6 libxext6 curl unzip tar wget make bzip2 &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install torch torchvision torchaudio gdown &&\
    git clone https://github.com/leoxiaobin/deep-high-resolution-net.pytorch.git /app &&\
    pip install -r /app/requirements.txt
WORKDIR /app/lib
RUN make &&\
    git clone https://github.com/cocodataset/cocoapi.git /coco
WORKDIR /coco/PythonAPI
RUN make install
WORKDIR /app
RUN mkdir output && \
    mkdir log && \
    python3 -c "import gdown;gdown.download_folder('https://drive.google.com/drive/folders/1hOTihvbyIxsm5ygDpbUuJ7O_tzv4oXjC')" &&\
    python3 -c "import gdown;gdown.download_folder('https://drive.google.com/drive/folders/159PKd3GYKsV2FCa9YjJ4YecYtWkjgaOE')" &&\
    wget https://datasets.d2.mpi-inf.mpg.de/andriluka14cvpr/mpii_human_pose_v1.tar.gz &&\
    tar -xzf mpii_human_pose_v1.tar.gz -C data/mpii &&\
    rm mpii_human_pose_v1.tar.gz
WORKDIR /app/data/coco
RUN mkdir images &&\
    wget http://images.cocodataset.org/zips/train2017.zip &&\
    unzip train2017.zip -d images &&\
    rm train2017.zip &&\
    wget http://images.cocodataset.org/zips/val2017.zip &&\
    unzip val2017.zip -d images &&\
    rm val2017.zip &&\
    mkdir annotations &&\
    wget https://huggingface.co/datasets/merve/coco/resolve/main/annotations/person_keypoints_train2017.json -P annotations &&\
    wget https://huggingface.co/datasets/merve/coco/resolve/main/annotations/person_keypoints_val2017.json -P annotations
WORKDIR /app
RUN python3 tools/train.py --cfg experiments/mpii/hrnet/w32_256x256_adam_lr1e-3.yaml

CMD ["python", "demo/inference.py",\
     "--cfg", "demo/inference-config.yaml",\
     "--videoFile", "/data/input.mp4",\
     "--writeBoxFrames",\
     "--outputDir", "/data",\
     "TEST.MODEL_FILE", "./models/pytorch/pose_coco/pose_hrnet_w32_256x192.pth"]