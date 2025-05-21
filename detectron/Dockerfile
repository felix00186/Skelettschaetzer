FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

# Systemabhängigkeiten
RUN apt-get update && apt-get install -y \
    wget git ca-certificates libglib2.0-0 libsm6 libxext6 libxrender-dev \
    build-essential ninja-build python3-opencv libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Miniconda installieren
ENV CONDA_DIR=/opt/conda
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    bash ~/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh && \
    $CONDA_DIR/bin/conda clean -afy
ENV PATH=$CONDA_DIR/bin:$PATH

# environment.yml kopieren und Conda-Umgebung erstellen
COPY environment.yml /app/environment.yml
RUN conda env create -f /app/environment.yml
ENV CONDA_DEFAULT_ENV=detectron
ENV PATH=$CONDA_DIR/envs/detectron/bin:$PATH

# FORCE_CUDA setzen
ENV FORCE_CUDA="1"ENV CUDA_HOME=/usr/local/cuda
ENV LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
ENV PATH=$CUDA_HOME/bin:$PATH
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

# detectron2 klonen & installieren
RUN git clone https://github.com/facebookresearch/detectron2 detectron2 && \
    pip install -e detectron2

# Model Cache-Verzeichnis setzen
ENV FVCORE_CACHE="/tmp"

# Diese Verlinkungen muessen gesetzt werden, damit ein sehr seltsam geschriebener Import aus der demo.py funktioniert.
ENV PYTHONPATH=/app
RUN mkdir -p /app/vision/fair/detectron2/demo && \
    ln -s /app/detectron2/demo/predictor.py /app/vision/fair/detectron2/demo/predictor.py && \
    ln -s /app/detectron2/demo/demo.py /app/vision/fair/detectron2/demo/demo.py

WORKDIR /app/detectron2

# Standardbefehl
CMD ["python", "demo/demo.py", \
     "--config-file", "configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml", \
     "--video-input", "/data/input.mp4", \
     "--output", "/data/detectron.mp4", \
     "--opts", "MODEL.WEIGHTS", "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"]