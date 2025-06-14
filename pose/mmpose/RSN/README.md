# RSN
RSN (**Residual Steps Network**) ist ein effizientes Pose-Schätzungsmodell, das durch gezielte Aggregation gleich großer Feature-Maps besonders präzise lokale Repräsentationen erzeugt. Unterstützt wird dies durch ein leichtgewichtiges Attention-Modul namens Pose Refine Machine, das die Genauigkeit der Gelenkpositionen weiter verbessert. Das Modell erzielt starke Ergebnisse auf COCO und MPII – ganz ohne externe Daten oder vortrainierte Backbones.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
```bibtex
@misc{cai2020learning,
    title={Learning Delicate Local Representations for Multi-Person Pose Estimation},
    author={Yuanhao Cai and Zhicheng Wang and Zhengxiong Luo and Binyi Yin and Angang Du and Haoqian Wang and Xinyu Zhou and Erjin Zhou and Xiangyu Zhang and Jian Sun},
    year={2020},
    eprint={2003.04030},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
```

RSN wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git