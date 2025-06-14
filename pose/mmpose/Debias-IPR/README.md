# Debias-IPR
Der Skelettschätzer im Paper basiert auf der Integral Pose Regression, bei der Gelenkkoordinaten nicht direkt, sondern als Erwartungswert über eine implizite Heatmap unter Softmax‐Normierung berechnet werden. Die Autoren identifizieren dabei einen systematischen Bias, der durch die Kombination von Softmax und Erwartungsoperator entsteht – besonders wenn sich der Heatmap-Modus vom Zentrum entfernt. Zur Korrektur schlagen sie eine einfache Bias-Kompensation vor, die auf allen gängigen 2D-Pose-Datensätzen die Genauigkeit verbessert. Außerdem integrieren sie diesen kompensierten Regressionsteil mit einer herkömmlichen Heatmap‐Detektion zu einem gemeinsamen Lernframework, das sowohl eine schnelle Konvergenz als auch höhere Leistung in „harten“ Fällen erzielt

<img src="./demo.gif" height="300px" />

## Quelle
Die Technologie entstammt diesem Paper:
https://openaccess.thecvf.com/content/ICCV2021/papers/Gu_Removing_the_Bias_of_Integral_Pose_Regression_ICCV_2021_paper.pdf
```bibtex
@inproceedings{gu2021removing,
    title={Removing the Bias of Integral Pose Regression},
    author={Gu, Kerui and Yang, Linlin and Yao, Angela},
    booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
    pages={11067--11076},
    year={2021}
  }
```

Debias-IPR wurde mit Hilfe von MMPose implementiert. Dieses findet sich im folgenden Repository:
https://github.com/open-mmlab/mmpose.git