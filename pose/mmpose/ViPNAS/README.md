# ViPNAS
**ViPNAS** ist eine Methode zur automatischen Netzwerksuche, die sowohl räumliche als auch zeitliche Aspekte für schnelle Online-Video-Pose-Schätzung optimiert. Dabei wird im räumlichen Bereich die Architektur in fünf Dimensionen wie Tiefe, Breite und Aufmerksamkeitssysteme durchsucht, während im zeitlichen Bereich verschiedene Feature-Fusionsstrategien evaluiert werden. So entstehen Modelle, die auf COCO2017 und PoseTrack2018 eine deutlich höhere Geschwindigkeit bei nahezu gleicher Genauigkeit erreichen und damit besonders für Echtzeitanwendungen geeignet sind.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/2105.10154
```bibtex
@article{xu2021vipnas,
  title={ViPNAS: Efficient Video Pose Estimation via Neural Architecture Search},
  author={Xu, Lumin and Guan, Yingda and Jin, Sheng and Liu, Wentao and Qian, Chen and Luo, Ping and Ouyang, Wanli and Wang, Xiaogang},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  year={2021}
}
```

ViPNAS wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git