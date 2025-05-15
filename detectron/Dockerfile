FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04
# use an older system (18.04) to avoid opencv incompatibility (issue#3524)

WORKDIR /app
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get install -y \
	python3-opencv ca-certificates python3-dev python3-pip git wget ninja-build
RUN ln -sv /usr/bin/python3 /usr/bin/python

# install dependencies
# See https://pytorch.org/ for other options if you use a different version of CUDA
RUN pip3 install --no-cache-dir --upgrade pip setuptools wheel scikit-build
RUN pip3 install cmake
RUN pip3 install --no-cache-dir protobuf==3.19.6
RUN pip3 install tensorboard onnx
RUN pip3 install torch==1.10 torchvision==0.11.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html

RUN pip3 install 'git+https://github.com/facebookresearch/fvcore'
# install detectron2
RUN git clone https://github.com/facebookresearch/detectron2 detectron2_repo
# set FORCE_CUDA because during `docker build` cuda is not accessible
ENV FORCE_CUDA="1"
# This will by default build detectron2 for all common cuda architectures and take a lot more time,
# because inside `docker build`, there is no way to tell which architecture will be used.
ARG TORCH_CUDA_ARCH_LIST="Kepler;Kepler+Tesla;Maxwell;Maxwell+Tegra;Pascal;Volta;Turing"
ENV TORCH_CUDA_ARCH_LIST="${TORCH_CUDA_ARCH_LIST}"

RUN pip3 install -e detectron2_repo

# Set a fixed model cache directory.
ENV FVCORE_CACHE="/tmp"
WORKDIR /app/detectron2_repo

# run detectron2 under user "appuser":
CMD ["python3", "demo/demo.py",  \
	 "--config-file", "configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml", \
	 "--video-input", "/data/input.mp4", \
	 "--output", "/data/detectron.mp4", \
	 "--opts", "MODEL.WEIGHTS", "detectron2://COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x/137849600/model_final_f10217.pkl"]