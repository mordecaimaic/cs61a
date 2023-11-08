from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1


def ordered_digits(x):
    """Return True if the (base 10) digits of X>0 are in non-decreasing
    order, and False otherwise.

    >>> ordered_digits(5)
    True
    >>> ordered_digits(11)
    True
    >>> ordered_digits(127)
    True
    >>> ordered_digits(1357)
    True
    >>> ordered_digits(21)
    False
    >>> result = ordered_digits(1375) # Return, don't print
    >>> result
    False

    """
    "*** YOUR CODE HERE ***"
    originial_x = x
    while originial_x > 0:
        last_digit = originial_x % 10
        originial_x, x = originial_x // 10, originial_x // 10
        while x > 0:
            if last_digit < x % 10:
                return False
            else:
                x = x // 10
    return True



def get_k_run_starter(n, k):
    """Returns the 0th digit of the kth increasing run within n.
    >>> get_k_run_starter(123444345, 0) # example from description
    3
    >>> get_k_run_starter(123444345, 1)
    4
    >>> get_k_run_starter(123444345, 2)
    4
    >>> get_k_run_starter(123444345, 3)
    1
    >>> get_k_run_starter(123412341234, 1)
    1
    >>> get_k_run_starter(1234234534564567, 0)
    4
    >>> get_k_run_starter(1234234534564567, 1)
    3
    >>> get_k_run_starter(1234234534564567, 2)
    2
    """
    i = 0
    final = None
    while i <= k:
        while n > 10:
            if n % 10 <= n // 10 % 10:
                break
            else:
                n = n // 10
        final = n % 10
        i = i + 1
        n = n // 10
    return final


def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    power_of_two = 1.0
    "*** YOUR CODE HERE ***"
    if x >= 1:
        while power_of_two < x:
            power_of_two *= 2
        if power_of_two - x <= x - power_of_two / 2:
            return power_of_two
        else:
            return power_of_two / 2 
    else:
        while power_of_two > x:
            power_of_two /= 2
        if x - power_of_two < power_of_two * 2 - x:
            return power_of_two
        else:
            return power_of_two * 2 




def make_repeater(func, n):
    """Returns the function that computes the nth application of func.

    >>> add_three = make_repeater(increment, 3)
    >>> add_three(5)
    8
    >>> make_repeater(triple, 5)(1) # 3 * 3 * 3 * 3 * 3 * 1
    243
    >>> make_repeater(square, 2)(5) # square(square(5))
    625
    >>> make_repeater(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> make_repeater(square, 0)(5) # Yes, it makes sense to apply the function zero times!
    5
    """
    "*** YOUR CODE HERE ***"
    def repeat(x):
        new_fun ,i = func, n
        if i > 0:
            while i > 1:
                new_fun = composer(new_fun, func)
                i -= 1
            return new_fun(x)
        else:
            return x
    return repeat

def composer(func1, func2):
    """Returns a function f, such that f(x) = func1(func2(x))."""
    def f(x):
        return func1(func2(x))
    return f

def apply_twice(func):
    """Returns a function that applies func twice.

    func -- a function that takes one argument

    >>> apply_twice(square)(2)
    16
    """
    "*** YOUR CODE HERE ***"
    return make_repeater(func, 2)


def div_by_primes_under(n):
    """
    >>> div_by_primes_under(10)(11)
    False
    >>> div_by_primes_under(10)(121)
    False
    >>> div_by_primes_under(10)(12)
    True
    >>> div_by_primes_under(5)(1)
    False
    """
    """
    有点巧妙的一个函数，div_by_primes_under(10)(11)，就是检测11能否被质数x整除，2 < x < 10，并且x要是质数是质数
    div_by_primes是一个返回check的函数
    checker在循环中被不断重新修饰(decorate)并且增加
    以下的语句是最核心的一条：
    checker = (lambda f, i: lambda x: f(x) or x % i == 0)(checker, i)
    
    为什么这样子就可以实现decorate的功能呢，我们可以从最开始的地方开始入手。
    1.最开始的时候check为false，i为2，此时check(2)为false，说明2是一个质数。
    2.此时外层的lambda函数对checker进行重新修饰，得出一个新的函数。此时新的checker(x) = False or x % 2
    3.当i为3的时候checker(3)依旧为False，所以要使用外层lambda对checker函数进行重新修饰，则此时的checker(x) = False % or x % 2 == 0  or x % 3 == 0
    4.当i为4的时候，checker(4)为True，此时由于 4 % 2 == 0是一件真的事情，因此checker不需要被修饰
    5.so on and so forth...
    """
    checker = lambda x: False
    i = 2
    while i < n:
        if not checker(i):
            checker = (lambda f, i: lambda x: f(x) or x % i == 0)(checker, i)
        i = i + 1
    return checker

def div_by_primes_under_no_lambda(n):
    """
    >>> div_by_primes_under_no_lambda(10)(11)
    False
    >>> div_by_primes_under_no_lambda(10)(121)
    False
    >>> div_by_primes_under_no_lambda(10)(12)
    True
    >>> div_by_primes_under_no_lambda(5)(1)
    False
    """
    def checker(x):
        return False
    i = 2
    while i < n:
        if not checker(i):
            def outer(checker, i):
                def inner(x):
                    return checker(x) or x % i == 0
                return inner
            checker = outer(checker, i)
        i = i + 1
    return checker

