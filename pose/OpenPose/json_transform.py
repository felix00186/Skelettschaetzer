import json
import os
import numpy
import sys


width = float(sys.argv[1])
height = float(sys.argv[2])
dimensions = [width, height, 1]
axes = ["x", "y", "z"]

with open("./joint_names.json", "r") as f:
    JOINT_NAMES = json.load(f)

output_dir = "/data/openpose"
file_name = sys.argv[3]
input_dir = os.path.join("/cache", file_name)
files = os.listdir(input_dir)
files.sort()
output = []
for file in files:
    with open(os.path.join(input_dir, file), "r") as f:
        frame_raw_data = json.load(f)
    frame_data = []
    for person in frame_raw_data["people"]:
        keypoints = numpy.array(person["pose_keypoints_2d"]).reshape((-1, 3))
        person_data = {}
        for joint_nr, point in enumerate(keypoints):
            if (point==0).all():
                continue
            joint_name = JOINT_NAMES[joint_nr]
            person_data[joint_name] = {axes[i]: point[i]/dimensions[i] for i in range(3)}
        frame_data.append(person_data)
    output.append(frame_data)
with open(os.path.join(output_dir, f"{file_name}.json"), "w") as f:
    json.dump(output, f)
