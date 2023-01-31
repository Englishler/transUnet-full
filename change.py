from PIL import Image
import glob
import os
import tqdm

from pathlib import Path

current_dir = Path('.').resolve()

img_dir = current_dir / "data/train/masks"
out_dir = current_dir / "data/train/mask"
os.makedirs(out_dir, exist_ok=True)
cnt = 0

for img in tqdm.tqdm(glob.glob(str(img_dir / "*.bmp"))):
    filename = Path(img).stem
    Image.open(img).save(str(out_dir / f'{filename}.png'))