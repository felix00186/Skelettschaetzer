FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

# Systemabhängigkeiten
RUN apt-get update && apt-get install -y \
    wget \
    git \
    ca-certificates \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    build-essential \
    ninja-build \
    libgl1 \
    python3-distutils \
    pkg-config && \
    rm -rf /var/lib/apt/lists/*

# Miniconda installieren
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
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
RUN git clone https://github.com/facebookresearch/detectron2 detectron2 && \
    pip install -e detectron2 #&& \
    #pip install av --no-binary :all:
ENV FVCORE_CACHE="/tmp"
ENV PYTHONPATH=/app
RUN mkdir -p /app/vision/fair/detectron2/demo && \
    ln -s /app/detectron2/demo/predictor.py /app/vision/fair/detectron2/demo/predictor.py && \
    ln -s /app/detectron2/demo/demo.py /app/vision/fair/detectron2/demo/demo.py

# DensePose einrichten
ENV LD_LIBRARY_PATH=$CONDA_DIR/envs/detectron/lib:$LD_LIBRARY_PATH
WORKDIR /app/detectron2/projects/DensePose
RUN wget --quiet https://raw.githubusercontent.com/dajes/DensePose-TorchScript/refs/heads/main/configs/Base-DensePose-RCNN-FPN.yaml && \
    wget --quiet https://huggingface.co/spaces/pngwn/IDM-VTON/resolve/4dbb2636fc5ab6149dbdaec6561706e1b8309402/configs/densepose_rcnn_R_50_FPN_s1x.yaml && \
    wget --quiet https://dl.fbaipublicfiles.com/densepose/densepose_rcnn_R_50_FPN_s1x_legacy/164832157/model_final_d366fa.pkl -O weights.pkl
CMD ["python", "train_net.py", \
     "--config-file", "densepose_rcnn_R_50_FPN_s1x.yaml", \
     "MODEL.WEIGHTS", "weights.pkl", \
     "OUTPUT_DIR", "."]

#CMD ["python", "demo/demo.py", \
#     "--config-file", "densepose_rcnn_R_50_FPN_s1x.yaml", \
#     "--video-input", "/data/input.mp4", \
#     "--output", "/data/densepose.mp4"]
