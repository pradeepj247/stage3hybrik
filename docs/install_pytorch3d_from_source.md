# Install PyTorch3D From Source (Fast Colab Guide)

## Overview
This guide provides a clean, minimal, and fast method to compile PyTorch3D from source
inside Google Colab. With the correct prerequisites installed, the build completes in ~5 minutes.

---

## 1. Install System Dependencies (Required for Fast Build)
These must be installed BEFORE building PyTorch3D. Missing these can slow compilation
from 5 minutes to 20+ minutes.

```bash
pip install -U \
  'fvcore>=0.1.5' \
  'iopath' \
  'ninja' \
  'tqdm' \
  'Pillow' \
  'scipy' \
  'numpy'
```

### Why these matter:

* ninja: fast C++/CUDA build backend
* fvcore / iopath: required for PyTorch3D internal modules
* scipy / numpy / Pillow: needed for geometry + data processing

---

## 2. Clone the PyTorch3D Source

```bash
%cd /content
git clone https://github.com/facebookresearch/pytorch3d.git pytorch3d-src
```

---

## 3. Build and Install PyTorch3D

```bash
%cd /content/pytorch3d-src
pip install -e .
```

Expected build time with correct prereqs: **3–6 minutes**.

---

## 4. Verify PyTorch3D Build

```python
import torch
import pytorch3d
from pytorch3d.utils import ico_sphere

print("Torch:", torch.__version__)
print("PyTorch3D:", pytorch3d.__version__)

mesh = ico_sphere(level=1)
print("verts:", mesh.verts_packed().shape)
print("faces:", mesh.faces_packed().shape)
```

If this runs without errors → **build successful**.

---

## 5. (Optional) Save a Backup for Future Colab Sessions

```bash
%cd /content
zip_name="pytorch3d_built_for_${torch.__version__}.zip"
zip -r $zip_name pytorch3d-src/pytorch3d
echo "Backup created:" $zip_name
```

Upload this zip to Drive for future sessions.

---

## 6. Clean Up Source Folder (Optional)

```bash
rm -rf /content/pytorch3d-src
```

---

## Summary

With the required prerequisites installed, PyTorch3D compiles very quickly on Colab.
This guide keeps the setup clean, predictable, and reproducible.

---

End of guide.