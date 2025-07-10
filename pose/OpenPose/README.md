# OpenPose
OpenPose ist eine Open-Source-Software, die Echtzeit-2D- und 3D-Pose-Estimation für einzelne Personen und Gruppen ermöglicht. Sie wurde an der Carnegie Mellon University entwickelt und kann neben Ganzkörperposen auch Hände und Gesichtspunkte erkennen. OpenPose ist bekannt für seine flexible Pipeline und breite Hardware-Unterstützung.

<img src="demo.gif" height="400px">

## Quellen
Die Software entstammt diesem Repository:
https://github.com/CMU-Perceptual-Computing-Lab/openpose.git

Der Bau des Docker-Images ist inspiriert durch dieses Repository:
https://github.com/hmurari/openpose-docker.git

Zitiert werden kann folgendermaßen:
```bibtex
@article{8765346,
  author = {Z. {Cao} and G. {Hidalgo Martinez} and T. {Simon} and S. {Wei} and Y. A. {Sheikh}},
  journal = {IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title = {OpenPose: Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2019}
}

@inproceedings{simon2017hand,
  author = {Tomas Simon and Hanbyul Joo and Iain Matthews and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Hand Keypoint Detection in Single Images using Multiview Bootstrapping},
  year = {2017}
}

@inproceedings{cao2017realtime,
  author = {Zhe Cao and Tomas Simon and Shih-En Wei and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
  year = {2017}
}

@inproceedings{wei2016cpm,
  author = {Shih-En Wei and Varun Ramakrishna and Takeo Kanade and Yaser Sheikh},
  booktitle = {CVPR},
  title = {Convolutional pose machines},
  year = {2016}
}
```