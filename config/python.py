""" python depedencies for this project """
from typing import List


console_scripts: List[str] = [
    "pycookie=pycookie.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
    "pyyaml",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "browsercookie",
]
build_requires: List[str] = [
    "pymakehelper",
    "pydmt",
]
test_requires: List[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
