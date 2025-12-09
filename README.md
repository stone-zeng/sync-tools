# Sync tools

## GitHub

Clone GitHub repositories:

```sh
./clone.sh <name>/<repo>
```

## PyPI

Mirror PyPI packages using `bandersnatch`.

### Patch `bandersnatch`

We only need `x86_64` (Linux) and `amd64` (Windows) wheels, so we patch `bandersnatch` to only download those files.

```sh
p12y patch bandersnatch
p12y commit <edit_path>
p12y apply
```

### Mirror

TODO: configure and run `bandersnatch` to mirror PyPI packages.

## VS Code

Download VS Code and extensions:

```sh
python download.py ext vsix/vsix.txt
```

`vsix.txt` contains a list of extension information as:

```yaml
Name: Python
Id: ms-python.python
Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more.
Version: 2025.18.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python

Name: Python Debugger
Id: ms-python.debugpy
Description: Python Debugger extension using debugpy.
Version: 2025.16.0
Publisher: Microsoft
VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy
```
