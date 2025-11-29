# 🚀 Stage3 HybrIK - Working Pipeline

Minimal working implementation of HybrIK with all critical fixes applied.

## 📋 What's Fixed
- ✅ Python 3.12 compatibility (chumpy fixes)
- ✅ PyTorch3D dependency removed (dummy renderer)
- ✅ Correct 3D scale/orientation/placement
- ✅ Working camera parameters
- ✅ Complete documentation

## 🛠️ Setup
1. Clone original HybrIK: `git clone https://github.com/Jeff-sjtu/HybrIK.git`
2. Download model files (731MB) from Google Drive to `model_files/`
3. Copy these working files over the original
4. Run: `python extract_3d_data.py`

## 📁 Files
- `extract_3d_data.py` - Main 3D extraction
- `working_renderer.py` - Camera parameters
- `create_overlay.py` - Visualization
- `hybrik/utils/render_pytorch3d.py` - Dummy renderer
- `docs/HYBRIK_DEBUGGING_GUIDE.md` - Complete guide

## ⚠️ Note
Model files (731MB) not included - download separately.


## 📁 Required Assets
Download campus_walk.mp4, stage1_output.json, and stage2_output.json for full pipeline testing.

## 📁 Project Structure
```
stage3hybrik/
├── 📄 extract_3d_data.py       # Main 3D extraction
├── 📄 working_renderer.py      # Camera parameters
├── 📄 create_overlay.py        # Visualization
├── 📄 setup_environment.py     # Python 3.12 fixes
├── 📄 requirements.txt         # Dependencies
├── 📄 README.md                # This file
├── 📁 pipeline_data/           # Input assets
│   ├── 🎥 campus_walk.mp4      # Test video
│   ├── 📊 stage1_bboxes.json   # Stage1 results
│   ├── 📊 stage2_2dkps.json    # Stage2 results
│   └── 🖼️ testimage.jpg        # Test image
├── 📁 hybrik/utils/
│   └── 📄 render_pytorch3d.py  # Dummy renderer
└── 📁 docs/
    └── 📄 HYBRIK_DEBUGGING_GUIDE.md
```

## 🚀 Quick Start
```bash
# 1. Setup environment
python setup_environment.py

# 2. Run on test image
python extract_3d_data.py

# 3. Run on video with stage1/stage2 data
# (Modify scripts to use pipeline_data/ assets)
```
## 🖼️ Expected Output
Run `python create_overlay.py` to generate:
- **successful_overlay_example.png** - Reference output (included)
- Shows correct scale/orientation/placement

## 📊 Verification
Compare your output with the reference image to verify:
- Human scale: ~1.53m height
- Proper mesh alignment with image
- Correct camera perspective
