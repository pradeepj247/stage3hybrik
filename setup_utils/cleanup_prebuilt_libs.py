import os
import shutil

PREBUILT_ROOT = '/content/prebuilt_libs'

print('🧹 Cleanup for prebuilt libraries')
print(f'Target directory: {PREBUILT_ROOT}')
print('-' * 50)

if os.path.exists(PREBUILT_ROOT):
    shutil.rmtree(PREBUILT_ROOT)
    print(f'✅ Removed directory and all contents: {PREBUILT_ROOT}')
else:
    print(f'ℹ️ Nothing to clean. Directory does not exist: {PREBUILT_ROOT}')

print('-' * 50)
print('🎉 Cleanup complete. Any prebuilt libraries will need to be reinstalled before use.')