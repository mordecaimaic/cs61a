def search(f):
    x = 0
    while True:
        if f(x):
            return x
        else:
            x += 1

def is_three(x):
    return x == 3

def square(x):
    return x ** 2

def positive(x):
    return max(0, square(x) - 100)

def check_inverse(f, g):
    x = 0
    while True:
        f(g(x)) == x
        x += 1
def inverse(f):
    """inverse(f) = g, f(g(x)) == x, inverse function"""
    def g():
        search(x)