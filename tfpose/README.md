# TfPose
Dies ist ein Skelettschätzer, der auf TensorFlow (Tf) und OpenPose aufbaut.

## Installation
Sie müssen zunächst die Datei unter dem Link https://www.mediafire.com/file/qlzzr20mpocnpa3/graph_opt.pb herunterladen
und in diesem Verzeichnis ablegen.

## Quelle
Genutzt wird das Git-Repository https://github.com/jiajunhua/ildoonet-tf-pose-estimation.git

Die `run_video.py` aus diesem Verzeichnis baut auf der gleichnamigen Datei im Repository auf.
Geändert wurde, dass das erstellte Video nicht auf einer GUI angezeigt, sondern in einem selbst gewählten Ordner
gespeichert wird.

Die Sekundärquellen können unter dem folgenden Link eingesehen werden: https://github.com/jiajunhua/ildoonet-tf-pose-estimation/blob/master/etcs/reference.md

TfPose baut auf OpenPose auf. Auf dieses kann folgendermaßen verwiesen werden:
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