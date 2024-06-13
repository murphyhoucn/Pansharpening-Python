# Py_pansharpening [![License](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/codegaj/py_pansharpening/blob/master/LICENSE)

A Python version pansharpening toolbox with some classic methods. The toolbox implements the following algorithms so far,
- Brovey 
- PCA
- IHS
- SFIM
- GS
- Wavelet
- MTF-GLP
- MTF-GLP-HPM
- GSA
- CNMF
- GFPCA
- PNN
- PanNet

**Demo for Pansharpening**
```
python demo_pansharpening.py
```
 
**Demo for Evaluating All Methods**
```
python demo_all_methods.py
```

**Visualization**

![](./example_visualization.jpg)

**Evaluation**

![](./example_comparision.png)

**Requirements**
```
tensorflow-gpu==1.8.0
keras==2.2.4
numpy==1.14.2
cv2==4.1.0
scipy==1.2.1
scikit-learn==0.21.2
pywt==1.0.3
```

# My Re Implement

# Environment
``` bash
(Pansharpening-py) houjinliang@3080server:~/MyCVProject/fFusion/Pansharpening-Python$ pip list
Package               Version
--------------------- ---------
absl-py               1.4.0
astor                 0.8.1
bleach                1.5.0
cached-property       1.5.2
certifi               2021.5.30
dataclasses           0.8
gast                  0.5.4
grpcio                1.48.2
h5py                  3.1.0
html5lib              0.9999999
importlib-metadata    4.8.3
joblib                1.1.1
Keras                 2.2.4
Keras-Applications    1.0.8
Keras-Preprocessing   1.1.2
Markdown              3.3.7
numpy                 1.19.5
opencv-contrib-python 4.1.0.25
opencv-python         4.1.0.25
pip                   21.2.2
protobuf              3.19.6
PyWavelets            1.0.3
PyYAML                6.0.1
scikit-learn          0.21.2
scipy                 1.5.4
setuptools            58.0.4
six                   1.16.0
tensorboard           1.8.0
tensorflow-gpu        1.8.0
termcolor             1.1.0
typing_extensions     4.1.1
Werkzeug              2.0.3
wheel                 0.37.1
zipp                  3.6.0
```