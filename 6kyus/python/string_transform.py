def string_transformer(s):
    result = "".join([letter.lower() if letter.isupper() else letter.upper() if letter.islower() else "- -" for letter in s])
    return "".join(list(reversed(result.split("-"))))
