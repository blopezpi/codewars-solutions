vowels = "aeiou"
values = "abcdefghijklmnopqrstuvwxyz"


def solve(s):
    vocab = [ i for i in values ]
    sum = 0
    result = []
    for letter in s:
        if letter not in vowels:
            sum += vocab.index(letter) + 1
        else:
            sum = 0
        result.append(sum)
    return max(result)
