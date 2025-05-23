import subprocess
import cv2
import os
import re

# Zerlegen des Videos in einzelne Bilder
cap = cv2.VideoCapture("/data/input.mp4")
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
    save_line = result[i + 1]
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
video_writer = cv2.VideoWriter("/data/densepose.mp4", fourcc, fps, size)
for idx, img_path in enumerate(image_paths):
    frame = cv2.imread(img_path)
    video_writer.write(frame)
video_writer.release()