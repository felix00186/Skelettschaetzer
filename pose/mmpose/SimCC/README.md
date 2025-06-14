# SimCC
**SimCC** reformuliert die 2D-Pose-Schätzung als zwei separate Klassifikationsaufgaben für horizontale und vertikale Koordinaten, wodurch eine subpixelgenaue Lokalisierung erreicht wird. Durch die Aufteilung jedes Pixels in mehrere Bins wird der Quantisierungsfehler deutlich reduziert, was zusätzliche Nachbearbeitung und aufwändige Upsampling-Schichten überflüssig macht. Das Ergebnis ist eine einfachere, effizientere Pipeline, die besonders bei niedrig aufgelösten Eingaben deutlich bessere Ergebnisse liefert als herkömmliche Heatmap-basierte Methoden.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/2107.03332
```bibtex
@misc{https://doi.org/10.48550/arxiv.2107.03332,
  title={SimCC: a Simple Coordinate Classification Perspective for Human Pose Estimation},
  author={Li, Yanjie and Yang, Sen and Liu, Peidong and Zhang, Shoukui and Wang, Yunxiao and Wang, Zhicheng and Yang, Wankou and Xia, Shu-Tao},
  year={2021}
}
```

SimCC wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git