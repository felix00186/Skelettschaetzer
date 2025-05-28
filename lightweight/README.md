# Lightweight

Lightweight basiert auf einer stark optimierten Version von OpenPose und erkennt in Echtzeit die Körperhaltungen mehrerer Personen auf Bildern.
Dabei werden bis zu 18 Schlüsselpunkte pro Person (wie Augen, Schultern oder Knie) detektiert. Im Vergleich zu OpenPose bietet dieses Modell eine deutlich höhere Effizienz bei minimalem Genauigkeitsverlust.

## Quelle
Lightweight entstammt dem folgenden Repository:
https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch

Dem liegt die folgende Veröffentlichung zugrunde: https://arxiv.org/pdf/1811.12004

Zitiert werden kann folgendermaßen:
```bibtex
@inproceedings{osokin2018lightweight_openpose,
    author={Osokin, Daniil},
    title={Real-time 2D Multi-Person Pose Estimation on CPU: Lightweight OpenPose},
    booktitle = {arXiv preprint arXiv:1811.12004},
    year = {2018}
}
```

## CPU-Kompatibilität
Lightweight benötigt grundsätzlich keine GPU, sondern kann rein auf einer CPU arbeiten. Das ist allerdings deutlich ineffizienter.
Wenn Sie diese Lösung bevorzugen, tun Sie die folgenden beiden Dinge:
1. Öffnen Sie das Dockerfile. Ergänzen Sie in der letzten Zeile in der Liste nach `CMD` das Element `--cpu`.
2. Entfernen Sie in der `docker-compose.yml` im Stammverzeichnis beim Service `lightweight` den gesamten folgenden Abschnitt:
```yaml
deploy:
  resources:
    reservations:
      devices:
        - driver: nvidia
          count: all
          capabilities:
            - gpu
```