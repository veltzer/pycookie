# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pycookie/configs.py:7` - `ConfigDemo` with a `map_size` "size of mmap" parameter is leftover scaffolding from an lmdb project; nothing imports it and no endpoint uses it. Delete the module (and its section in `sphinx/pycookie.rst:7`), or replace it with a real config such as a browser choice.
- `src/pycookie/main.py:20` - `dump_cookies` is hardwired to `browsercookie.firefox()` with the Chrome and "all browsers" variants commented out (lines 18-19), although the package advertises chrome support (`pyproject.toml:21`, `config/project.lua:6`). Add a `--browser` option (firefox/chrome/all mapping to `browsercookie.firefox/chrome/load`).
- `src/pycookie/main.py:25` - iterates the private `cj._cookies` (needing a pylint suppression) and prints raw nested dicts. A `CookieJar` is iterable: `for cookie in cj:` and print `cookie.domain`, `cookie.name`, `cookie.value`; drop the commented-out debugging lines 21-22 and 28-30.
- `doc/TODO.txt:1` - the whole TODO (lmdb db entries, folder filters, a "dup" command, cursor `set_range`) belongs to pyunique (`../pyunique/doc/TODO.txt` has the same text) and has nothing to do with cookies. Replace it with pycookie's real TODO or delete it.

## Low

- `pyproject.toml:39` - `pyyaml` is a runtime dependency but nothing in `src/` imports `yaml`; remove it and refresh `uv.lock`.
- `tests/unit_tests/test_basic.py:20` - the only tests are import smoke tests. Once `dump_cookies` takes a browser option, add a test that patches `browsercookie.firefox` with an in-memory `CookieJar` and checks the printed output.
- `src/pycookie/__init__.py:5` - `LOGGER_NAME` is defined both here and in the generated `src/pycookie/static.py:5` and used by neither; keep one (the generated one) or drop both.
- `pyproject.toml:89` - fleet-wide pattern: `mypy_path = "src:python:scripts"` names nonexistent `python/` and `scripts/`, and `rsconstruct.toml:28`/`rsconstruct.toml:32` scan a `.lua`-only `config/` with ruff and mypy (89 repos carry the `config` entry, 82 this `mypy_path`); fix at the fleet's source.
