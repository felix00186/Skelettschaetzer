import json
import os

data_folder = "/srv/docker/skelettschaetzer/data"
subdirs = [os.path.join(data_folder, dir) for dir in os.listdir(data_folder) if dir != "input"]
subdirs = list(filter(lambda dir: len(list(filter(lambda f: f.endswith(".json"), os.listdir(dir)))) > 0, subdirs))

with open("./joint_list.json", "r") as f:
    JOINT_LIST = json.load(f)

# verarbeitete Daten finden
json_files = set(list(filter(lambda f: f.endswith(".json"), os.listdir(subdirs[0]))))
for subdir in subdirs[1:]:
    json_files &= set(list(filter(lambda f: f.endswith(".json"), os.listdir(subdir))))
json_files = list(json_files)

global_frame_counter = 0
global_data = []
for json_file in json_files:
    frame_count = None
    for subdir in subdirs:
        poser_name = subdir.split("/")[-1]
        with open(os.path.join(subdir, json_file), "r") as f:
            video_raw_data = json.load(f)
        # Prüfen, ob die Anzahl der Frames überall gleich ist
        if frame_count is None:
            frame_count_comparer = poser_name
            frame_count = len(video_raw_data)
            global_data += [{} for _ in range(frame_count)]
        else:
            assert frame_count == len(video_raw_data), f"Die Ausgaben haben unterschiedliche Anzahlen von Frames. -> Video {json_file.replace('.json', '.mp4')} ({frame_count_comparer}={frame_count}, {poser_name}={len(video_raw_data)})"
        print(f"Skelettschätzer {poser_name}, Video {json_file.replace('.json', '.mp4')} erfolgreich eingelesen")
        # Iterieren durch die Frames
        for local_frame_counter in range(frame_count):
            frame_data = global_data[global_frame_counter + local_frame_counter]
            frame_raw_data = video_raw_data[local_frame_counter]
            frame_data["META_VIDEO_FILE"] = json_file.replace(".json", ".mp4")
            frame_data[f"PERSONCOUNT_{poser_name}"] = len(frame_raw_data)
    global_frame_counter += frame_count

for line in json.dumps(global_data, indent=2).split("\n"):
    print(line)