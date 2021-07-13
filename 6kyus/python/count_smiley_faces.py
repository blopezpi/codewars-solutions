def get_smiles(arr):
    for i in range(len(arr)):
        if arr[i] in ":;":
            pass
        elif arr[i] in "-~":
            pass
        elif arr[i] in "D)":
            return True
        else:
            return False


def count_smileys(arr):
    smiles = filter(get_smiles, arr)
    result = 0
    for smile in smiles:
        result += 1
    return result
