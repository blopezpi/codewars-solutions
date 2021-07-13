import math


def find_next_square(sq):
    num = math.sqrt(sq)
    if num == 0:
        return (num + 1)**2
    elif sq % num == 0:
        return (num + 1)**2
    else:
        return -1
