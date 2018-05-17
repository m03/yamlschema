from setuptools import setup
from inspect import cleandoc


_version = {}
execfile('yamlschema/_version.py', _version)


setup(
  name = 'yamlschema',
  packages = ['yamlschema', 'yamlschema.test'],
  version = _version['__version__'],
  description = 'A schema validator for YAML files',
  author = 'Ashley Fisher',
  author_email = 'fish.ash@gmail.com',
  url = 'https://github.com/Brightmd/yamlschema',
  keywords = ['yaml', 'schema'],
  classifiers = [],
  scripts = ['bin/yamlschema'],
  install_requires=cleandoc('''
    codado>=0.4.997,<0.6
    jsonschema==2.6.0
    ''').split(),
  setup_requires=cleandoc('''
    pytest-runner==4.2
    ''').split(),
  tests_require=cleandoc('''
    mock==2.0.0
    pyflakes==1.6.0
    pytest==3.2.3
    pytest-cov==2.5.1
    pytest-flakes==2.0.0
    ''').split()
)
