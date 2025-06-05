import os


INPUT_DIR = "/data/input"

# Ansonsten Link auslesen
if os.path.exists(os.path.join(INPUT_DIR, "input.txt")):
    with open(os.path.join(INPUT_DIR, "input.txt")) as f:
        urls = [line.replace("\n", "").strip() for line in f.readlines()]
    import yt_dlp
    for i, url in enumerate(urls):
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4",
            "outtmpl": f"{INPUT_DIR}/input_{i}.mp4",
            "merge_output_format": "mp4",
            "noplaylist": True,
            "quiet": False
        }
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            print(f"URL: {url}, gescheitert!")


files = os.listdir(INPUT_DIR)
mp4_files = list(filter(lambda f: f.endswith(".mp4"), files))
if len(mp4_files) == 0:
    raise IOError("No mp4 files found.")