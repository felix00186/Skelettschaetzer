# OpenPifPaf
OpenPifPaf ist ein auf Deep Learning basierendes Open-Source-Framework zur präzisen 2D-Personen- und Skelettschätzung in Bildern. Es nutzt ein Bottom-up-Verfahren mit *Part Intensity Fields* (PIF) und *Part Association Fields* (PAF), um Körperpunkte und ihre Verbindungen zuverlässig zu erkennen. Die Software ist besonders für den Einsatz in komplexen Szenen mit mehreren Personen optimiert.

<img src="demo.gif" height="400px">

## Quelle
OpenPifPaf kann mit *pip* über *pipy.org* installiert werden.
Das Paket entstammt dem folgenden Repository:
https://github.com/openpifpaf/openpifpaf.git

Hier ist das zugehörige Paper: https://arxiv.org/abs/2103.02440

Dies sind die Lizenz-Informationen:
```
Copyright 2019-2021 by Sven Kreiss and contributors. All rights reserved.

This project and all its files are licensed under
GNU AGPLv3 or later version. A copy is included in docs/LICENSE.AGPL.

If this license is not suitable for your business or project
please contact EPFL-TTO (https://tto.epfl.ch/) for a full commercial license.

This software may not be used to harm any person deliberately.
```

Zitiert werden kann folgendermaßen:
```bibtex
@misc{kreiss2021openpifpafcompositefieldssemantic,
      title={OpenPifPaf: Composite Fields for Semantic Keypoint Detection and Spatio-Temporal Association}, 
      author={Sven Kreiss and Lorenzo Bertoni and Alexandre Alahi},
      year={2021},
      eprint={2103.02440},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2103.02440}, 
}
```