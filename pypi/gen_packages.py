import re
import subprocess
from pathlib import Path

CWD = Path(__file__).parent


def old_packages() -> set[str]:
    packages = set()
    with open(CWD / "index.html") as f:
        for line in f:
            if match := re.match(r"<.+>(.+?)</a><br/>", line.strip()):
                packages.add(match[1])
    return packages


def new_packages() -> set[str]:
    p = subprocess.run(
        f"uv pip install --dry-run -r {CWD / 'requirements.txt'}",
        shell=True,
        check=True,
        capture_output=True,
        text=True,
    )
    return set(re.findall(r"\+\s+(.+)?==", p.stderr))


def main():
    old: set[str] = old_packages()
    new = new_packages()

    for i in sorted(new - old):
        print(f"    {i}")


if __name__ == "__main__":
    main()
