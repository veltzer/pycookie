""" python deps for this project """

console_scripts: list[str] = [
    "pycookie=pycookie.main:main",
]
config_requires: list[str] = [
    "pyclassifiers",
]
install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "browsercookie",
]
build_requires: list[str] = [
    "pymakehelper",
    "pydmt",

    "pyyaml",
]
test_requires: list[str] = [
    "pylint",
    "pytest",
    "pytest-cov",
    "mypy",
]
requires = config_requires + install_requires + build_requires + test_requires
