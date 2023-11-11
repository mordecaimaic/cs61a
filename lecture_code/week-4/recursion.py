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

def hailstone(n,):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"

    def hailstone_helper(n ,step):
        # print(n)
        if n == 1:
            return step
        elif n % 2 == 0:
            return hailstone_helper(n // 2, step + 1)
        else:
            return hailstone_helper(3*n + 1, step + 1)
    return hailstone_helper(n, 1)

def test(n):
    max, index, i = 0, 9, 1
    while i <= n:
        steps = hailstone(i)
        if max < steps:
            max = steps
            index = i
        if i % 10000 == 0:
            print("running:",round(i * 100 / n, 2) , "%")
        i += 1
    print("max_step:", max, "i:", index)


def merge(n1, n2):
    """Merges two numbers by digit in decreasing order.
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    # print(n1, n2)

    def merge_helper(n1, n2 , k):
        all_but_last_1, last_1 = n1 // 10, n1 % 10
        all_but_last_2, last_2 = n2 // 10, n2 % 10
        if n1 == 0 and n2 != 0:
            return single_merge(n2, k)
        elif n1 != 0 and n2 == 0:
            return single_merge(n1, k)
        elif n1 == 0 and n2 == 0:
            return 0      
        if last_1 == 0:
            return merge_helper(all_but_last_1, n2, k)
        elif last_2 == 0:
            return merge_helper(n1, all_but_last_2, k)
        if last_1 <= last_2 and last_1 > 0:
            min = last_1
            return merge_helper(all_but_last_1,  n2, k+1) + min*pow(10,k)
        elif last_1 > last_2 and last_2 > 0:
            min = last_2
            return merge_helper(n1,  all_but_last_2, k +  1) + min*pow(10,k)

    def single_merge(n, k):
        if(n == 0):
            return 0
        all_but_last, last = n // 10, n % 10
        return single_merge(all_but_last, k+1) + last*pow(10,k)
    

    return merge_helper(n1, n2 , 0)
    



    

def merge_copilot(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        last_digit_n1 = n1 % 10
        last_digit_n2 = n2 % 10
        if last_digit_n1 <= last_digit_n2:
            return merge(n1 // 10, n2) * 10 + last_digit_n1
        else:
            return merge(n1, n2 // 10) * 10 + last_digit_n2
        

def merge_new(n1, n2):
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    else:
        last_n1, last_n2 = n1 % 10, n2 % 10
    if last_n1 <= last_n2:
        return merge_new(n1 // 10, n2)*10 + last_n1
    else:
        return merge_new(n1, n2)*10 + last_n2