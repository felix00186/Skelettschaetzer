# HybrIK
HybrIK ist ein Modell zur 3D-Pose-Schätzung, das inverse Kinematik mit Deep Learning kombiniert. Es schätzt nicht direkt die 3D-Pose, sondern optimiert sie in einem differentiellen IK-Framework, sodass die Gelenkpositionen konsistent zum geschätzten 2D-Output bleiben. Dabei wird der SMPL-Body-Model-Parameterraum genutzt, um plausible menschliche Posen mit physikalischen Einschränkungen zu rekonstruieren. HybrIK wurde so konzipiert, dass es sowohl präzise als auch anatomisch sinnvolle Posen liefert – insbesondere bei selbstverdeckten Körperteilen.

<img height="400px" src="demo.gif">

## Installation
Bitte laden Sie diese Datei von Google Drive herunter und legen Sie sie in dieses Verzeichnis.

https://drive.usercontent.google.com/download?id=1R0WbySXs_vceygKg_oWeLMNAZCEoCadG&export=download&authuser=0

## Quellen
Die Software wurde auf diesem Repository aufgebaut:

https://github.com/jeffffffli/HybrIK.git

Zitiert werden kann folgendermaßen:

```bibtex
@inproceedings{li2021hybrik,
    title={Hybrik: A hybrid analytical-neural inverse kinematics solution for 3d human pose and shape estimation},
    author={Li, Jiefeng and Xu, Chao and Chen, Zhicun and Bian, Siyuan and Yang, Lixin and Lu, Cewu},
    booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
    pages={3383--3393},
    year={2021}
}

@article{li2023hybrik,
    title={HybrIK-X: Hybrid Analytical-Neural Inverse Kinematics for Whole-body Mesh Recovery},
    author={Li, Jiefeng and Bian, Siyuan and Xu, Chao and Chen, Zhicun and Yang, Lixin and Lu, Cewu},
    journal={arXiv preprint arXiv:2304.05690},
    year={2023}
}
```