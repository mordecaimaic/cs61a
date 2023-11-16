def trace(f):
    def g(*x):
        print("call", f,"on", *x, "return", f(*x))
    return g

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def cascade_reverse(n):
    grow(n)
    print(n)
    shrink(n)


def f_then_g(f, g, n):
    """use the higher order function to implement the inverse cascade"""
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


def grow(n):
    """
    >>> grow(1234)
    1
    12
    123
    """
    n = n // 10
    if n < 10:
        print(n)
    else:
        grow(n)
        print(n)


def shrink(n):
    """
    >>> shrink(1234)
    123
    12
    1
    """
    n = n // 10
    if n < 10:
        print(n)
    else:
        print(n)
        shrink(n)

# @trace
def count_partition(m, n):
    """
    2 + 4 = 6
    1 + 1 + 4 = 6
    3 + 3 = 6
    1 + 2 + 3 = 6
    1 + 1 + 1 + 3 = 6
    2 + 2 + 2 = 6
    1 + 1 + 2 + 2= 6
    1 + 1 + 1 + 1 + 2 = 6
    1 + 1 + 1 + 1 + 1 + 1 = 6
    >>> count_partition(6 , 4)
    9
    """
    if m == 0:
        return 1
    elif n == 0:
        return 0
    elif m < 0:
        return 0
    else:
        return  count_partition(m - n, n) + count_partition(m, n - 1)

def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)
    
def iterative_fibo(n):
    for i in range(n):
        print(fibo(i), end=" ")

def part_rec(n, m):
    if n < 0:
        return 0
    elif m == 1:
        return 1
    else:
        return part_rec(n - m, m) + part_rec(n, m - 1)