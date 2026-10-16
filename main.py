#!/usr/bin/env python3
import os, sys
from PIL import Image

folder_path = sys.argv[1]

os.makedirs("/opt/icons", exist_ok=True)

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename)

    if not os.path.isfile(full_path):
        continue

    f, _ = os.path.splitext(filename)

    converted_path = os.path.join("/opt/icons", f + ".jpeg")

    try:
        with Image.open(full_path) as img:
            (
            img.rotate(270, expand=True)
               .resize((128,128))
               .convert("RGB")
               .save(converted_path, "JPEG")
            )
            print(f"Converted: {filename} -> {os.path.basename(converted_path)}")
    except Exception as e:
        print(f"FAILED on {filename} -> Reason: {type(e).__name__}: {e}")