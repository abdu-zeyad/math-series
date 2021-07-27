def fibonacci(n):
    # the formula is : Fn= Fn-1  + Fn-2
    if n <= 1:
        if n == 0:
            return 0
        else:
            return 1

    return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):

    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1

    return lucas(n-1) + lucas(n-2)


def sum_series(n, f=0, s=1):

    if n == 0:
        return f
    elif n == 1:
        return s
    else:
        return sum_series(n - 1, f, s) + sum_series(n - 2, f, s)


print(sum_series(6, 4, 5))
