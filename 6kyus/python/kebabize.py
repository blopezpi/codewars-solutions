def kebabize(string):
    result = ""
    for letter in string:
        if letter.isupper():
            result += "-"
        elif letter in "0123456789":
            continue
        result += letter.lower()
    return result.lstrip("-")
