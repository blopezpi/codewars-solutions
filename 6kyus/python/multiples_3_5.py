def solution(number):
    if number < 0:
        return 0
    result = [i if i % 3 == 0 else i if i % 5 == 0 else 0 for i in range(number)]
    return sum(result)
