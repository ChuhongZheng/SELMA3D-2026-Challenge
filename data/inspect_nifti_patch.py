#!/usr/bin/env python3
"""Print structural and statistical summary of a NIfTI patch (e.g. SELMA3D2026 .nii.gz)."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import numpy as np

try:
    import nibabel as nib
except ImportError as e:
    print("This script requires nibabel: pip install nibabel", file=sys.stderr)
    raise SystemExit(1) from e


def _repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def main() -> None:
    default_rel = Path(
        "datasets/SELMA3D2026_cropped_patches/isolated_structures/"
        "Sox9_Chondrogenic_cells/patchvolume_1000.nii.gz"
    )
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=_repo_root() / default_rel,
        help="Path to .nii or .nii.gz (default: SELMA3D2026 example patch under repo)",
    )
    args = parser.parse_args()
    path: Path = args.path.expanduser().resolve()

    print("=== Path ===")
    print(path)
    print(f"exists: {path.is_file()}")
    if not path.is_file():
        raise SystemExit(1)

    img = nib.load(str(path))
    hdr = img.header
    data = np.asarray(img.dataobj)

    print("\n=== Array (on-disk / as loaded) ===")
    print(f"shape: {data.shape}")
    print(f"dtype (array): {data.dtype}")
    print(f"dtype (header): {hdr.get_data_dtype()}")

    print("\n=== Intensity (finite voxels only) ===")
    finite = np.isfinite(data)
    if finite.any():
        v = data[finite]
        print(f"finite count: {v.size} / {data.size}")
        print(f"min: {v.min()}")
        print(f"max: {v.max()}")
        print(f"mean: {v.mean():.6g}")
        print(f"std: {v.std():.6g}")
        for p in (0.1, 0.5, 1, 5, 50, 95, 99, 99.5, 99.9):
            print(f"percentile {p}: {np.percentile(v, p):.6g}")
    else:
        print("no finite values")

    print("\n=== NIfTI header (spatial / display) ===")
    print(f"pixdim (raw header): {hdr['pixdim'].tolist()}")
    try:
        zooms = hdr.get_zooms()
        print(f"get_zooms(): {zooms}")
    except Exception as e:
        print(f"get_zooms(): <error: {e}>")
    print(f"dim: {hdr['dim'].tolist()}")
    print(f"cal_min / cal_max: {hdr['cal_min']} / {hdr['cal_max']}")
    print(f"scl_slope / scl_inter: {hdr['scl_slope']} / {hdr['scl_inter']}")

    print("\n=== Affine (voxel index -> mm RAS+) ===")
    print(np.array2string(img.affine, precision=6, suppress_small=False))

    print("\n=== qform / sform ===")
    print(f"get_qform(): {img.get_qform(coded=True)}")
    print(f"get_sform(): {img.get_sform(coded=True)}")
    print(f"qform_code: {hdr['qform_code']}, sform_code: {hdr['sform_code']}")

    print("\n=== nibabel image object ===")
    print(f"image class: {type(img).__name__}")
    print(f"dataobj class: {type(img.dataobj).__name__}")


if __name__ == "__main__":
    main()
