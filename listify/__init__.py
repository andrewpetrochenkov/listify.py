__all__ = ['listify']


import functools
import types

"""
decorator for making generator functions return a list instead
"""


def listify(func):
    """`@listify` decorator"""
    @functools.wraps(func)
    def new_func(*args, **kwargs):
        r = func(*args, **kwargs)
        if r is None:
            return []
        if isinstance(r, types.GeneratorType):
            return list(r)
        return r
    return new_func
