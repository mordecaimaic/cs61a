HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 0:
        return 0
    elif n % 10 == 8:
        return num_eights(n // 10) + 1
    else:
        return num_eights(n // 10)

def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    """
    --计算1个数的digit_distance--
    在写递归的时候，不要把函数具像化
    最好的方法：就是先把函数功能进行抽象化
    先完成else部分的内容
    再完成base case判断的内容
    ————John Berkeley cs61a
    """
    if n < 10:
        return 0
    else:
        return abs(n % 10 - n // 10 % 10) + digit_distance(n // 10)


def interleaved_sum(n, odd_term, even_term):
    """Compute the sum odd_term(1) + even_term(2) + odd_term(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1 + 2^2 + 3 + 4^2 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1^2 + 2 + 3^2 + 4 + 5^2
    41
    >>> interleaved_sum(4, triple, square) # 1 * 3 + 2^2 + 3 * 3 + 4^2
    32
    >>> interleaved_sum(4, square, triple) # 1^2 + 2 * 3 + 3^2 + 4 * 3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    """难点在于，如何不使用取余符号进行递归
    1.按照cs61a的课程说明，我们需要定义个helper才可以
    2.并且可以每次都调用同一个位置的函数，但是那个函数可以被调换位置
    3.How can you keep track of which function to use? 
    Is it possible to swap the two functions in the helper function's parameters during each recursive call?
    """
    def iterative_helper(f, g, k = 1):
        if k > n:
            return 0
        else:
            return iterative_helper(g, f, k + 1) + f(k)
    return iterative_helper(odd_term, even_term)
    

#------------------------------------------coin change recursision-------------------------------------------------------#
def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def count_coins_helper(n, m):
    """
    n < m
    count_conins_helper(5, 5) = 5
    count_conins_helper(5, 5) = 1 + 1 + 1 + 1 + 1
    >>> count_conins_helper(5, 5)
    2
    >>> count_conins_helper(10, 10)
    4
    """
    """
    重新定义一个helper函数，在count_coins里面调用这个count_coins函数即可
    和老师上课讲的最后一个count_partition的例子完全一模一样
    """
    if m == 1:
        return 1
    elif n < 0:
        return 0
    else:
        return count_coins_helper(n, next_smaller_coin(m)) + count_coins_helper(n - m, m)


def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if total >= 25:
        return count_coins_helper(total, 25)
    elif total >= 10:
        return count_coins_helper(total, 10)
    elif total >= 5:
        return count_coins_helper(total, 5)
    else:
        return count_coins_helper(total, 1)
#------------------------------------------------end----------------------------------------------------------------#

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"


from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'

