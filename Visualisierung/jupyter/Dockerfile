FROM jupyter/base-notebook

USER root
RUN apt update &&\
    apt install -y r-base &&\
    pip install ipywidgets tomli rpy2 &&\
    jupyter labextension install @jupyter-widgets/jupyterlab-manager
WORKDIR /home/jovyan
COPY notebooks/* ./work
COPY entrypoint.sh .
RUN chmod -R 777 /home/jovyan/work

CMD ["bash", "entrypoint.sh"]