# 🚀 HYBRIK SETUP & DEBUGGING GUIDE

## 📋 STARTING POINT
We had a working HybrIK installation but our pipeline had **wrong scale/orientation/placement** of 3D meshes.

## 🎯 END GOAL ACHIEVED
Extracted **exact 3D parameters** from working HybrIK to fix our pipeline's scale/orientation issues.

---

## 🔧 STEP-BY-STEP BREAKTHROUGH

### 1. BYPASS BROKEN DEMO DEPENDENCIES
```python
# Critical: Fix Python 3.12 path for PyTorch3D
import sys
sys.path.insert(0, '/usr/local/lib/python3.12/site-packages')

# Bypass PyTorch3D rendering with dummy renderer
# Created: hybrik/utils/render_pytorch3d.py (dummy functions)
```

### 2. FIX CRITICAL DEPENDENCIES
```bash
# Fix chumpy for Python 3.12
sed -i 's/inspect.getargspec/inspect.getfullargspec/g' /usr/local/lib/python3.12/dist-packages/chumpy/ch.py

# Download missing model files:
# - smplx_kid_template.npy (from HuggingFace)
# - SMPLX_NEUTRAL.npz, SMPLX_MALE.npz, SMPLX_FEMALE.npz
```

### 3. EXTRACT WORKING 3D PARAMETERS
Created `extract_3d_data.py` → **SUCCESS!** Got:
- **Vertices**: `(6890, 3)` with proper human scale
- **Translation**: `[-0.739, -0.214, 7.810]`
- **Focal Length**: `1730.3 pixels`

### 4. GET EXACT CAMERA PARAMS
Created `working_renderer.py` → Extracted:
- **Bounding box**: `[167.14, 195.64, 442.96, 442.96]` (cx, cy, w, h)
- **Focal calculation**: `focal = 1000.0 / 256 * bbox_w`

### 5. CREATE VISUAL REFERENCE
Created `create_overlay.py` → Generated overlay images showing **correct placement**

---

## 📊 REFERENCE DATA OBTAINED

### 3D MESH SCALE (Meters):
```
X: [-0.309, 0.462]  → Width:  ~0.77m
Y: [-0.583, 0.946]  → Height: ~1.53m
Z: [-0.414, 0.241]  → Depth:  ~0.66m
```

### CAMERA PARAMETERS:
```python
translation = [-0.739, -0.214, 7.810]  # Camera position
focal_length = 1730.3                   # Scaled from bbox
image_size = (640, 429)                 # Width x Height
bbox_xywh = [167.14, 195.64, 442.96, 442.96]  # cx, cy, w, h
```

---

## 📁 FILES CREATED

### Core Scripts:
- `extract_3d_data.py` - Extract raw 3D vertices and translation
- `working_renderer.py` - Get exact camera parameters
- `create_overlay.py` - Create visual overlay reference
- `hybrik_camera_params.npy` - Saved parameters for pipeline

### Output Files:
- `vertices_3d.npy` - 3D mesh vertices (6890, 3)
- `translation.npy` - Camera translation vector
- `hybrik_overlay_comparison.png` - Visual comparison
- `mesh_overlay_only.jpg` - Mesh overlay on image

---

## 💾 MODEL FILES BACKUP

### Essential SMPL Files (274MB):
```
model_files/
├── basicModel_neutral_lbs_10_207_0_v1.0.0.pkl  # ← OUR PIPELINE USES THIS!
├── SMPL_NEUTRAL.pkl                            # ← AND THIS!
├── h36m_mean_beta.npy
├── J_regressor_h36m.npy
└── smplx_kid_template.npy
```

### Key Discovery:
Our working pipeline `HRNetSMPLCam` uses **SMPL v1.0.0 (.pkl files)**, not SMPL-X!

---

## 🎪 CRITICAL INSIGHTS

### 1. Focal Length Calculation:
```python
focal = 1000.0 / 256 * bbox_xywh[2]  # bbox_w
```

### 2. Coordinate System:
- **Y-axis**: Up/Down (height)
- **X-axis**: Left/Right (width)
- **Z-axis**: Depth (forward/backward)

### 3. Scale Reference:
- Human height: ~1.53m (Y-axis range)
- Proper proportions maintained
- Meters, not arbitrary units

---

## 🚨 COMMON PITFALLS SOLVED

1. **PyTorch3D version mismatch** → Used dummy renderer
2. **Python 3.12 compatibility** → Fixed chumpy imports
3. **Missing model files** → Downloaded from HuggingFace
4. **Wrong model type** → Discovered we use SMPL, not SMPL-X
5. **Path issues** → Explicit sys.path insertion

---

## ✅ VERIFICATION METHOD

Compare your pipeline output with:
1. **Numerical ranges**: Vertex coordinates should match reference
2. **Visual overlay**: Mesh should align with image
3. **Camera params**: Use exact focal length and translation

---

## 🏁 CONCLUSION

We successfully **extracted ground truth 3D parameters** from HybrIK,
bypassing all broken dependencies and creating a **minimal working pipeline**
that provides the exact scale, orientation, and placement references needed
to fix our own pipeline's 3D mesh issues!

**No more dependency hell - we have the reference data!** 🎉
