# YoloPose
YOLOPose ist eine Erweiterung der YOLOv8-Architektur, die neben Objekterkennung auch die Posen einzelner Personen direkt schätzen kann. Dabei gibt das Modell für jede erkannte Person eine feste Anzahl von Keypoints (z. B. 17 Gelenkpunkte) mit Koordinaten und Konfidenzwerten aus. YOLOPose zeichnet sich durch seine hohe Geschwindigkeit und Effizienz aus, da Erkennung und Pose-Schätzung in einem einzigen Forward-Pass erfolgen. Es eignet sich besonders gut für Echtzeitanwendungen und läuft auch auf ressourcenschwächeren Geräten zuverlässig.

<img height="400px" src="demo.gif">

## Quellen
Der Skelettschätzer wurde auf Grundlage des folgenden Repositorys aufgebaut:
https://github.com/ultralytics/ultralytics.git

Zitiert werden kann folgendermaßen:
```bibtex
@software{glenn_jocher_2022_7347926,
  author       = {Glenn Jocher and
                  Ayush Chaurasia and
                  Alex Stoken and
                  Jirka Borovec and
                  NanoCode012 and
                  Yonghye Kwon and
                  Kalen Michael and
                  TaoXie and
                  Jiacong Fang and
                  imyhxy and
                  Lorna and
                  Zeng Yifu and
                  Colin Wong and
                  Abhiram V and
                  Diego Montes and
                  Zhiqiang Wang and
                  Cristi Fati and
                  Jebastin Nadar and
                  Laughing and
                  UnglvKitDe and
                  Victor Sonck and
                  tkianai and
                  yxNONG and
                  Piotr Skalski and
                  Adam Hogan and
                  Dhruv Nair and
                  Max Strobel and
                  Mrinal Jain},
  title        = {ultralytics/yolov5: v7.0 - YOLOv5 SOTA Realtime
                   Instance Segmentation
                  },
  month        = nov,
  year         = 2022,
  publisher    = {Zenodo},
  version      = {v7.0},
  doi          = {10.5281/zenodo.7347926},
  url          = {https://doi.org/10.5281/zenodo.7347926},
}
```

Es existiert (noch) keine wissenschaftliche Publikation, da der gesamte Aufwand in die Softwareentwicklung gesteckt wurde. Deshalb gibt es nur das Repository zum Zitieren.

## Besonderheiten
YoloPose ist besonders einfach zu handhaben, was die Hardware betrifft. Egal, ob man dem Docker-Container Zugang zu einer GPU gibt oder nicht - das Programm läuft. Es muss nicht mal eine Einstellung geändert werden. Hat der Container Zugang zur GPU, wird diese auch genutzt und die Verarbeitung läuft deutlich schneller. Wenn nicht, dann läuft es langsamer ... aber es funktioniert!