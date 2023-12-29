console_scripts = [
    "pycookie=pycookie.main:main",
]
dev_requires = [
    "pypitools",
    "pyyaml",
]
config_requires = []
install_requires = [
    "pytconf",
    "pylogconf",
    "browsercookie",
]
make_requires = [
    "pymakehelper",
    "pydmt",
    "pyclassifiers",
]
test_requires = [
    "pylint",
    "pytest",
    "pytest-cov",
    "flake8",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
