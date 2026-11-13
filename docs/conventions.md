# Coding conventions

- **Python 3.12, standard library only.** No third-party dependency.
- **One public function per module.** `wordtools/<name>.py` holds the function `<name>`, and `tests/test_<name>.py` holds its tests. `wordtools/__init__.py` stays empty: callers import from the module, so two helpers never share a file.
- **Every public function** has type hints and a one-line docstring.
- **Tests use `unittest`.** Run them all from the repository's root with `python3 -m unittest discover -s tests -t .`.
