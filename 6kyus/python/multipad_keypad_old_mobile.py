one = "1ADGJMPTW*# "
two = "BEHKNQUX0"
three = "CFILORVY"
four = "SZ234568"
five = "79"


def presses(phrase):
    pulses = 0
    phrase = phrase.upper()
    for char in phrase:
        if char in one:
            pulses += 1
        elif char in two:
            pulses += 2
        elif char in three:
            pulses += 3
        elif char in four:
            pulses += 4
        else:
            pulses += 5
    return pulses
