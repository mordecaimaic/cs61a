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


#Q7: Doge
"""记录一下这个函数，看了有一点久
much可以理解为是一个修饰器（也就是对函数进行修饰的函数）
但是在理解为什么much == wow可以对函数进行判断的之前，我们可以先假设一个例子，可以做出一个验证
1. 证明
证明函数体内部可使可以读取到当前函数frame的名字的
def test():
    print("Debug", test)
当运行test()的时候，我们可以看到Debug <Function...>
当运行test的时候，我们看到<Function...>，和上面是一样的，因此可以说明在函数frame内部的时候，是可以读取到当前frame的函数地址的
2.因此当当执行much(much)的时候，我们可以知道 if much == wow这个条件很明显是正确的
3.在函数内部重新定义一个wow，这个函数不需要参数。并且当这个函数被执行的时候[wow()]，会返回一个新的函数such
4.such需要接受一个参数，但是such函数的主体和和传入的参数没有关系，会直接返回5
5.所以much(much)将会返回一个函数的修饰器，我们暂且把这个称做为lambda_1，并且它不会被执行。
6.接下来将会进入到much(lambda_1)，此时if much == wow这个条件为假。
7.接下来将会执行such = lambda wow: 4，但是这条语句很明显没有起到任何作用
8.所以such(lambda_1)将会直接返回wow()。wow也就是函数修饰器lambda_1，在执行函数修饰器lambda_1之后，将会生成一个新的函数
9.这个函数也就是我们在执行much(much)的时候定义的such，我们可以把这个函数先叫做lambda_2。lambda_2需要接受一个参数，但是直接返回5
10.所以 such(lambda_1) = lambda2
11.lambda2(Anything) = 5,结束:)

"""
wow = 6

def much(wow):
    if much == wow:
        such = lambda wow: 5
        print("Same")
        def wow():
            return such
        return wow
    such = lambda wow: 4
    return wow()


# wow = much(much(much))(wow)

def test():
    print("Debug", test)


y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y)




