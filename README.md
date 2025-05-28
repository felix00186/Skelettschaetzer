# Skelettschätzer
## Voraussetzungen
Folgende technische Voraussetzungen müssen erfüllt sein:
* Linux Ubuntu, Version >= 20.3
* NVIDIA-Grafikkarte
* CUDA 12.0
* Docker, Version >= 20.10.22
* NVIDIA-Docker (die Schnittstelle zwischen NVIDIA-GPU und Docker)

## Installation
Sie benötigen einen Ordner `/srv/docker/skelettschaetzer/data`, der mit ausreichenden Zugriffsrechten ausgestattet ist.
Wenn Sie stattdessen einen anderen Ordner verwenden möchten, können Sie diesen Pfad in der `docker-compose.yml` dementsprechend ändern.

Die Installationsanleitungen für die einzelnen Skelettschätzer finden sich in den entsprechenden Unterordnern.

## Bedienung
Nachdem Sie alle Dateien des Respositorys heruntergeladen haben, können Sie die folgenden Schritte ausführen, um die Skelettschätzungen auszuführen:

### Input-Daten
Als Eingaben werden entweder ein Link zu einem YouTube-Video oder ein mp4-Video akzeptiert.
Die Eingaben müssen im data-Ordner (siehe Installation) liegen.

Wenn Sie ein mp4-Video eingeben möchten, dann legen Sie dieses als `input.mp4` in den data-Ordner.

Falls Sie ein YouTube-Video herunterladen möchten, schreiben Sie die vollständige URL in eine `input.txt` und schieben Sie diese in den data-Ordner.

Beachten Sie, dass im Falle dessen, dass sowohl mp4-Video als auch Link vorhanden sind, das mp4-Video bevorzugt wird.

### Ausführung
1. Öffnen Sie eine Kommandozeile und wechseln Sie in den Stammordner des Repositorys.
2. Starten Sie die Software mittels `docker compose up`
3. Warten Sie, bis alle Container automatisch beendet sind.
4. Sie finden die generierten Videos mit Skelettschätzungen im Ordner `data`.