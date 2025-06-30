""" python deps for this project """

import config.shared

scripts: dict[str,str] = {
    "pycookie": "pycookie.main:main",
}

install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "browsercookie",
    "pyyaml",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires = install_requires + build_requires + test_requires
