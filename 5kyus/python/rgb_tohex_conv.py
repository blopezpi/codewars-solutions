def rgb(*colors):
    result_hex = ""
    for color in colors:
        if color <= 0:
            result_hex += f"{0:02X}"
        elif color >= 255:
            result_hex += f"{255:02X}"
        else:
            result_hex += f"{color:02X}"
    return result_hex
