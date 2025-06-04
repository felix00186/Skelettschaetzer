FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu20.04

# Systemabhaengigkeiten installieren
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
        python3-pip=20.0.2-5ubuntu1.11 \
        python3-dev=3.8.2-0ubuntu2 \
        git \
        wget \
        ffmpeg=7:4.2.7-0ubuntu0.1 \
        libsm6=2:1.2.3-1 \
        libxext6=2:1.3.4-0ubuntu1 \
        libxrender-dev=1:0.9.10-1 \
        cmake \
        libglib2.0-0=2.64.6-1~ubuntu20.04.9 \
        libgtk2.0-dev=2.24.32-4ubuntu4.1 \
        pkg-config=0.29.1-0ubuntu4 \
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
    cd tfpose/tf_pose/pafprocess && \
    swig -python -c++ pafprocess.i && \
    python3 setup.py build_ext --inplace

# Modell laden
WORKDIR /app/tfpose
COPY run_video.py .
COPY graph_opt.pb /app/tfpose/models/graph/cmu/graph_opt.pb


CMD ["python3", "run_video.py",\
     "--video", "/data/input",\
     "--show-process", "SHOW_PROCESS",\
     "--output", "/data/tfpose"]
