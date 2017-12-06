# yamlschema

A schema validator for YAML files

## For maintainers: How to build

1. Increment `__version__` in `__version.py`.
2. Update the Change Log below.
3. Run the following:

```
python setup.py sdist bdist_wheel
twine upload dist/*<version>*
```

## Change Log
### [0.1.3] - 2017-12-06
#### Added
- Added jsonschema dependency to setup

### [0.1.2] - 2017-12-05
#### Changed
- Minor stylistic updates

[0.1.2]: https://github.com/Brightmd/yamlschema/tree/0.1.2
[0.1.3]: https://github.com/Brightmd/yamlschema/compare/0.1.2...0.1.3