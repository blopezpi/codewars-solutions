def in_array(array1, array2):
    result = set()
    for i in array1:
        for j in array2:
            if j.__contains__(i):
                result.add(i)
    return sorted(list(result))
