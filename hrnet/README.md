# HRNet
## Quelle

### Repository
Das Dockerfile wurde entsprechend der Anleitung des folgenden Git-Repositorys geschrieben: https://github.com/leoxiaobin/deep-high-resolution-net.pytorch.git

Außerdem wurde die COCO-API nach diesem Repository gebaut: https://github.com/cocodataset/cocoapi.git

Trainingsdaten, Modelle und Gewichte entstammen diesen beiden Quellen:
* COCO: http://cocodataset.org/#download
* MPII: http://human-pose.mpi-inf.mpg.de/

### Paper
Das Repository entstammt dem Paper `Deep High-Resolution Representation Learning for Human Pose Estimation` von Ke Sun, Bin Xiao, Dong Liu und Jingdong Wang.

Das Paper findet sich unter dem folgenden Link: https://arxiv.org/pdf/1902.09212

Zitiert werden kann mit diesen Quellenangaben:
```{bibtex}
@inproceedings{sun2019deep,
  title={Deep High-Resolution Representation Learning for Human Pose Estimation},
  author={Sun, Ke and Xiao, Bin and Liu, Dong and Wang, Jingdong},
  booktitle={CVPR},
  year={2019}
}

@inproceedings{xiao2018simple,
    author={Xiao, Bin and Wu, Haiping and Wei, Yichen},
    title={Simple Baselines for Human Pose Estimation and Tracking},
    booktitle = {European Conference on Computer Vision (ECCV)},
    year = {2018}
}

@article{WangSCJDZLMTWLX19,
  title={Deep High-Resolution Representation Learning for Visual Recognition},
  author={Jingdong Wang and Ke Sun and Tianheng Cheng and 
          Borui Jiang and Chaorui Deng and Yang Zhao and Dong Liu and Yadong Mu and 
          Mingkui Tan and Xinggang Wang and Wenyu Liu and Bin Xiao},
  journal   = {TPAMI}
  year={2019}
}
```