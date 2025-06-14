# IPR
**Integral Human Pose Regression** verbindet Heatmap-basierte Schätzung mit direkter Koordinatenregression – mithilfe einer einfachen, aber effektiven Integrationsoperation („taking-expectation“) über die Wahrscheinlichkeitsverteilung der Heatmap. Dadurch wird das nicht-differenzierbare Argmax ersetzt, was den gesamten Prozess end-to-end trainierbar macht und Quantisierungsfehler verringert. Diese Methode ist leichtgewichtig (parameterfrei), universell einsetzbar mit bestehenden Heatmap-Modellen und verbessert nachweislich die Leistung sowohl bei 2D- (MPII, COCO) als auch bei 3D-Pose-(Human3.6M)-Schätzungen.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/1711.08229
```bibtex
@inproceedings{sun2018integral,
  title={Integral human pose regression},
  author={Sun, Xiao and Xiao, Bin and Wei, Fangyin and Liang, Shuang and Wei, Yichen},
  booktitle={Proceedings of the European conference on computer vision (ECCV)},
  pages={529--545},
  year={2018}
}
```

IPR wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git