#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path


SECRET_PATTERNS = (
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)authorization:\s*bearer\s+[A-Za-z0-9._-]{16,}"),
)


def contains_secret(text: str) -> bool:
    return any(pattern.search(text) for pattern in SECRET_PATTERNS)


def tracked_paths(root: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=root,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [root / raw.decode() for raw in result.stdout.split(b"\0") if raw]


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for path in tracked_paths(root):
        relative = path.relative_to(root).as_posix()
        try:
            text = path.readlink().as_posix() if path.is_symlink() else path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if contains_secret(text):
            errors.append(f"credential-shaped content in {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path("."))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        assert contains_secret("gh" + "p_" + "A" * 32)
        assert contains_secret("Authorization: Bearer " + "a" * 24)
        assert not contains_secret("github_pat_[A-Za-z0-9_]{20,}")
        print("Public secret validator self-test passed.")
        return 0
    errors = validate(args.root.resolve())
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("Public secret validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
