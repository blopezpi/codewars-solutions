def balance(left, right):
    left_result = 0
    right_result = 0
    for i in left:
        if i == "!":
            left_result += 2
        else:
            left_result += 3
    for i in right:
        if i == "!":
            right_result += 2
        else:
            right_result += 3
    if left_result > right_result:
        return "Left"
    elif left_result < right_result:
        return "Right"
    else:
        return "Balance"
