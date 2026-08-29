from pathlib import Path
from PIL import Image

src = Path(".")  # directory with images
dst = Path(".")    # output directory
dst.mkdir(exist_ok=True)

for f in src.glob("*"):
    if f.suffix.lower() in (".png", ".jpg", ".jpeg"):
        img = Image.open(f)
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
        out = dst / f"{f.stem}.webp"
        img.save(out, "WEBP", quality=80, method=6)
        print(f"Saved {out}")
