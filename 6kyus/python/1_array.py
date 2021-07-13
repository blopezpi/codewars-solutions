def up_array(arr):
    if not arr:
        return None
    string_list = [ None if num < 0 else None if num > 9 else str(num) for num in arr ]
    if None in string_list:
        return None
    result = [ int(i) for i in str(int("".join(string_list)) + 1)]
    return result
