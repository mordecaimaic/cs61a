def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket_with_if(90, False)
    False
    >>> wears_jacket_with_if(40, False)
    True
    >>> wears_jacket_with_if(100, True)
    True
    """
    "*** YOUR CODE HERE ***"
    return temp < 60 or raining


def nearest_ten(n):
    """
    >>> nearest_ten(0)
    0
    >>> nearest_ten(4)
    0
    >>> nearest_ten(5)
    10
    >>> nearest_ten(61)
    60
    >>> nearest_ten(2023)
    2020
    """
    "*** YOUR CODE HERE ***"
    remainder = n %10
    if remainder < 5:
        return n - remainder
    else:
        return n + 10 - remainder
    
def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> print(result)
    None
    """
    "*** YOUR CODE HERE ***"
    k = 1
    while k <= n:
        if k % 3 == 0 and k % 5 == 0:
            print("fizzbuzz")
        elif k % 3 == 0:
            print("fizz")
        elif k % 5 == 0:
            print("buzz")
        else:
            print(k)
        k += 1

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    >>> is_prime(1) # one is not a prime number!!
    False
    """
    "*** YOUR CODE HERE ***"
    k = 2
    if n == 1:
        return False
    else:
        while(k < n):
            if n % k == 0:
                return False
            k += 1
        return True
    

def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    count, num = 0, 0
    while num <= 9:
        if has_digit(n, num):
            count += 1
        num += 1
    return count

def unique_digits_alt(n):
    unique_count = 0
    while n != 0:
        last = n % 10
        n = n // 10
        if not has_digit(n, last):
            unique_count += 1
    return unique_count

        


def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while (n > 0):
        if n % 10 == k:
            return True
        n = n // 10
    return False


        
