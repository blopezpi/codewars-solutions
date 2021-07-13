def diamond(n):
    if n < 0: return None
    if n % 2 == 0: return None
    result = []
    for i in range(1,n+1,2):
        if i == n:
            result.append("*" * i + '\n')
        else:
            ast = ('*' * i).center(n).rstrip() + '\n'
            result.append(ast)
    reverse = reversed(result[:-1])
    diamond = result + list(reverse)
    return ''.join(diamond)
