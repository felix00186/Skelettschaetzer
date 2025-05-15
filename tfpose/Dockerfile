FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu20.04

# Systempakete installieren
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin
RUN apt-get update && apt-get install -y \
    git build-essential cmake wget unzip \
    ninja-build gcc g++ curl libglib2.0-0 libsm6 libxext6 libxrender-dev

# Miniconda
ENV CONDA_DIR /opt/conda
RUN curl -sLo ~/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -ya
ENV PATH=$CONDA_DIR/bin:$PATH

# Conda Env
RUN conda create -y -n detectron python=3.7
SHELL ["conda", "run", "-n", "detectron", "/bin/bash", "-c"]

# PyTorch 1.8.1 + torchvision 0.9.1 (für CUDA 11.1)
RUN conda install -y pytorch==1.8.1 torchvision==0.9.1 cudatoolkit=11.1 -c pytorch -c nvidia
RUN pip install cython pyyaml matplotlib ninja opencv-python

# fvcore passend zur Detectron2-Version
RUN pip install 'git+https://github.com/facebookresearch/fvcore'

# Detectron2 v0.3
RUN pip install cython && \
    git clone https://github.com/cocodataset/cocoapi.git && \
    cd cocoapi/PythonAPI && python setup.py build_ext install && \
    git clone https://github.com/facebookresearch/detectron2.git && \
    cd detectron2 && git checkout v0.3 && python setup.py build develop

# AdelaiDet installieren
RUN git clone https://github.com/aim-uofa/adet.git &&\
    cd adet &&\
    python setup.py build develop

# Pretrained Modell herunterladen
RUN wget https://huggingface.co/tianzhi/AdelaiDet-FCOS/resolve/main/FCOS_R_50_1x.pth?download=true -O fcos_R_50_1x.pth

# Arbeitsverzeichnis wechseln
WORKDIR /root/code/adet

# Kommando setzen
CMD ["/bin/bash", "-c", "source activate detectron && python demo/demo.py \
    --video-input /data/input.mp4 \
    --config-file configs/FCOS-Detection/R_50_1x.yaml \
    --output /data/tfpose.mp4 \
    --opts MODEL.WEIGHTS fcos_R_50_1x.pth"]
