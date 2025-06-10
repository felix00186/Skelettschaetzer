chmod -R a+rx /home/jovyan/data
start-notebook.sh --NotebookApp.token='' --NotebookNotary.checkpoint_dir=/tmp/checkpoints_disabled --NotebookApp.notebook_dir=/home/jovyan
