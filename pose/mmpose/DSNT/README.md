# DSNT
**DSNT-Layer** (Differentiable Spatial to Numerical Transform) ermöglicht die direkte Regression von Gelenkkoordinaten aus Feature-Maps – ganz ohne vollständig verbundene Schichten und ohne traditionelle Heatmap-Matching-Ansätze. DSNT ist voll differenzierbar, besitzt keine zusätzlichen Parameter und zeigt eine starke räumliche Generalisierungsfähigkeit, selbst bei niedriger Auflösung der Heatmaps. Im Vergleich zu herkömmlichen Verfahren erzielt DSNT sowohl eine höhere Genauigkeit als auch eine effizientere Inferenz – etwa eine dreifache Geschwindigkeit bei nur halb so hohem Speicheraufwand. Besonders in Kombination mit bewährten Architekturen wie Stacked Hourglass oder ResNet liefert DSNT verbesserte Ergebnisse auf dem MPII-Pose-Datensatz.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/1801.07372v2

```bibtex
@article{nibali2018numerical,
  title={Numerical Coordinate Regression with Convolutional Neural Networks},
  author={Nibali, Aiden and He, Zhen and Morgan, Stuart and Prendergast, Luke},
  journal={arXiv preprint arXiv:1801.07372},
  year={2018}
}
```

DSNT wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git