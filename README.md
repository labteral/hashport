<h1 align="center">hashport</h1>
<p align="center">
    A Python library that implements hashport.
    <br />
    <br />
</p>
<p align="center">
    <a href="https://pypi.python.org/pypi/hashport/"><img alt="PyPi" src="https://img.shields.io/pypi/v/hashport.svg?style=flat-square"></a>
    <a href="https://github.com/labteral/hashport/blob/master/LICENSE"><img alt="License" src="https://img.shields.io/github/license/labteral/hashport.svg?style=flat-square"></a>
</p>
<p align="center">
    <a href="https://www.buymeacoffee.com/brunneis" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="35px"></a>
</p>

Hashport is a function that generates a port number using a deterministic hashing algorithm. It takes a string input as the name of the project or entity that requires a port number and returns an integer value that falls within the range of ports typically used for dynamic assignments (49152 to 65535).

The function uses the SHA-256 algorithm to generate a hash of the input string. The resulting hash is then converted to an integer, and the integer is scaled to the desired range using modular arithmetic.

Hashport is useful in scenarios where a fixed and deterministic port assignment is required. By hashing the project name, the same input will always generate the same output, ensuring consistency and predictability in port assignments.

## Install or update
```bash
pip install -U hashport
```

## Usage
```python
from hashport import hashport

port = hashport('project-name')
```
