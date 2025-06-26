FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
        git \
        ffmpeg=7:4.2.7-0ubuntu0.1 \
        libgl1=1.3.2-1~ubuntu0.20.04.2 \
        build-essential=12.8ubuntu1.1 \
        wget &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Detectron2 and DensePose
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone https://github.com/facebookresearch/detectron2.git detectron2 &&\
    cd detectron2 && git checkout b15f64ec4429e23a148972175a0207c5a9ab84cf && cd .. &&\
    pip install -e detectron2
WORKDIR /app/detectron2/projects/DensePose
RUN pip install -e .

WORKDIR /app
RUN wget https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_DL_s1x/165712097/model_final_0ed407.pkl
COPY exec.py .

CMD ["python", "exec.py"]
