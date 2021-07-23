def hex_string_to_RGB(hex_string):
    hex_string = hex_string[1:]
    result = ["r", "g", "b"]
    return {
        result[i//2]: int(hex_string[i:i+2], 16)
        for i in range(0, len(hex_string), 2)
    }
