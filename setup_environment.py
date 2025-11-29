"""Setup script for HybrIK environment fixes"""

import sys
import os
import subprocess

def fix_python_path():
    """Fix Python 3.12 path for PyTorch3D"""
    python_312_path = '/usr/local/lib/python3.12/site-packages'
    if python_312_path not in sys.path:
        sys.path.insert(0, python_312_path)
        print(f"✅ Added {python_312_path} to sys.path")
    return python_312_path

def patch_chumpy():
    """Patch chumpy for Python 3.12 compatibility"""
    chumpy_path = '/usr/local/lib/python3.12/dist-packages/chumpy/ch.py'
    patch_command = [
        'sed', '-i', 
        's/inspect.getargspec/inspect.getfullargspec/g', 
        chumpy_path
    ]
    
    try:
        subprocess.run(patch_command, check=True)
        print("✅ Patched chumpy for Python 3.12")
    except Exception as e:
        print(f"⚠️  Chumpy patch failed: {e}")
        print("Manual patch required: replace 'inspect.getargspec' with 'inspect.getfullargspec' in chumpy/ch.py")

if __name__ == "__main__":
    print("🔧 Setting up HybrIK environment...")
    fix_python_path()
    patch_chumpy()
    print("✅ Environment setup complete!")
