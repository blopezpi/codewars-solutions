def multiplication_table(size):
    result = []
    for i in range(1, size+1):
        operation = []
        for j in range(1, size+1):
            operation.append(i*j)
        result.append(operation)
    return result
