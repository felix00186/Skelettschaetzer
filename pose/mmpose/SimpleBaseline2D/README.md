# SimpleBaseline2D
SimpleBaseline2D bietet einfache, aber leistungsfähige Baseline-Methoden für sowohl Pose-Estimation als auch Pose-Tracking an. Diese Baselines sind bewusst minimalistisch gehalten, um die zunehmende Komplexität moderner Modelle zu reduzieren und so die Analyse, das Verständnis und den Vergleich von Algorithmen zu erleichtern. Trotz ihrer Einfachheit erzielen diese Methoden dennoch state-of-the-art Ergebnisse auf schwierigen Benchmarks. Der Code ist öffentlich verfügbar und bietet damit eine solide Grundlage für Forschung und Entwicklung im Bereich menschlicher Posen und deren Verfolgung über Zeit

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://openaccess.thecvf.com/content_ECCV_2018/papers/Bin_Xiao_Simple_Baselines_for_ECCV_2018_paper.pdf
```bibtex
@inproceedings{xiao2018simple,
  title={Simple baselines for human pose estimation and tracking},
  author={Xiao, Bin and Wu, Haiping and Wei, Yichen},
  booktitle={Proceedings of the European conference on computer vision (ECCV)},
  pages={466--481},
  year={2018}
}
```

SimpleBaseline2D wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git