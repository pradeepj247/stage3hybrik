# PyTorch3D Installation (Manual)

Since PyTorch3D has compatibility issues, we use a dummy renderer.
But if you need actual rendering:

## Option 1: Install from our Google Drive wheels
1. Download PyTorch3D wheels from Google Drive
2. Install: `pip install /path/to/pytorch3d-*.whl`

## Option 2: Build from source
```bash
pip install "git+https://github.com/facebookresearch/pytorch3d.git@stable"
```

## Option 3: Use our dummy renderer (recommended)
No installation needed - we bypass PyTorch3D completely.