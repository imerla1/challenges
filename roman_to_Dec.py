SUBS = [
    ("IIIII", "V"),
    ("VV", "X"),
    ("XXXXX", "L"),
    ("LL", "C"),
    ("CCCCC", "D"),
    ("DD", "M"),
    ("IIII", "IV"),
    ("VIV", "IX"),
    ("XXXX", "XL"),
    ("LXL", "XC"),
    ("CCCC", "CD"),
    ("DCD", "CM"),
]


def to_roman(n):
    res = "I" * n
    for r in SUBS:
        res = res.replace(*r)
    return res


def to_int(n):
    res = n
    for r in SUBS[::-1]:
        res = res.replace(*r[::-1])
    return len(res)
