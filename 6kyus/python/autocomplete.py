import re


def autocomplete(input_, dictionary):
    s = re.sub(r'[^a-zA-Z]', '', input_)
    return [ word for word in dictionary if word.upper().startswith(s.upper()) ][:5]
