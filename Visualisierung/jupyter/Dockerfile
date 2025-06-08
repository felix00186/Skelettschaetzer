FROM jupyter/base-notebook

USER root
RUN apt update &&\
    apt install -y r-base &&\
    pip install ipywidgets tomli rpy2 &&\
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
USER jovyan
WORKDIR /home/jovyan
COPY notebooks/* .

CMD ["start-notebook.sh",\
     "--NotebookApp.token=''",\
     "--NotebookNotary.checkpoint_dir=/tmp/checkpoints_disabled"]