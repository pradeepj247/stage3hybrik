
import os
import sys
import shutil
from google.colab import drive

print("🚀 Starting PyTorch3D installation from Drive backup...")



# --------------------------------------------------
# 2. Paths
# --------------------------------------------------
backup_zip = "/content/drive/MyDrive/libs_backup/pytorch3d_built_for_torch_2.9.0+cu126.zip"
extract_root = "/content/pytorch3d_built"

print(f"📦 Backup zip: {backup_zip}")

# --------------------------------------------------
# 3. Clean any old extracted version
# --------------------------------------------------
if os.path.exists(extract_root):
    shutil.rmtree(extract_root)
    print(f"🧹 Removed existing folder: {extract_root}")

# --------------------------------------------------
# 4. Extract the zip
# --------------------------------------------------
print("📤 Extracting backup...")
shutil.unpack_archive(backup_zip, extract_root, "zip")

# After extraction, the structure looks like:
# /content/pytorch3d_built/content/pytorch3d-src/pytorch3d

inner_root = os.path.join(extract_root, "content", "pytorch3d-src")
pt3d_pkg_dir = os.path.join(inner_root, "pytorch3d")

# --------------------------------------------------
# 5. Validate extraction
# --------------------------------------------------
if not os.path.exists(pt3d_pkg_dir):
    raise FileNotFoundError(f"❌ Could not find pytorch3d package at: {pt3d_pkg_dir}")

print("📁 Located pytorch3d folder:", pt3d_pkg_dir)

# --------------------------------------------------
# 6. Add package parent to sys.path
# --------------------------------------------------
parent_to_add = inner_root   # parent folder containing pytorch3d/

if parent_to_add not in sys.path:
    sys.path.insert(0, parent_to_add)

print("🛠️ Added to sys.path:", parent_to_add)
print("sys.path[0:2] =", sys.path[:2])

# --------------------------------------------------
# 7. Import & test PyTorch3D
# --------------------------------------------------
print("🔍 Verifying import...")

import torch
import pytorch3d
from pytorch3d.utils import ico_sphere

print("Torch version:", torch.__version__)
print("PyTorch3D version:", pytorch3d.__version__)

# basic functionality test
mesh = ico_sphere(level=1)
print("Verts:", mesh.verts_packed().shape)
print("Faces:", mesh.faces_packed().shape)

print("🎉 PyTorch3D installation completed successfully!")
