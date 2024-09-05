import functools as ft

d = {"a": 2, "b": 3, "c": 4}

r = ft.reduce(lambda a, b: a * b, d.values())
print(r)
