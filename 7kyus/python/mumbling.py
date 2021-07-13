def accum(s):
    result = ""
    for i in range(len(s)):
        if i == len(s)-1:
            result += (s[i] * (i+1)).capitalize()
        else:
            result += (s[i] * (i+1)).capitalize() + "-"
    return result
