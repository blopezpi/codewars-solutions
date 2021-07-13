def iq_test(numbers):
    numbers = [int(i) for i in numbers.split()]
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]

    if len(even) == 1:
        return numbers.index(even[0]) + 1
    else:
        return numbers.index(odd[0]) + 1 
