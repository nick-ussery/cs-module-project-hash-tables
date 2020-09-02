d = {
    "foo": 12,
    "bar": 17,
    "qux": 2,
    34: 3
}
i = list(d.items())


# i.sort(key=lambda e: str(e))  # sort by Key, then Value


def comp(e):
    return e[1]


i.sort(key=comp)
print(i)
