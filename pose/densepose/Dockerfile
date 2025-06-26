FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
        git \
        ffmpeg \
        libgl1 \
        build-essential &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Detectron2 and DensePose
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN git clone https://github.com/facebookresearch/detectron2 detectron2
RUN pip install -e detectron2
WORKDIR /app/detectron2/projects/DensePose
RUN pip install -e .

WORKDIR /app
COPY exec.py .
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD ["/app/entrypoint.sh"]
