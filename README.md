# Skelettschätzer
## Voraussetzungen
Folgende technische Voraussetzungen müssen erfüllt sein:
* Windows 10 oder Windows 11
* NVIDIA-Grafikkarte
* Docker Desktop installiert und gestartet
* WSL 2 installiert
* WSL-Integration auf Docker Desktop aktiviert (Settings -> Resources -> WSL Integration -> Häkchen setzen und Ubuntu auswählen)

## Installation
Die Installationsanleitungen für die einzelnen Skelettschätzer finden sich in den entsprechenden Unterordnern.

## Bedienung
Nachdem Sie alle Dateien des Respositorys heruntergeladen haben, können Sie die folgenden Schritte ausführen, um die Skelettschätzungen auszuführen:
1. Schieben Sie ein .mp4-Video in den Ordner `data` und bennenen Sie dieses in `input.mp4` um.
2. Öffnen Sie eine Kommandozeile und wechseln Sie in den Stammordner des Repositorys.
3. Starten Sie die Software mittels `docker compose up --build`
4. Warten Sie, bis alle Container automatisch beendet sind.
5. Sie finden die generierten Videos mit Skelettschätzungen im Ordner `data`.