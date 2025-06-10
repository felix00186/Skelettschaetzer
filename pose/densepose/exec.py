import subprocess
import cv2
import os
import re


INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/densepose"
os.makedirs(OUTPUT_DIR, exist_ok=True)

files = os.listdir(INPUT_DIR)
mp4_files = list(filter(lambda f: f.endswith(".mp4"), files))

for file_name in mp4_files:
    # Caches leeren
    for cache in ["cache", "cache2"]:
        for file in os.listdir(os.path.join("/app", cache)):
            os.remove(os.path.join("/app", cache, file))

    # Video laden und in Einzelbilder unterteilen
    cap = cv2.VideoCapture(os.path.join(INPUT_DIR, file_name))
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join("./cache", f"{frame_count}.jpg")
        cv2.imwrite(frame_filename, frame)
        frame_count += 1
    cap.release()

    # Ausführen der Skelettschaetzung auf den Bildern
    args = [
        "python",
        "apply_net.py",
        "show",
        "densepose_rcnn_R_50_FPN_DL_s1x.yaml",      # config
        "model_final_0ed407.pkl",                   # model
        "cache/*.jpg",                              # input
        "dp_contour,bbox",                          # visualization
        "--output", "cache2/densepose.png",         # output
        "-v"
    ]
    result = subprocess.run(args, capture_output=True, text=True)
    result = result.stdout.split("\n")
    result = [s.split("apply_net]: ")[1] for s in result if re.search("^\[.* apply_net\]: ", s)]
    result = list(filter(lambda s: s.startswith("Processing") or s .startswith("Output saved to"), result))
    images = {}
    for i in range(0, len(result), 2):
        proc_line = result[i]
        try:
            save_line = result[i + 1]
        except IndexError:
            continue
        input_img = re.search("^Processing (.*)$", proc_line).group(1)
        output_img = re.search("^Output saved to (.*)$", save_line).group(1)
        images[input_img] = output_img

    # Bilder zu Video zusammensetzen
    inputs = list(images.keys())
    inputs.sort(key=lambda s: int(s.split("/")[1].split(".")[0]))
    image_paths = [images[input_img] for input_img in inputs]
    first_frame = cv2.imread(image_paths[0])
    height, width, _ = first_frame.shape
    size = (width, height)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # MP4 Codec
    video_writer = cv2.VideoWriter(os.path.join(OUTPUT_DIR, file_name), fourcc, fps, size)
    for idx, img_path in enumerate(image_paths):
        frame = cv2.imread(img_path)
        video_writer.write(frame)
    video_writer.release()