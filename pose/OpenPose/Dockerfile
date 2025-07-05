FROM nvidia/cuda:11.1.1-cudnn8-devel-ubuntu18.04


ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update &&\
    apt-get install -y --no-install-recommends \
        python3-dev \
        python3-pip \
        python3-setuptools \
        git \
        g++ \
        wget \
        make \
        libprotobuf-dev \
        protobuf-compiler \
        libopencv-dev \
        libgoogle-glog-dev \
        libboost-all-dev \
        libcaffe-cuda-dev \
        libhdf5-dev \
        libatlas-base-dev \
        ffmpeg &&\
    pip3 install --upgrade pip &&\
    pip3 install numpy opencv-python &&\
    wget https://github.com/Kitware/CMake/releases/download/v3.16.0/cmake-3.16.0-Linux-x86_64.tar.gz && \
    tar xzf cmake-3.16.0-Linux-x86_64.tar.gz -C /opt && \
    rm cmake-3.16.0-Linux-x86_64.tar.gz
ENV PATH="/opt/cmake-3.16.0-Linux-x86_64/bin:${PATH}"
WORKDIR /openpose
RUN git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git .
WORKDIR /openpose/build
RUN cmake -DBUILD_PYTHON=ON .. &&\
    make -j `nproc`
WORKDIR /openpose/models
RUN ./getModels.sh
WORKDIR /openpose
COPY exec.sh .
COPY joint_names.json .
COPY json_transform.py .


CMD ["/bin/bash", "exec.sh"]
