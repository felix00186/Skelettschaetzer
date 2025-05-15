# Skelettschätzer
## Voraussetzungen
Folgende technische Voraussetzungen müssen erfüllt sein:
* Linux Ubuntu, Version >= 20.3
* NVIDIA-Grafikkarte
* CUDA 12.0
* Docker, Version >= 20.10.22

## Installation
Sie benötigen einen Ordner `/srv/docker/skelettschaetzer/data`, der mit ausreichenden Zugriffsrechten ausgestattet ist.
Wenn Sie stattdessen einen anderen Ordner verwenden möchten, können Sie diesen Pfad in der `docker-compose.yml` dementsprechend ändern.

Die Installationsanleitungen für die einzelnen Skelettschätzer finden sich in den entsprechenden Unterordnern.

## Bedienung
Nachdem Sie alle Dateien des Respositorys heruntergeladen haben, können Sie die folgenden Schritte ausführen, um die Skelettschätzungen auszuführen:
1. Schieben Sie ein .mp4-Video in den Ordner `/srv/docker/skelettschaetzer/data` und bennenen Sie dieses in `input.mp4` um.
2. Öffnen Sie eine Kommandozeile und wechseln Sie in den Stammordner des Repositorys.
3. Starten Sie die Software mittels `docker compose up --build`
4. Warten Sie, bis alle Container automatisch beendet sind.
5. Sie finden die generierten Videos mit Skelettschätzungen im Ordner `data`.