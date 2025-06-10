import cv2
import mediapipe as mp
import os
import json


mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils
INPUT_DIR = "/data/input"
OUTPUT_DIR = "/data/blazepose"
os.makedirs(OUTPUT_DIR, exist_ok=True)

with open("./joint_names.json", "r") as f:
    joint_names = json.load(f)

# Iteriere durch Videos
files = os.listdir(INPUT_DIR)
mp4_files = list(filter(lambda f: f.endswith(".mp4"), files))

for video_path in mp4_files:
    cap = cv2.VideoCapture(os.path.join(INPUT_DIR, video_path))

    # Hole Video-Informationen
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    out = cv2.VideoWriter(os.path.join(OUTPUT_DIR, video_path), cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    data = []

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    for frame_number in range(total_frames):
        success, frame = cap.read()
        if not success:
            data.append([])
            continue

        # Konvertiere das Bild zu RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Pose-Erkennung
        results = pose.process(image)

        # Zurück zu BGR für OpenCV
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.pose_landmarks:
            # Skelett zeichnen
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

            # strukturierte Daten ausgeben
            data.append([{
                joint_names[i]:
                {
                    "x": lm.x * width,
                    "y": lm.y * height,
                    "z": lm.z,
                    "score": lm.visibility,
                }
                for i, lm in enumerate(results.pose_landmarks.landmark)
            }])

        else:
            data.append([])

        # Schreibe Frame ins Ausgabefile
        out.write(image)

    # Ressourcen freigeben
    cap.release()
    out.release()
    print(f"Video verarbeitet: {video_path}")

    with open(os.path.join(OUTPUT_DIR, video_path.replace(".mp4", ".json")), "w") as f:
        json.dump(data, f)
