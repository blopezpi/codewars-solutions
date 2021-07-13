def minimum_number(numbers):
    suma = sum(numbers)
    while True:
        for i in range(2, suma):
            if suma % i == 0:
                break
        else:
            break
        suma += 1

    return suma - sum(numbers)
