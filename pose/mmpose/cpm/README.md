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

DeepPose wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git