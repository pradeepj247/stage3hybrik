import os
import sys

print('🔍 PyTorch3D origin inspection')
print('=' * 50)

# 1. Torch
try:
    import torch
    print(f'✅ torch version: {torch.__version__}')
except Exception as e:
    print(f'❌ torch import failed: {e!r}')

print('-' * 50)

# 2. PyTorch3D
try:
    import pytorch3d
    print(f'✅ pytorch3d version: {pytorch3d.__version__}')
    print(f'📄 pytorch3d.__file__: {pytorch3d.__file__}')
    pkg_dir = os.path.dirname(pytorch3d.__file__)
    parent = os.path.dirname(pkg_dir)
    print(f'📁 pytorch3d package dir: {pkg_dir}')
    print(f'📂 parent directory: {parent}')
    in_path = parent in sys.path
    print(f'🔎 parent in sys.path: {"YES" if in_path else "NO"}')
    try:
        from pytorch3d import _C
        so_path = getattr(_C, '__file__', None)
        print(f'🧩 pytorch3d._C extension file: {so_path}')
    except Exception as e:
        print(f'⚠️ Could not import pytorch3d._C: {e!r}')
except Exception as e:
    print(f'❌ pytorch3d import failed: {e!r}')

print('=' * 50)
print('Sys.path (first 10 entries):')
for i, p in enumerate(sys.path[:10]):
    print(f'  [{i}] {p}')

print('=' * 50)
for path in ['/content/prebuilt_libs', '/content/prebuilt_libs/pytorch3d_built']:
    status = 'EXISTS' if os.path.exists(path) else 'missing'
    print(f'{path}: {status}')

print('=' * 50)
print('✅ Inspection complete.')