# yamlschema

A schema validator for YAML files

## For maintainers: How to build

First, increment `__version` in `__version.py`. Then:

```
python setup.py sdist bdist_wheel
twine upload dist/*<version>*
```

## Change Log

- 0.1.1 first working version