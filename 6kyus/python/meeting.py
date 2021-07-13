def meeting(s):
    return "".join(sorted(["(" + meet.split(":")[1].upper() + ", " + meet.split(":")[0].upper() + ")" for meet in s.split(";")]))
