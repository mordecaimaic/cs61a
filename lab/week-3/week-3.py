def check(f, num):
    n = 0
    while f(n) != num:
        n += 1
    return n

def reverse(f):
    """使用reverse可以获得f的函数，但是主义，只能够是输入是整数，输出也是整数"""
    return lambda y: check(f, y)



def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def cond(f):
        count = 1
        while count <= n:
            if f(count):
                print(count)
            count += 1
    return cond

def curry(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = curry(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = curry(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> curry(mod)(123)(10)
    3
    """
    "*** YOUR CODE HERE ***"
    def f(x):
        def g(y):
            return func(x, y)
        return g 
    return f


def f1():
    """
    >>> f1()
    3
    """
    "*** YOUR CODE HERE ***"
    return 3

def f2():
    """
    >>> f2()()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda : 3

def f3():
    """
    >>> f3()(3)
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda x: x

def f4():
    """
    >>> f4()()(3)()
    3
    """
    "*** YOUR CODE HERE ***"
    return lambda: lambda x: lambda: x

def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    # def ____________________________:
    #     ____________________________
    #     while ____________________________:
    #         if ____________________________:
    #             return ____________________________
    #         ____________________________
    #     ____________________________
    # ____________________________
    def check_part(num):
        n, temp = 0, num
        while n < k:
            digit = num % 10
            while temp // pow(10, k)> 0:
                temp, next_digit = divied_k_times(k, temp)
                # print("Debug: compare", digit, "and", next_digit)
                if next_digit != digit:
                    return False
            num = num // 10
            temp = num
            n += 1
        return True
    return check_part
            
def divied_k_times(k, num):
    while k > 0:
        num = num // 10
        k -= 1
    return num, num % 10

def remove(number, digit):
    """delete the digit in the number
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    assert(digit >= 0 and digit <= 9), "Digit Must between 0 and 9"
    n ,new = 0, 0
    while number > 0:
        ones_digit,number = number % 10, number // 10
        if ones_digit != digit:
            new += ones_digit * pow(10, n)
            n += 1
    return new


def trace(fn):
    """To trace function fn"""
    def traced(x):
        print("Calling", fn, "on argument", x)
        return fn(x)
    return traced


# @trace
def square(x):
    return x * x

# @trace
def sum_square(x):
    n, total = 1, 0
    while n <= x:
        total, n = total + square(n), n + 1
    return total