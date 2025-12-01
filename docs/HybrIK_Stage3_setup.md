# HybrIK Custom Pipeline – Stage 3 Setup Guide (Clean Version)

This guide describes how to set up **Stage 3** of the HybrIK pipeline on Google Colab:

- Install supporting libraries  
- Restore a pre-built **PyTorch3D** from Google Drive  
- Verify the environment  
- Clone and install HybrIK  
- Add model files (later)  

> **Assumptions**  
> - Colab with **GPU** enabled  
> - PyTorch **2.9.0 + cu126**  
> - Python **3.12**  
> - You already have this file in Drive:  
>   `/content/drive/MyDrive/libs_backup/pytorch3d_built_for_torch_2.9.0+cu126.zip`

---

## 0. Mount Google Drive

```python
from google.colab import drive
drive.mount('/content/drive')
```

Check Drive:

```bash
!ls -la /content/drive/MyDrive
```

---

## 1. Install base Python dependencies

```bash
!pip install torchgeometry
!pip install pycocotools
!pip install opencv-python
```

---

## 2. Install PyTorch3D from Google Drive backup

### 2.1 Run install script

```bash
!python /content/install_pytorch3d.py
```

This will:

- Extract the PyTorch3D build  
- Add it to `sys.path`  
- Verify import with `ico_sphere`

---

## 3. Verify all core imports

```bash
!python /content/verify_imports.py
```

Checks:

- PyTorch + CUDA  
- torchgeometry  
- pycocotools  
- OpenCV  
- PyTorch3D (`ico_sphere`)  

---

## 4. Clone HybrIK repository

```bash
%cd /content
!git clone https://github.com/Jeff-sjtu/HybrIK.git
```

Verify:

```bash
!ls -la /content/HybrIK
```

You should see:

- main.py  
- lib/  
- configs/  
- data/  
- README.md

---

## 5. Quick PyTorch3D Smoke Test

```python
from pytorch3d.utils import ico_sphere

mesh = ico_sphere(level=1)
print("✅ ico_sphere ok, verts:", mesh.verts_packed().shape)
```

---

## 6. Install HybrIK package

We now install HybrIK directly in Colab.

### 6.1 Install pycocotools

```bash
%cd /content/HybrIK
!pip install pycocotools
```

---

### 6.2 Patch setup.py for OpenCV fix

Install modern OpenCV:

```bash
!pip install opencv-python
```

Patch setup.py:

```python
from pathlib import Path

setup_path = Path("/content/HybrIK/setup.py")
text = setup_path.read_text()

text = text.replace("opencv-python==4.1.2.30", "opencv-python")

setup_path.write_text(text)
print("setup.py patched")
```

---

### 6.3 Install HybrIK editable

```bash
%cd /content/HybrIK
!pip install -e . --no-deps
```

---

### 6.4 Sanity check

```python
import hybrik
import cv2
import torch

print("HybrIK import OK:", hybrik.__file__)
print("OpenCV:", cv2.__version__)
print("Torch:", torch.__version__)
```

---

## 7. Download HybrIK Pretrained Models & Configs

HybrIK requires pretrained weights and config files.

### 7.1 Create directories
```bash
%cd /content/HybrIK
!mkdir -p pretrained_models
!mkdir -p configs/smplx
```

### 7.2 Download HybrIK model (SMPL)
```bash
!gdown --id 1gp3549vIEKfbc8SDQ-YF3Idi1aoR3DkW -O pretrained_models/hybrik_hrnet.pth

!wget -O configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml \
  https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml
```

### 7.3 Download HybrIK-X model (SMPL-X)
```bash
!gdown --id 1R0WbySXs_vceygKg_oWeLMNAZCEoCadG -O pretrained_models/hybrikx_rle_hrnet.pth

!wget -O configs/smplx/256x192_hrnet_rle_smplx_kid.yaml \
  https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/smplx/256x192_hrnet_rle_smplx_kid.yaml
```

### 7.4 Final directory structure
```
HybrIK/
├── pretrained_models/
│   ├── hybrik_hrnet.pth
│   └── hybrikx_rle_hrnet.pth
│
├── configs/
│   ├── 256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml
│   └── smplx/
│       └── 256x192_hrnet_rle_smplx_kid.yaml
```
