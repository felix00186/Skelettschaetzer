# Skelettschätzer
## Voraussetzungen
Folgende technische Voraussetzungen müssen erfüllt sein:
* Linux Ubuntu, Version >= 20.3
* NVIDIA-Grafikkarte
* CUDA 12.0
* Docker, Version >= 20.10.22
* NVIDIA-Docker (die Schnittstelle zwischen NVIDIA-GPU und Docker)

## SSH-Verbindung
Da die Software hohe Anforderungen an die GPU hat, wurde sie so geschrieben, dass sie vollständig per SSH-Verbindung lauffähig ist.
Das schließt eine benutzerfreundliche Option über eine graphische Oberfläche zum Einspeisen von Videos und zum Betrachten der Ergebnisse ein.

Die Kommunikation läuft also per SSH. Sie benötigen die Ports `8888` und `8000`.
Sie können die SSH-Verbindung mit dem folgenden Befehl herstellen:

`ssh -L 8888:127.0.0.1:8888 -L 8000:127.0.0.1:8000 <user>@<server>`

## Installation
1. Sie benötigen einen Ordner für Daten, der mit ausreichenden Zugriffsrechten ausgestattet ist.
Den Pfad dieses Ordners schreiben Sie bitte:
   * in die `.env`-Datei in diesem Verzeichnis
   * in die `.env`-Datei im Verzeichnis `Visualisierung`
2. Innerhalb des von Ihnen ausgewählten Daten-Ordners muss ein Unterordner namens `input` existieren. Bitte erstellen Sie diesen.
3. Die Skelettschätzer befinden sich jeweils in eigenen Ordnern innerhalb des Ordners `pose`.
    Schauen Sie sich die dortigen Installationsanweisungen einmal an, da verschiedene Skelettschätzer
    bestimmte Downloads benötigen.

## Bedienung

### Input-Daten
In den Unterordner `input` innerhalb Ihres Daten-Ordners können Sie folgendes legen:
1. Videos im mp4-Format (beliebig viele)
2. Eine Datei namens `input.txt` mit Links zu YouTube-Videos. Der Link muss direkt zum Video führen. Pro Zeile ein Link.

Sie können die entsprechenden Dateien über das Terminal in den Ordner legen. Alternativ können Sie auch das Jupyter Notebook `runner.ipynb` nutzen.
Dieses stellt eine bequeme Variante dar, Dateien von Ihrem Computer auf den Host zu übertragen.

### Ausführung
Für die Ausführung können Sie sowohl das Terminal als auch eine graphische Oberfläche über ein Jupyter Notebook nutzen.

#### Terminal
1. Öffnen Sie eine Kommandozeile und wechseln Sie in den Stammordner des Repositorys.
2. Starten Sie die Software mittels `docker compose up`
3. Warten Sie, bis alle Container automatisch beendet sind.
4. Sie finden die generierten Videos mit Skelettschätzungen im von Ihnen gewählten Data-Ordner.

#### Graphische Oberfläche
Sie können erneut das Jupyter Notebook `runner.ipynb` nutzen. Auf diesem können Sie per Klick auf einen Button die Skelettschätzer starten.

#### Hinweise
Falls eine `input.txt` vorhanden ist, werden vor der Ausführung die YouTube-Videos davon heruntergeladen und zu den ggf. vorhandenen mp4-Dateien ergänzt.
Sollten keine Videos vorhanden sein, beendet sich die Anwendung mit einem Fehler.

### Visualisierung
Auch für die Visualisierung der Daten gibt es ein Jupyter Notebook. Da das Anschauen der Videos vom Host-System aus über SSH auf dem Notebook einen Webserver voraussetzt,
muss erneut ein Docker-Compose gestartet werden.

Bitte wechseln Sie in den Unterordner `Visualisierung`.
Dort können Sie nun `docker compose up` ausführen. Der Docker-Container startet. Wenn Sie vorher nach Anleitung die Portübertragung über SSH
aktiviert haben, können Sie das Notebook nun über `localhost:8888` in Ihrem Browser öffnen.

## Bildrechte
Die GIF-Bilder in den Unterordnern zeigen Lucas W. Kunze. Aufgenommen wurde das Video von Felix Semt.
Weiterverwendung nur zu wissenschaftlichen Zwecken erlaubt.