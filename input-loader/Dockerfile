FROM python:3.11-slim


RUN apt-get update && apt-get install -y ffmpeg curl bc &&\
    rm -rf /var/lib/apt/lists/* &&\
    pip install --no-cache-dir yt-dlp
WORKDIR /app
COPY exec.py .
COPY exec.sh .

# Standardbefehl: Hilfe anzeigen
CMD ["/bin/bash", "exec.sh"]
