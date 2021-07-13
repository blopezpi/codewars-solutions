def delete_nth(order,max_e):
    result = []
    for num in order:
        if result.count(num) < max_e:
            result.append(num)
    return result
