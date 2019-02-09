import re

def bird_codes(lst):
    for i in lst:
        separate = i.split(' ')
        if len(separate) == 1:
            return [c[0:4] for c in lst]
        if len(separate) == 2:
