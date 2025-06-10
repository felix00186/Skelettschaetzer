FROM python:3.11-slim

WORKDIR /app

# Installiere notwendige Pakete
COPY requirements.txt .
RUN apt-get update &&\
    apt-get install -y  \
        ffmpeg=7:5.1.6-0+deb12u1 \
        libsm6=2:1.2.3-1 \
        libxext6=2:1.3.4-1+b1 &&\
    pip install -r requirements.txt

# Kopiere das Python-Skript
COPY exec.py .
COPY joint_names.json .

# Starte das Skript beim Containerstart
CMD ["python", "exec.py"]