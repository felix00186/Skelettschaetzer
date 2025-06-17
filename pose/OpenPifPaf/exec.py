import os
import glob
import openpifpaf
from openpifpaf import show
import cv2
import numpy
from PIL import Image
import io
import matplotlib.pyplot as plt


# Ordner mit Videos
VIDEO_DIR = '/data/input'
OUTPUT_DIR = '/data/OpenPifPaf'

# Modell-Checkpoint
CHECKPOINT = os.environ['CHECKPOINT']


def process_video(video_path, predictor, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    video_name = os.path.splitext(os.path.basename(video_path))[0]
    output_path = os.path.join(output_dir, f"{video_name}_annotated.mp4")

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    frame_index = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        predictions, _, _ = predictor.numpy_image(frame)

        # Annotiertes Bild als PIL aus dem Canvas holen
        buf = io.BytesIO()
        painter = show.annotation_painter.AnnotationPainter()

        with show.Canvas.image(frame) as ax:
            painter.annotations(painter, ax, predictions)

            fig = ax.get_figure()
            fig.savefig(buf, format='png', bbox_inches='tight', pad_inches=0)
            plt.close(fig)

        buf.seek(0)
        annotated_pil = Image.open(buf).convert("RGB")
        annotated_frame = cv2.cvtColor(numpy.array(annotated_pil), cv2.COLOR_RGB2BGR)

        # Resize auf Originalgröße (Canvas kann leicht abweichen)
        annotated_frame = cv2.resize(annotated_frame, (width, height))

        writer.write(annotated_frame)
        frame_index += 1

    cap.release()
    writer.release()
    print(f"Video gespeichert unter: {output_path}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Predictor initialisieren
    predictor = openpifpaf.Predictor(checkpoint=CHECKPOINT)

    video_files = glob.glob(os.path.join(VIDEO_DIR, '*.mp4'))  # Alle .mp4 im Ordner

    for video_path in video_files:
        print(f'Starte Verarbeitung: {video_path}')
        process_video(video_path, predictor, OUTPUT_DIR)


if __name__ == '__main__':
    main()
