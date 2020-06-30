<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/listify.svg?maxAge=3600)](https://pypi.org/project/listify/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/listify.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/listify.py/actions)

### Installation
```bash
$ [sudo] pip install listify
```

#### Examples
`yield` + `list()`
```python
>>> def func():
        yield "value"

>>> list(func())
```
`list.append()`
```python
>>> def func():
        result = []
        result.append("value")
        return result
```

`@listify`
```python
>>> @listify
    def func():
        yield "value"
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>