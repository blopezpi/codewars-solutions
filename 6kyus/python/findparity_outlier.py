def find_outlier(integers):
    even = []
    odd = []
    for num in integers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]
