FROM nvidia/cuda:11.3.1-cudnn8-devel-ubuntu20.04

# Systemabhaengigkeiten installieren
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python3-pip \
        python3-dev \
        git \
        wget \
        ffmpeg \
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
        libomp-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app

# Miniconda installieren
ENV CONDA_DIR=/opt/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -afy
ENV PATH=$CONDA_DIR/bin:$PATH

COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml
ENV CONDA_DEFAULT_ENV=hybrik
ENV PATH=$CONDA_DIR/envs/hybrik/bin:$PATH
ENV FORCE_CUDA="1"
ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=/usr/local/cuda/lib64:/usr/local/cuda/extras/CUPTI/lib64:/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH
ENV PATH=$CUDA_HOME/bin:$PATH
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

RUN git clone --branch v0.7.5 https://github.com/facebookresearch/pytorch3d.git /tmp/pytorch3d
WORKDIR /tmp/pytorch3d
RUN pip install -e . &&\
    git clone https://github.com/Jeff-sjtu/HybrIK.git /app/HybrIK
WORKDIR /app/HybrIK
RUN pip install -e .
WORKDIR /app/HybrIK/model_files/smplx
RUN wget https://huggingface.co/camenduru/SMPLer-X/resolve/main/SMPLX_NEUTRAL.npz &&\
    wget https://huggingface.co/camenduru/SMPLer-X/resolve/main/SMPLX_FEMALE.npz &&\
    wget https://huggingface.co/camenduru/SMPLer-X/resolve/main/SMPLX_MALE.npz
WORKDIR /app/HybrIK/model_files
RUN wget https://huggingface.co/camenduru/buddi/resolve/55f84a18ff09950b4c53365bfd427c24263db875/romp/smplx_kid_template.npy
WORKDIR /app/HybrIK/pretrained_models
COPY hybrikx_rle_hrnet.pth .
WORKDIR /root/.cache/torch/hub/checkpoints
RUN wget https://download.pytorch.org/models/fasterrcnn_resnet50_fpn_coco-258fb6c6.pth
WORKDIR /app/HybrIK

COPY exec.sh .

CMD ["/bin/bash", "exec.sh"]