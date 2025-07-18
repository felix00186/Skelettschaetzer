# PoseNet
PoseNet ist ein leichtgewichtiges Modell zur Skelettschätzung, das ursprünglich für Echtzeitanwendungen im Browser mit TensorFlow\.js entwickelt wurde. Es unterstützt sowohl MobileNet als auch ResNet als Backbone, wobei ResNet eine höhere Genauigkeit bei höherem Rechenaufwand bietet. PoseNet kann Einzelpersonen oder mehrere Personen in Bildern und Videos erkennen, ist jedoch im Vergleich zu moderneren Modellen wie MediaPipe oder OpenPose weniger präzise. Durch seine einfache Architektur eignet es sich gut für mobile Geräte und ressourcenschonende Umgebungen.

<img height="400px" src="demo.gif">

## Quellen
Die Software wurde in JavaScript implementiert und kann per `npm` installiert werden.

Zitiert werden kann folgendermaßen:

```bibtex
@misc{posenet2018,
  title        = {PoseNet: Real-time Human Pose Estimation},
  author       = {{Google Creative Lab and Google Brain}},
  year         = {2018},
  howpublished = {\url{https://github.com/tensorflow/tfjs-models/tree/master/posenet}}
}
```