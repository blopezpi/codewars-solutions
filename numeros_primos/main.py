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

# With set()

num_primos.clear()

num_primos = {2, 3}

for num in range(4, 101):
    for div in range(2, num):
        if num % div == 0:
            if num in num_primos:
                num_primos.remove(num)
            break
        num_primos.add(num)

print(list(num_primos))
