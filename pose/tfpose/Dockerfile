FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04

# Systemabhaengigkeiten installieren
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python3-pip=9.0.1-2.3~ubuntu1.18.04.8 \
        python3-dev=3.6.7-1~18.04 \
        git \
        wget \
        ffmpeg=7:3.4.11-0ubuntu0.1 \
        libsm6=2:1.2.2-1 \
        libxext6=2:1.3.3-1 \
        libxrender-dev=1:0.9.10-1 \
        cmake=3.10.2-1ubuntu2.18.04.2 \
        libglib2.0-0=2.56.4-0ubuntu0.18.04.9 \
        libgtk2.0-dev=2.24.32-1ubuntu1 \
        pkg-config=0.29.1-0ubuntu2 \
        swig && \
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
    cd tfpose/tf_pose/pafprocess && \
    swig -python -c++ pafprocess.i && \
    python3 setup.py build_ext --inplace

# Modell laden
WORKDIR /app/tfpose
COPY exec.py .
COPY graph_opt.pb /app/tfpose/models/graph/cmu/graph_opt.pb
COPY joint_names.json .


CMD ["python3", "exec.py",\
     "--video", "/data/input",\
     "--show-process", "SHOW_PROCESS",\
     "--output", "/data/tfpose"]
