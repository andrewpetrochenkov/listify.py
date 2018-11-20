#!/usr/bin/env python
import listify


@listify.listify
def func():
    return


@listify.listify
def func2():
    yield "value"


@listify.listify
def func3():
    return [1, 2, 3]


assert isinstance(func(), list) == True
assert isinstance(func2(), list) == True
assert isinstance(func3(), list) == True
