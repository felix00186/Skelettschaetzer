import json
import os
import sys
import numpy


width = float(sys.argv[1])
height = float(sys.argv[2])
path = sys.argv[3]
dimensions = [width, height, 1]
axes = ["x", "y", "z"]

with open("./joint_names.json", "r") as f:
    JOINT_NAMES = json.load(f)

with open(path, "r") as f:
    raw_data = f.readlines()
raw_data = [json.loads(line.replace("\n", ""))["predictions"] for line in raw_data]
output = []
for frame_raw_data in raw_data:
    frame_data = []
    for person_raw_data in frame_raw_data:
        keypoints = numpy.array(person_raw_data["keypoints"]).reshape((-1, 3))
        person_data = {}
        for joint_nr, point in enumerate(keypoints):
            if (point==0).all():
                continue
            person_data[JOINT_NAMES[joint_nr]] = {axes[i]: point[i]/dimensions[i] for i in range(3)}
        frame_data.append(person_data)
    output.append(frame_data)

file_name = path.split("/")[-1].replace(".mp4.json", ".json")
with open(os.path.join("/data/OpenPifPaf", file_name), "w") as f:
    json.dump(output, f)
