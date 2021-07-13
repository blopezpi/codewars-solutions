def expanded_form(num):
    calc = []
    for index, number in enumerate(str(num)):
        if number == "0":
            continue
        else:
            zeros = "0" * (len(str(num)) - index - 1)
            calc.append(str(number) + zeros)
    return ' + '.join(calc)
