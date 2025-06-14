# MSPN
**Multi-Stage Pose Network (MSPN)** kombiniert optimierte Einzelstufenmodule mit einem effizienten Cross‑Stage Feature Aggregation – das ermöglicht eine verbesserte Merkmalstiefe und -verteilung zwischen den Stufen. Zusätzlich sorgt eine Coarse‑to‑Fine-Supervision dafür, dass die Schätzung der Schlüsselpunktkoordinaten stufenweise verfeinert wird. Diese Kombination führt zu deutlich besseren Ergebnissen auf COCO und MPII und setzt neue Maßstäbe unter den Multi‑Stage-Architekturen.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/1901.00148
```bibtex
@article{li2019rethinking,
  title={Rethinking on Multi-Stage Networks for Human Pose Estimation},
  author={Li, Wenbo and Wang, Zhicheng and Yin, Binyi and Peng, Qixiang and Du, Yuming and Xiao, Tianzi and Yu, Gang and Lu, Hongtao and Wei, Yichen and Sun, Jian},
  journal={arXiv preprint arXiv:1901.00148},
  year={2019}
}
```

MSPN wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git