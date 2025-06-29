""" python deps for this project """

scripts: dict[str,str] = {
    "pycookie": "pycookie.main:main",
}
config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "browsercookie",
]
build_requires: list[str] = [
    "hatch",
    "pydmt",
    "pymakehelper",
    "pycmdtools",
    # modules
    "pyyaml",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "mypy",
    "ruff",
]
requires = config_requires + install_requires + build_requires + test_requires
