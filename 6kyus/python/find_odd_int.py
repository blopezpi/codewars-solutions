from collections import Counter


def find_it(seq):
    counter = Counter(seq)
    result = 0
    for key in counter:
        if counter[key] % 2 != 0:
            result = key
    return result
