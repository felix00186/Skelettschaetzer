FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04

# Systemabhaengigkeiten installieren
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        python3-dev \
        git \
        wget \
        libsm6 \
        libxext6 \
        libx264-dev \
        libxrender-dev \
        libglib2.0-0 \
        libgtk2.0-dev \
        pkg-config \
        libopenblas-dev \
        g++ \
        gcc \
        libomp-dev \
        libyaml-dev &&\
    apt-get clean &&\
    rm -rf /var/lib/apt/lists/*
RUN wget https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-amd64-static.tar.xz && \
    tar -xJf ffmpeg-release-amd64-static.tar.xz && \
    mv ffmpeg-*-static/ffmpeg /usr/local/bin/ffmpeg && \
    chmod +x /usr/local/bin/ffmpeg && \
    rm -rf ffmpeg-*-static*
WORKDIR /app

# Miniconda installieren
ENV CONDA_DIR=/opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -afy
ENV PATH=$CONDA_DIR/bin:$PATH

COPY environment.yml /app/environment.yml
RUN conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main &&\
    conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r &&\
    conda env create -f /app/environment.yml
ENV CONDA_DEFAULT_ENV=alphapose
ENV PATH=$CONDA_DIR/envs/alphapose/bin:$PATH
ENV FORCE_CUDA="1"
ENV CUDA_HOME=/usr/local/cuda
ENV PATH=$CUDA_HOME/bin:$PATH
ENV LD_LIBRARY_PATH=$CONDA_DIR/envs/alphapose/lib:/usr/local/cuda/lib64/:$LD_LIBRARY_PATH
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

WORKDIR /app/detector/yolo
COPY yolov3-spp.weights .
RUN git clone --branch v0.7.5 https://github.com/facebookresearch/pytorch3d.git /tmp/pytorch3d
WORKDIR /tmp/pytorch3d
RUN pip install -e . &&\
    git clone https://github.com/MVIG-SJTU/AlphaPose.git /app/AlphaPose
WORKDIR /app/AlphaPose
RUN pip install -e .
COPY coco_wholebody133_fast152_duc_regression_256x192.pth checkpoint.pth
ENV CFG=configs/coco_wholebody/resnet/256x192_res152_lr1e-3_1x-duc.yaml

COPY exec.sh .

CMD ["/bin/bash", "exec.sh"]