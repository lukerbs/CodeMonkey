#!/bin/bash

# Clean uninstall and remove all build artifacts
pip3 uninstall scriptmonkey -y
rm -rf dist/
rm -rf build/
rm -rf *.egg-info

# Build and upload
python3 setup.py sdist bdist_wheel
twine upload dist/*