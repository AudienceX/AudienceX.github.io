import os
import common
from PIL import Image

for fp in common.get_files_in_directory(common.tf_icon_dst_path, common.scan_file_types):
    img = Image.open(fp)
    w, h = img.size
    if w > 1024 or h > 1024:
        print(f"w={w}, h={h}, name={os.path.basename(fp)}, size={os.path.getsize(fp)/ 1024}")
        # os.remove(fp)