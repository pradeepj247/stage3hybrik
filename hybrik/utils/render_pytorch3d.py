"""
Dummy renderer - PyTorch3D compatibility disabled
"""
import torch

def render_mesh(*args, **kwargs):
    print("Rendering disabled: PyTorch3D not available")
    return None

def get_renderer(*args, **kwargs):
    print("Renderer creation disabled: PyTorch3D not available")
    return None
