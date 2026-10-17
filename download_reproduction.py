#!/usr/bin/env python3
"""Download, verify and unpack the versioned GEO-PERIO scientific inputs and code."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import urllib.request
import zipfile


def sha256(path: Path) -> str:
    with path.open("rb") as handle:
        return hashlib.file_digest(handle, "sha256").hexdigest()


def verified(path: Path, item: dict) -> bool:
    return path.is_file() and path.stat().st_size == item["bytes"] and sha256(path) == item["sha256"]


def unpack(archive: Path, destination: Path) -> None:
    destination = destination.resolve()
    with zipfile.ZipFile(archive) as handle:
        for entry in handle.infolist():
            name = PurePosixPath(entry.filename)
            target = (destination / entry.filename).resolve()
            if name.is_absolute() or ".." in name.parts or not target.is_relative_to(destination):
                raise ValueError(f"Unsafe archive member: {entry.filename}")
            if name.parts[0] != "GEO_PERIO_Reproducibility":
                raise ValueError(f"Unexpected project directory: {entry.filename}")
            if ((entry.external_attr >> 16) & 0o170000) == 0o120000:
                raise ValueError(f"Unexpected symbolic link: {entry.filename}")
        bad = handle.testzip()
        if bad is not None:
            raise ValueError(f"Archive CRC failed: {bad}")
        handle.extractall(destination)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=Path.cwd(), help="Parent directory for the scientific project and downloaded archives")
    parser.add_argument("--figures-only", action="store_true", help="Download the self-contained figure code, embedded inputs and source tables")
    parser.add_argument("--download-only", action="store_true", help="Verify archives and retain them without unpacking")
    args = parser.parse_args()
    index = json.loads(Path(__file__).with_name("release-assets.json").read_text())
    selected = [a for a in index["assets"] if not args.figures_only or a["group"] == "figures"]
    if not selected:
        raise ValueError("No assets selected")
    destination = args.destination.expanduser().resolve()
    archive_dir = destination / "GEO_PERIO_Downloads" / index["version"]
    archive_dir.mkdir(parents=True, exist_ok=True)
    for item in selected:
        filename = item["name"]
        if Path(filename).name != filename or not filename.endswith(".zip"):
            raise ValueError(f"Invalid asset name: {filename}")
        expected_prefix = "https://github.com/Ab-code-inc/GEO-PERIO/releases/download/" + index["version"] + "/"
        if item["url"] != expected_prefix + filename:
            raise ValueError(f"Unexpected download location for {filename}")
        path = archive_dir / filename
        if verified(path, item):
            print(f"Verified existing archive: {filename}", flush=True)
        else:
            temporary = path.with_suffix(".zip.part")
            print(f"Downloading {filename} ({item['bytes']:,} bytes)", flush=True)
            request = urllib.request.Request(item["url"], headers={"User-Agent": "GEO-PERIO-reproduction/1.0"})
            with urllib.request.urlopen(request, timeout=120) as response, temporary.open("wb") as output:
                shutil.copyfileobj(response, output, length=1024 * 1024)
            if not verified(temporary, item):
                raise ValueError(f"Size or SHA-256 mismatch: {filename}")
            temporary.replace(path)
        if not args.download_only:
            print(f"Unpacking {filename}", flush=True)
            unpack(path, destination)
    print(f"Completed {len(selected)} verified archives in {destination}")


if __name__ == "__main__":
    main()
