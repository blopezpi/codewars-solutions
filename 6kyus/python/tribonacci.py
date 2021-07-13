def tribonacci(signature, n):
    if n == 0:
        return []
    elif n <= 3:
        return signature[0:n]
    first = signature[0]
    second = signature[1]
    third = signature[2]
    for _ in range(3, n):
        sum = first + second + third
        signature.append(sum)
        first = second
        second = third
        third = sum
    return signature
