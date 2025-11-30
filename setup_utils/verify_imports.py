"""
Verify PyTorch3D installation and print versions
"""
import sys
import os

# Add pytorch3d to path (in case it's not already)
pytorch3d_path = '/content/pytorch3d'
if os.path.exists(pytorch3d_path) and pytorch3d_path not in sys.path:
    sys.path.insert(0, pytorch3d_path)

print("🔍 Verifying all installations...")
print("=" * 50)

# 1. Verify PyTorch
try:
    import torch
    print(f"✅ PyTorch version: {torch.__version__}")
    print(f"✅ CUDA available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"✅ CUDA version: {torch.version.cuda}")
        print(f"✅ GPU device: {torch.cuda.get_device_name(0)}")
except ImportError as e:
    print(f"❌ PyTorch import failed: {e}")

print("-" * 50)

# 2. Verify Step 1 libraries
print("📦 Step 1 Libraries:")
try:
    import torchgeometry
    print("✅ torchgeometry imported successfully")
except ImportError as e:
    print(f"❌ torchgeometry import failed: {e}")

try:
    import pycocotools
    print("✅ pycocotools imported successfully")
except ImportError as e:
    print(f"❌ pycocotools import failed: {e}")

try:
    import cv2
    print(f"✅ OpenCV version: {cv2.__version__}")
except ImportError as e:
    print(f"❌ OpenCV import failed: {e}")

print("-" * 50)

# 3. Verify PyTorch3D
print("🎯 PyTorch3D Verification:")
try:
    import pytorch3d
    print(f"✅ PyTorch3D version: {pytorch3d.__version__}")
    
    # Test importing key modules
    from pytorch3d import structures, renderer, io
    print("✅ All PyTorch3D modules imported successfully")
    
    # Test basic functionality
    from pytorch3d.utils import ico_sphere
    mesh = ico_sphere(level=1)
    print(f"✅ Basic functionality test passed - Mesh vertices: {mesh.verts_packed().shape}")
    
except ImportError as e:
    print(f"❌ PyTorch3D import failed: {e}")
    print("💡 Make sure you ran install_pytorch3d.py first!")

print("=" * 50)
print("🎊 All verifications completed!")