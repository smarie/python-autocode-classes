# python-autoclass

[![Build Status](https://travis-ci.org/smarie/python-autoclass.svg?branch=master)](https://travis-ci.org/smarie/python-autoclass) [![codecov](https://codecov.io/gh/smarie/python-autoclass/branch/master/graph/badge.svg)](https://codecov.io/gh/smarie/python-autoclass) [![Documentation](https://img.shields.io/badge/docs-latest-blue.svg)](https://smarie.github.io/python-autoclass/) [![PyPI](https://img.shields.io/badge/PyPI-autoclass-blue.svg)](https://pypi.python.org/pypi/autoclass/)

Project page : [https://smarie.github.io/python-autoclass/](https://smarie.github.io/python-autoclass/)

## What's new

* Improved documentation, and no longer hosted on readthedocs
* Travis and codecov integration
* Doc now generated from markdown using [mkdocs](http://www.mkdocs.org/)

## Want to contribute ?

Contributions are welcome ! Simply fork this project on github, commit your contributions, and create pull requests.

Here is a non-exhaustive list of interesting open topics: [https://github.com/smarie/python-autoclass/issues](https://github.com/smarie/python-autoclass/issues)

## Running the tests

This project uses `pytest`. 

```bash
pytest -v autoclass/tests/
```

You may need to install requirements for setup beforehand, using 

```bash
pip install -r requirements-test.txt
```

## Packaging

This project uses `setuptools_scm` to synchronise the version number. Therefore the following command should be used for development snapshots as well as official releases: 

```bash
python setup.py egg_info bdist_wheel rotate -m.whl -k3
```

You may need to install requirements for setup beforehand, using 

```bash
pip install -r requirements-setup.txt
```

## Generating the documentation page

This project uses `mkdocs` to generate its documentation page. Therefore building a local copy of the doc page may be done using:

```bash
mkdocs build
```

You may need to install requirements for doc beforehand, using 

```bash
pip install -r requirements-doc.txt
```

### PyPI Releasing memo

```bash
twine upload dist/* -r pypitest
twine upload dist/*
```