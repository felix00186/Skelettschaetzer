# Skelettschätzer
## Voraussetzungen
Folgende technische Voraussetzungen müssen erfüllt sein:
* Linux Ubuntu, Version >= 20.3
* NVIDIA-Grafikkarte
* CUDA 12.0
* Docker, Version >= 20.10.22
* NVIDIA-Docker (die Schnittstelle zwischen NVIDIA-GPU und Docker)

## Installation
Sie benötigen einen Ordner für Daten, der mit ausreichenden Zugriffsrechten ausgestattet ist.
Den Pfad wählen Sie in der Datei `.env` aus.

Die Installationsanleitungen für die einzelnen Skelettschätzer finden sich in den entsprechenden Unterordnern.

## Bedienung
Nachdem Sie alle Dateien des Respositorys heruntergeladen haben, können Sie die folgenden Schritte ausführen, um die Skelettschätzungen auszuführen:

### Input-Daten
Unterhalb des von Ihnen gewählten Data-Ordners müssen Sie einen Ordner namens `input` erstellen.
In diesen können Sie dann Folgendes ablegen:
1. Videos im mp4-Format (beliebig viele)
2. Eine Datei namens `input.txt` mit Links zu YouTube-Videos. Der Link muss direkt zum Video führen. Pro Zeile ein Link.

### Ausführung
1. Öffnen Sie eine Kommandozeile und wechseln Sie in den Stammordner des Repositorys.
2. Starten Sie die Software mittels `docker compose up`
3. Warten Sie, bis alle Container automatisch beendet sind.
4. Sie finden die generierten Videos mit Skelettschätzungen im von Ihnen gewählten Data-Ordner.

Falls eine `input.txt` vorhanden ist, werden vor der Ausführung die YouTube-Videos davon heruntergeladen und zu den ggf. vorhandenen mp4-Dateien ergänzt.
Sollten keine Videos vorhanden sein, beendet sich die Anwendung mit einem Fehler.

## Bildrechte
Die GIF-Bilder in den Unterordnern zeigen Lucas W. Kunze. Aufgenommen wurde das Video von Felix Semt.
Weiterverwendung nur zu wissenschaftlichen Zwecken erlaubt.