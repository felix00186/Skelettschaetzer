FROM jupyter/base-notebook

USER root
RUN apt update &&\
    apt install -y r-base &&\
    pip install ipywidgets tomli rpy2 pandas &&\
    jupyter labextension install @jupyter-widgets/jupyterlab-manager &&\
    Rscript -e "install.packages('tidyverse')"
WORKDIR /home/jovyan
COPY notebooks/* ./work
COPY entrypoint.sh .
RUN mkdir /home/jovyan/work/cache &&\
    chmod -R 777 /home/jovyan/work


CMD ["bash", "entrypoint.sh"]