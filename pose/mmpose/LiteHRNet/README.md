# LiteHRNet
Lite-HRNet ist eine schlanke Pose-Estimation-Bibliothek in PyTorch, die auf effizienten Shuffle-Blöcken und kanalgewichteter Feature-Fusion basiert. Sie bietet hochauflösende Merkmalsverarbeitung bei geringem Rechenaufwand und ist damit gut für mobile oder ressourcenarme Anwendungen geeignet. Die Software umfasst vortrainierte Modelle, Trainingsskripte und eine modulare Architektur zur einfachen Anpassung.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://arxiv.org/pdf/2104.06403
```bibtex
@inproceedings{Yulitehrnet21,
  title={Lite-HRNet: A Lightweight High-Resolution Network},
  author={Yu, Changqian and Xiao, Bin and Gao, Changxin and Yuan, Lu and Zhang, Lei and Sang, Nong and Wang, Jingdong},
  booktitle={CVPR},
  year={2021}
}
```

LiteHRNet wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git