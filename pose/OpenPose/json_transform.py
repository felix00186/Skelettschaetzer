import json
import os
import numpy


with open("./joint_names.json", "r") as f:
    JOINT_NAMES = json.load(f)

INPUT_DIR = "/cache"
OUTPUT_DIR = "/data/openpose"
subdirs = [d for d in os.listdir(INPUT_DIR) if os.path.isdir(os.path.join(INPUT_DIR, d))]
for subdir in subdirs:
    files = os.listdir(os.path.join(INPUT_DIR, subdir))
    files.sort()
    output = []
    for file in files:
        with open(os.path.join(INPUT_DIR, subdir, file), "r") as f:
            frame_raw_data = json.load(f)
        frame_data = []
        for person in frame_raw_data["people"]:
            keypoints = numpy.array(person["pose_keypoints_2d"]).reshape((-1, 3))
            person_data = {}
            for joint_nr, point in enumerate(keypoints):
                if (point==0).all():
                    continue
                joint_name = JOINT_NAMES[joint_nr]
                person_data[joint_name] = {["x", "y", "z"][i]: point[i] for i in range(3)}
            frame_data.append(person_data)
        output.append(frame_data)
    with open(os.path.join(OUTPUT_DIR, f"{subdir}.json"), "w") as f:
        json.dump(output, f)
