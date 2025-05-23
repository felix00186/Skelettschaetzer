# Basis: NVIDIA CUDA Ubuntu Image
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

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
        libxrender-dev \
        cmake \
        libglib2.0-0 \
        libgtk2.0-dev \
        pkg-config \
        swig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    ln -s /usr/bin/python3 /usr/bin/python
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
ENV CONDA_DEFAULT_ENV=tf_pose
ENV PATH=$CONDA_DIR/envs/tf_pose/bin:$PATH
ENV FORCE_CUDA="1"
ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV PATH=$CUDA_HOME/bin:$PATH
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

# TfPose von GitHub klonen
RUN git clone https://github.com/jiajunhua/ildoonet-tf-pose-estimation.git tfpose && \
    cd tfpose && \
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt && \
    cd tf_pose/pafprocess && \
    swig -python -c++ pafprocess.i && \
    python3 setup.py build_ext --inplace

# Modell laden
WORKDIR /app/tfpose
COPY run_video.py .
COPY graph_opt.pb /app/tfpose/models/graph/cmu/graph_opt.pb


ENTRYPOINT ["python3", "run_video.py",\
            "--video", "/data/input.mp4",\
            "--show-process", "SHOW_PROCESS",\
            "--output", "/data/tfpose.mp4"]
