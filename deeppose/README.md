# DeepPose
DeepPose ist ein auf Deep Learning basierender Skelettschätzer, der menschliche Posen aus Bildern oder Videos präzise erkennt und rekonstruiert. Das System nutzt ein neuronales Netzwerk, um die Positionen von Körpergelenken direkt zu schätzen, ohne auf klassische Merkmalsextraktion angewiesen zu sein.

<img src="./demo.gif" height="300px" />

## Hinweis
⚠️ Im ausgegebenen Video ist sowohl Objekt-/Personenerkennung als auch Skelettschätzung implementiert.
Deeppose hat dabei nur die Skelettschätzung vorgenommen. Im gegebenen Softwarepaket
war allerdings die Skelettschätzung nur in Verbindung mit einer Objekterkennung möglich, die
DeepPose nicht bietet. Deshalb wurde diese aus einer fremden Quelle (Faster R-CNN) hinzugefügt.

## Quelle
Dem Projekt liegt das folgende Paper zugrunde: **DeepPose: Human Pose Estimation via Deep Neural Networks** (https://openaccess.thecvf.com/content_cvpr_2014/html/Toshev_DeepPose_Human_Pose_2014_CVPR_paper.html)

```bibtex
@InProceedings{Toshev_2014_CVPR,
    author = {Toshev, Alexander and Szegedy, Christian},
    title = {DeepPose: Human Pose Estimation via Deep Neural Networks},
    booktitle = {Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2014}
} 
```

DeepPose wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git