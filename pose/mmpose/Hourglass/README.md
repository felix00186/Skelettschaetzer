# Hourglass
**Stacked Hourglass Network** ist eine mehrstufige Faltungsarchitektur für die 2D-Pose-Schätzung, die Merkmale in symmetrischer Weise über mehrere Skalen hinweg (Pooling gefolgt von Upsampling) verarbeitet. Durch das Aneinanderhängen mehrerer solcher „Hourglass“-Module und Anwendung von Zwischenüberwachung (intermediate supervision) gelingt eine wiederholte Bottom‑Up–Top‑Down-Verarbeitung, die sowohl globales als auch lokales Kontextwissen konsolidiert. Dieses Vorgehen führte zu einer deutlichen Verbesserung der Genauigkeit auf gängigen Datensätzen wie FLIC und MPII – mit bis zu +2 % im Durchschnitt und +4–5 % bei schwierigen Gelenken wie Knie und Knöchel.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://link.springer.com/chapter/10.1007/978-3-319-46484-8_29
```bibtex
@inproceedings{newell2016stacked,
  title={Stacked hourglass networks for human pose estimation},
  author={Newell, Alejandro and Yang, Kaiyu and Deng, Jia},
  booktitle={European conference on computer vision},
  pages={483--499},
  year={2016},
  organization={Springer}
}
```

Hourglass wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git