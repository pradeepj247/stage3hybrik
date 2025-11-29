#!/bin/bash
# download_models.sh - Download required HybrIK models

echo "📥 Downloading HybrIK models..."

# Create directories
mkdir -p pretrained_models
mkdir -p configs/smplx

# HybrIK Model (Required)
echo "Downloading HybrIK model..."
gdown --id 1gp3549vIEKfbc8SDQ-YF3Idi1aoR3DkW -O pretrained_models/hybrik_hrnet.pth

echo "Downloading HybrIK config..."
wget -O configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml \
  https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml

# HybrIK-X Model (Optional)
echo "Downloading HybrIK-X model..."
gdown --id 1R0WbySXs_vceygKg_oWeLMNAZCEoCadG -O pretrained_models/hybrikx_rle_hrnet.pth

echo "Downloading HybrIK-X config..."
wget -O configs/smplx/256x192_hrnet_rle_smplx_kid.yaml \
  https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/smplx/256x192_hrnet_rle_smplx_kid.yaml

echo "✅ All models downloaded!"