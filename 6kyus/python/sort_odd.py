def sort_array(source_array):
    result = sorted([num for num in source_array if num % 2 != 0])
    for index, i in enumerate(source_array):
        if i % 2 == 0:
            result.insert(index, i)
    return result
