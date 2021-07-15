for num in range(1, 101):
    result = f"{num} "
    if num % 3 == 0:
        result += "Fizz"
    if num % 5 == 0:
        result += "Buzz"

    print(result)
