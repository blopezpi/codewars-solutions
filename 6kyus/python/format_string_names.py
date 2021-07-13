def namelist(names):
    result = ''
    if len(names) == 0:
        return ''
    elif len(names) == 1:
        return names[0]["name"]
    else:
        for index, name in enumerate(names):
            if index == len(names)-1:
                result += "& " + name["name"]
            elif index == len(names)-2:
                result += name["name"] + " "
            else:
                result += name["name"] + ", "
        return result
