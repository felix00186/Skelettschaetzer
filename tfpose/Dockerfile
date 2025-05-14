FROM nvidia/cuda:12.0.0-cudnn8-devel-ubuntu20.04

RUN apt-get update && \
    apt-get install -y libglib2.0-0 && \
    apt-get clean &&\
    apt-get install -y wget htop byobu git gcc g++ vim libsm6 libxext6 libxrender-dev lsb-core
RUN cd /root && wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
RUN cd /root && bash Anaconda3-2020.07-Linux-x86_64.sh -b -p ./anaconda3
RUN bash -c "source /root/anaconda3/etc/profile.d/conda.sh && conda install -y pytorch==1.5.0 torchvision cudatoolkit=10.2 -c pytorch"
RUN bash -c "/root/anaconda3/bin/conda init bash"
WORKDIR /root/code
RUN git clone https://github.com/facebookresearch/detectron2.git
RUN bash -c "source /root/anaconda3/etc/profile.d/conda.sh && conda activate base && cd detectron2 && python setup.py build develop"
RUN git clone https://github.com/aim-uofa/AdelaiDet.git adet
WORKDIR adet
RUN bash -c "source /root/anaconda3/etc/profile.d/conda.sh && conda activate base && python setup.py build develop"
RUN rm /root/Anaconda3-2020.07-Linux-x86_64.sh
WORKDIR /root/code
RUN wget https://huggingface.co/tianzhi/AdelaiDet-FCOS/resolve/main/FCOS_R_50_1x.pth?download=true -O fcos_R_50_1x.pth

CMD ["python", "demo/demo.py",\
     "--video-input", "/data/input.mp4",\
     "--config-file", "configs/FCOS-Detection/R_50_1x.yaml",\
     "--output", "/data/tfpose.mp4",\
     "--opts", "MODEL.WEIGHTS", "fcos_R_50_1x.pth"]