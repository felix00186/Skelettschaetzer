# HRNetV2
HRNetV2 is ein mehrstufiges HRNet‑Modell (Multi‑Stage HRNet), das auf dem Top‑Down‑Prinzip basiert und für jede Stufe hochauflösende Darstellungen beibehält. Durch „Cross‑Stage Feature Aggregation“ werden Merkmale zwischen den Stufen ausgetauscht und die Schlüsselpunkt-Schätzung kontinuierlich verfeinert. Diese Architektur erreicht auf dem COCO-Datensatz eine Test-dev-AP von 77.1 % mit einem einzelnen Modell in Single‑Scale‑Testkonfiguration.

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9052469
```bibtex
@article{WangSCJDZLMTWLX19,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Jingdong Wang and Ke Sun and Tianheng Cheng and
          Borui Jiang and Chaorui Deng and Yang Zhao and Dong Liu and Yadong Mu and
          Mingkui Tan and Xinggang Wang and Wenyu Liu and Bin Xiao},
  journal={TPAMI},
  year={2019}
}
```

HRNetV2 wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git