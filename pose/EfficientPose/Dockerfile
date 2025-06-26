FROM tensorflow/tensorflow:1.15.0-gpu-py3

WORKDIR /app
RUN rm /etc/apt/sources.list.d/cuda.list &&\
    rm /etc/apt/sources.list.d/nvidia-ml.list &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub &&\
    apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub &&\
    apt-get update &&\
    apt-get install -y git\
                       libsm6 \
                       libxext6 \
                       libxrender1 &&\
    git clone https://github.com/ybkscht/EfficientPose.git
WORKDIR /app/EfficientPose
RUN git checkout 64b71190df7ecbdfaa8f34a24c1ed6c4c67693ef &&\
    pip install -r requirements.txt &&\
    python setup.py build_ext --inplace &&\
    pip install opencv-python &&\
    mkdir /cache_input &&\
    mkdir /cache_output &&\
    sed -i "s,/Datasets/Linemod_preprocessed/data/02/rgb/,/cache_input,g" inference.py &&\
    sed -i "s,./predictions/occlusion/,/cache_output,g" inference.py &&\
    mkdir weights


COPY exec.py .
COPY "phi_0_occlusion_best_ADD(-S).h5" "weights/phi_0_occlusion_best_ADD(-S).h5"
CMD ["python", "exec.py"]
