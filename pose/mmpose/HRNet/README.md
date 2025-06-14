# HRNet
**High‑Resolution Network (HRNet)** erhält während des gesamten Prozesses gleichbleibend fein aufgelöste Merkmalsrepräsentationen, anstatt erst niedrig aufgelöste Features hochzuskalieren. Dabei werden mehrere parallel verlaufende Subnetze mit unterschiedlichen Auflösungen kombiniert und regelmäßig mittels Multi‑Scale‑Fusion Informationen ausgetauscht – das verbessert sowohl die semantische Tiefe als auch die räumliche Genauigkeit der Keypoint‑Heatmaps. HRNet erreicht dadurch deutlich bessere Ergebnisse auf Standard‑Datensätzen wie COCO und MPII und zeigt auch im Pose‑Tracking (z. B. PoseTrack) starke Leistungen.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://openaccess.thecvf.com/content_CVPR_2019/papers/Sun_Deep_High-Resolution_Representation_Learning_for_Human_Pose_Estimation_CVPR_2019_paper.pdf
```bibtex
@inproceedings{sun2019deep,
  title={Deep high-resolution representation learning for human pose estimation},
  author={Sun, Ke and Xiao, Bin and Liu, Dong and Wang, Jingdong},
  booktitle={Proceedings of the IEEE conference on computer vision and pattern recognition},
  pages={5693--5703},
  year={2019}
}
```

HRNet wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git