def natural(n):
    return n
def cube(n):
    return pow(n ,3)
def sum(n, term):
    """
    >>> sum(100, natural)
    5050
    """
    sum, k = 0, 1
    while k <= n:
        sum, k = sum + term(k), k + 1
    return sum

def sum_naturals(n):
    """
    >>> sum_naturals(5)
    15
    """
    return sum(n, natural)

def sum_cubes(n):
    """
    >>> sum_cubes(5)
    225
    """
    return sum(n, cube)

def sum_naturals_test(n):
    total, k = 0, 1
    while k <= n:
        k, total = k + 1, total + k
    return total