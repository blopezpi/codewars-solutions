def find_even_index(arr):
    arr1 = []
    for i in range(0, len(arr)):
        first = sum(arr[i+1:len(arr)])
        second = sum(arr[:i])
        if first == second:
            arr1.append(i)
    if len(arr1) == 0:
        return -1
    else:
        return arr1[0]
