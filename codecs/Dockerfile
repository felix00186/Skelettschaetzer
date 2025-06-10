FROM debian:bullseye-slim


RUN apt-get update && \
    apt-get install -y ffmpeg findutils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY exec.sh .
RUN chmod +x exec.sh

CMD ["./exec.sh"]
