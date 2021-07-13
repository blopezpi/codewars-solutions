def in_array(array1, array2):
    return sorted(set(arr1 for arr1 in array1 for arr2 in array2 if arr1 in arr2))
