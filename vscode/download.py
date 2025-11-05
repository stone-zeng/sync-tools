import re
import sys

import requests


def download_ext(ext_file: str, ext_dir: str):
    with open(ext_file) as f:
        lines = [line for line in f.readlines() if not line.startswith("#")]
        exts = re.split(r"\n\n+", "".join(lines))
    for ext in exts:
        if not ext.strip():
            continue
        e = dict(i.split(": ", 1) for i in ext.splitlines() if i)
        id = e["Id"]
        version = e["Version"]
        publisher, name = id.split(".", 1)
        url = f"https://marketplace.visualstudio.com/_apis/public/gallery/publishers/{publisher}/vsextensions/{name}/{version}/vspackage"
        try:
            for platform in ["win32-x64", "linux-x64"]:
                platform_url = f"{url}?targetPlatform={platform}"
                response = requests.get(platform_url)
                response.raise_for_status()
                file = f"{id}-{version}@{platform}.vsix"
                print(f"Downloaded {file}")
                with open(f"{ext_dir}/{file}", "wb") as f:
                    f.write(response.content)
        except requests.HTTPError as e:
            response = requests.get(url)
            file = f"{id}-{version}.vsix"
            print(f"Downloaded {file}")
            with open(f"{ext_dir}/{file}", "wb") as f:
                f.write(response.content)


def main():
    match sys.argv[1]:
        case "code":
            pass
        case "ext":
            ext_dir = sys.argv[3] if len(sys.argv) >= 4 else "."
            download_ext(sys.argv[2], ext_dir)
        case _:
            print("Unknown command")
            sys.exit(1)


if __name__ == "__main__":
    main()
