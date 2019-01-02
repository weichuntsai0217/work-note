# DEMO pytest

## Installation

Please install `pytest` first.
```
$ pip install pytest
```

## `pytest` rules

The following rules are **VERY IMPORTANT**. If you don't follow them, `pytest` won't work.
* In every directory including `tests/`, you have to put a `__init__.py`.

* Every test file must be named like `test_*.py` or `*_test.py`, otherwise your test would fail.

## Usage

* In project root run all tests.
```
$ pytest ./
```

* In project root run single test (ex: `./foo/tests/test_foo.py`).
```
$ pytest ./foo/tests/test_foo.py
```
