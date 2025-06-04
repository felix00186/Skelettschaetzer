exit()
import os


# Schließen, falls input.mp4 existiert
if os.path.exists("/data/input.mp4"):
    exit()

# Ansonsten Link auslesen
if os.path.exists("/data/input.txt"):
    with open("/data/input.txt") as f:
        url = f.read().replace("\n", "").strip()
    import yt_dlp
    ydl_opts = {
        "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
        "outtmpl": "/data/input.mp4",
        "merge_output_format": "mp4",
        "noplaylist": True,
        "quiet": False
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
else:
    raise IOError("Weder ein Video noch ein Download-Link wurde gefunden.")