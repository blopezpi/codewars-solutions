import re


def valid_ISBN10(isbn):
    num = 0
    r = re.search(r'^\d{9}([X\d])$', isbn)
    if not r:
        return False
    if r.group(1) == "X":
        num += 10*len(isbn)
        isbn = re.sub(r'X$', "", isbn)
    return True if (num + sum([
        ((n+1)*int(isbn[n]))
        for n in range(len(isbn))
    ])) % 11 == 0 else False
