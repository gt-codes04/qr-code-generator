#!/usr/bin/env python3
import argparse
import os
import sys
from urllib.parse import urlparse

import qrcode

VALID_EXTS = {".png", ".jpg", ".jpeg"}
DEFAULT_URL = "http://github.com/kaw393939"
DEFAULT_DIR = "qr_codes"

def ensure_ext(path: str) -> str:
    root, ext = os.path.splitext(path)
    if ext.lower() in VALID_EXTS:
        return path
    # no or invalid ext → use .png
    return f"{root}.png" if ext else f"{path}.png"

def default_name_from_url(text: str) -> str:
    # try to make a friendly name from the URL; fallback to "qr.png"
    try:
        p = urlparse(text)
        base = (p.netloc or "qr").replace(":", "-").replace("/", "-")
        if not base:
            base = "qr"
    except Exception:
        base = "qr"
    return base + ".png"

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a QR code image from a URL or text.")
    parser.add_argument("--url", help="URL/text to encode (falls back to env DEFAULT_URL, then a default).")
    parser.add_argument("--out", help="Output filename (with or without extension).")
    parser.add_argument("--output-dir", help=f"Directory for output (default: ./{DEFAULT_DIR}).")
    args = parser.parse_args()

    # Resolve URL/text
    text = args.url or os.getenv("DEFAULT_URL") or DEFAULT_URL
    text = text.strip()
    if not text:
        print("Error: No content to encode. Provide --url or set DEFAULT_URL.", file=sys.stderr)
        return 1

    # Resolve output directory
    out_dir = os.path.abspath(args.output_dir or os.getenv("OUTPUT_DIR") or DEFAULT_DIR)
    os.makedirs(out_dir, exist_ok=True)

    # Resolve output filename
    if args.out:
        out_path = args.out
        if not os.path.isabs(out_path) and os.path.dirname(out_path) in {"", "."}:
            out_path = os.path.join(out_dir, out_path)
        out_path = ensure_ext(out_path)
    else:
        out_path = os.path.join(out_dir, default_name_from_url(text))

    # Generate and save
    img = qrcode.make(text)
    img.save(out_path)
    print(f"QR code saved to {out_path}")
    filename = os.path.join("qr_codes", "output.png")  # Ensure the filename has a valid extension
    return 0

if __name__ == "__main__":
    sys.exit(main())
