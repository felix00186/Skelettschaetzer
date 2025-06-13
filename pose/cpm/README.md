# CPM
CPM steht für Convolutional Pose Machines. Das Verfahren nutzt eine mehrstufige Architektur aus Convolutional Neural Networks, bei der in jeder Stufe sogenannte Belief Maps für die Positionen der Körperteile erzeugt werden. Diese Karten beschreiben die Wahrscheinlichkeitsverteilung für jedes Gelenk im Bild. Die Netzwerke in den späteren Stufen verwenden sowohl Bildinformationen als auch die Belief Maps aus den vorherigen Stufen, um schrittweise genauere Vorhersagen zu treffen. Durch Zwischenverluste an jeder Stufe wird das Problem verschwindender Gradienten beim Training vermieden und die Lernleistung verbessert.

## Quelle
Die Technologie entstammt diesem Paper:
```bibtex
@InProceedings{Wei_2016_CVPR,
    author = {Wei, Shih-En and Ramakrishna, Varun and Kanade, Takeo and Sheikh, Yaser},
    title = {Convolutional Pose Machines},
    booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2016}
}
```

## Implementierung
Implementiert wurde der Skelettschätzer mit Hilfe von
MMPose. Dieses Softwarepaket, das zahlreiche Skelettschätzer
unterstützt, finden Sie in diesem Repository: https://github.com/open-mmlab/mmpose.git

Sie können auf das Projekt folgendermaßen verweisen:
```bibtex
@misc{mmpose2020,
    title={OpenMMLab Pose Estimation Toolbox and Benchmark},
    author={MMPose Contributors},
    howpublished = {\url{https://github.com/open-mmlab/mmpose}},
    year={2020}
}
```