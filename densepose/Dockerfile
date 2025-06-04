FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

# Systemabhängigkeiten
RUN apt-get update && apt-get install -y \
    wget \
    git \
    ca-certificates=20230311ubuntu0.18.04.1 \
    libglib2.0-0=2.56.4-0ubuntu0.18.04.9 \
    libsm6=2:1.2.2-1 \
    libxext6=2:1.3.3-1 \
    libxrender-dev=1:0.9.10-1 \
    build-essential=12.4ubuntu1 \
    ninja-build=1.8.2-1 \
    libgl1=1.0.0-2ubuntu2.3 \
    python3-distutils=3.6.9-1~18.04 \
    pkg-config=0.29.1-0ubuntu2 \
    unzip && \
    rm -rf /var/lib/apt/lists/*

# Miniconda installieren
ENV CONDA_DIR=/opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -afy
ENV PATH=$CONDA_DIR/bin:$PATH

# Detectron 2 installieren
COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml
ENV CONDA_DEFAULT_ENV=detectron
ENV PATH=$CONDA_DIR/envs/detectron/bin:$PATH
ENV FORCE_CUDA="1"
ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV PATH=$CUDA_HOME/bin:$PATH
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"
RUN git clone https://github.com/facebookresearch/detectron2.git
ENV PYTHONPATH=/app

# DensePose einrichten
WORKDIR /app/detectron2/projects/DensePose
RUN pip install . &&\
    wget https://raw.githubusercontent.com/facebookresearch/detectron2/refs/heads/main/projects/DensePose/configs/densepose_rcnn_R_50_FPN_DL_s1x.yaml &&\
    wget https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_DL_s1x/165712097/model_final_0ed407.pkl &&\
    wget https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_DL_s1x/165712097/metrics.json &&\
    wget https://huggingface.co/spaces/pngwn/IDM-VTON/resolve/main/configs/Base-DensePose-RCNN-FPN.yaml &&\
    mkdir cache &&\
    mkdir cache2
COPY exec.py .
ENV LD_LIBRARY_PATH=$CONDA_DIR/envs/detectron/lib:$LD_LIBRARY_PATH


CMD ["python", "exec.py"]
