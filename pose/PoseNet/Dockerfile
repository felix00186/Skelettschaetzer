FROM node:18-slim

RUN apt-get update &&\
    apt-get install -y ffmpeg python3 &&\
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY package.json .
RUN npm install
COPY process.js .
COPY ffmpeg-wrapper.js .
COPY exec.sh .
RUN chmod +x exec.sh

CMD ["/bin/bash", "exec.sh"]
