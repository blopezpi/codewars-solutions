def unique_in_order(iterable):
    if not iterable:
        return []

    result = []
    result.append(iterable[0])
    for char in iterable:
        if str(char) in str(result[len(result) - 1]):
            continue
        result.append(char)
    return result
