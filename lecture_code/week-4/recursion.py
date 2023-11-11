def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last
    
def check_credit(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return check_credit_doule(all_but_last) + last

def check_credit_doule(n):
    all_but_last, last = n // 10, n % 10
    double_number = sum_digits(2 * last)
    if n < 10:
        return double_number
    else:
        return check_credit(all_but_last) + double_number
    
def multiply(m, n):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        return m
    else:
        return multiply(m, n - 1) + m 

def multiply_v2(m, n, total):
    """Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return total
    else:
        return multiply_v2(m, n - 1, total + m)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n <= 2:
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.
    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 2:
        return False
    elif n % 2 == 0 and n != 2:
        return False
    else:
        return is_prime_rec(n, n-1)


def is_prime_rec(n, i):
    if i == 1:
        return True
    elif n % i == 0:
        return False
    else:
        return is_prime_rec(n, i-1)