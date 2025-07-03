import cv2
import os
import inference


INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/EfficientPose"
os.makedirs(OUTPUT_DIR, exist_ok=True)
files = os.listdir(INPUT_DIR)
mp4_files = list(filter(lambda f: f.endswith(".mp4"), files))

def video_to_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    frame_number = 0

    while True:
        success, frame = cap.read()
        if not success:
            break

        filename = f"{frame_number:05d}.png"
        filepath = os.path.join(output_folder, filename)
        cv2.imwrite(filepath, frame)

        frame_number += 1
        if frame_number % 100 == 0:
            print(f"{frame_number} Frames gespeichert...")

    cap.release()
    print(f"Fertig. {frame_number} Frames gespeichert in: {output_folder}")


def frames_to_video(bilder_pfade, ausgabe_datei, fps=30):
    if not bilder_pfade:
        raise ValueError("Die Liste der Bilder ist leer.")

    # Bildgröße automatisch aus dem ersten Bild bestimmen
    erstes_bild = cv2.imread(bilder_pfade[0])
    if erstes_bild is None:
        raise ValueError(f"Bild konnte nicht geladen werden: {bilder_pfade[0]}")
    hoehe, breite, _ = erstes_bild.shape

    # VideoWriter initialisieren
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(ausgabe_datei, fourcc, fps, (breite, hoehe))

    for pfad in bilder_pfade:
        bild = cv2.imread(pfad)
        if bild is None:
            print(f"WARNUNG: Bild konnte nicht geladen werden: {pfad}")
            continue
        if bild.shape[:2] != (hoehe, breite):
            bild = cv2.resize(bild, (breite, hoehe))
        video_writer.write(bild)

    video_writer.release()
    print(f"Video gespeichert unter: {os.path.abspath(ausgabe_datei)}")


for file_name in mp4_files:
    # Caches leeren
    for cache in ["/cache_input", "/cache_output"]:
        for file in os.listdir(cache):
            os.remove(os.path.join(cache, file))
    video_to_frames(os.path.join(INPUT_DIR, file_name), "/cache_input")
    inference.main()
    pathes = os.listdir("/cache_output")
    pathes.sort()
    pathes = [os.path.join("/cache_output", f) for f in pathes]
    frames_to_video(pathes, os.path.join(OUTPUT_DIR, file_name))
