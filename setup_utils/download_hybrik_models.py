
#!/usr/bin/env python3
# download_hybrik_models.py
# Creates directories and downloads HybrIK + HybrIK-X models + configs.

import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path("/content/HybrIK")


def run(cmd):
    print(f"\n$ {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        print(f"❌ Command failed: {' '.join(cmd)}")
        sys.exit(result.returncode)


def main():
    # Check repo
    if not REPO_ROOT.exists():
        print("❌ /content/HybrIK not found. Clone the repo first.")
        sys.exit(1)

    os.chdir(REPO_ROOT)
    print(f"📁 Working directory: {os.getcwd()}")

    # Ensure gdown
    print("\n🔧 Installing gdown (if needed)...")
    run([sys.executable, "-m", "pip", "install", "-q", "gdown"])

    # Step 1 — Directories
    print("\n📂 Creating directories...")
    (REPO_ROOT / "pretrained_models").mkdir(exist_ok=True)
    (REPO_ROOT / "configs").mkdir(exist_ok=True)
    (REPO_ROOT / "configs" / "smplx").mkdir(parents=True, exist_ok=True)

    # Step 2 — HybrIK model
    print("\n⬇️ Downloading HybrIK model...")
    run([
        "gdown",
        "--id", "1gp3549vIEKfbc8SDQ-YF3Idi1aoR3DkW",
        "-O", "pretrained_models/hybrik_hrnet.pth"
    ])
    run([
        "wget",
        "-O", "configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml",
        "https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml"
    ])

    # Step 3 — HybrIK-X model
    print("\n⬇️ Downloading HybrIK-X model...")
    run([
        "gdown",
        "--id", "1R0WbySXs_vceygKg_oWeLMNAZCEoCadG",
        "-O", "pretrained_models/hybrikx_rle_hrnet.pth"
    ])
    run([
        "wget",
        "-O", "configs/smplx/256x192_hrnet_rle_smplx_kid.yaml",
        "https://raw.githubusercontent.com/jeffffffli/HybrIK/main/configs/smplx/256x192_hrnet_rle_smplx_kid.yaml"
    ])

    print("\n✅ Download complete.")
    print("Expected Structure:")
    print("pretrained_models/")
    print("  hybrik_hrnet.pth")
    print("  hybrikx_rle_hrnet.pth")
    print("configs/")
    print("  256x192_adam_lr1e-3-hrw48_cam_2x_w_pw3d_3dhp.yaml")
    print("  smplx/256x192_hrnet_rle_smplx_kid.yaml")


if __name__ == '__main__':
    main()
