def factorial (n, show=False):
    f = 1
    for c in range(n, 0 ,-1):
        f *= c
        print(f' {c} ', end='')
        if c > 1:
           print('X', end='')
        else:
            print('=', end='')
    return f


print(factorial(8))