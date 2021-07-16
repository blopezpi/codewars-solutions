num_primos = [2, 3]


def primo(num):
    for div in range(2, num):
        if num % div == 0:
            return False
    return True


for num in range(4, 101):
    if primo(num):
        num_primos.append(num)
print(num_primos)
