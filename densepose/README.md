# DensePose

<img src="./demo.gif" height="300px" />

## Quelle
DensePose ist als Erweiterung von Detectron 2 installiert (https://github.com/facebookresearch/detectron2.git).

Zum Zitieren kann der folgende Bibtex-Code verwendet werden:

```bibtex
@misc{detectron2,
  author =       {Yuxin Wu and Alexander Kirillov and Francisco Massa and
                  Wan-Yen Lo and Ross Girshick},
  title =        {Detectron2},
  howpublished = {\url{https://github.com/facebookresearch/detectron2}},
  year =         {2019}
}

@InProceedings{Guler2018DensePose,
  title={DensePose: Dense Human Pose Estimation In The Wild},
  author={R\{i}za Alp G\"uler, Natalia Neverova, Iasonas Kokkinos},
  journal={The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
  year={2018}
}
```

## Dokumentation
Nach der Installation diverser Pakete kann die Software DensePose ausgeführt werden,
die ein Teil des Repositorys von Detectron2 ist.

Da DensePose nur Bilder verarbeiten kann, wurde die `exec.py` geschrieben, in der
das eingegebene Video zunächst in einzelne Bilder zerlegt wird, die nach der Verarbeitung
durch DensePose in der richtigen Reihenfolge wieder zu einem Video zusammengesetzt werden.