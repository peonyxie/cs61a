HW_SOURCE_FILE = 'hw04.py'

###############
#  Questions  #
###############

def intersection(st, ave):
    """Represent an intersection using the Cantor pairing function."""
    return (st+ave)*(st+ave+1)//2 + ave

def street(inter):
    return w(inter) - avenue(inter)

def avenue(inter):
    return inter - (w(inter) ** 2 + w(inter)) // 2

w = lambda z: int(((8*z+1)**0.5-1)/2)

def taxicab(a, b):
    """Return the taxicab distance between two intersections.

    >>> times_square = intersection(46, 7)
    >>> ess_a_bagel = intersection(51, 3)
    >>> taxicab(times_square, ess_a_bagel)
    9
    >>> taxicab(ess_a_bagel, times_square)
    9
    """
    return abs(street(a) - street(b)) + abs(avenue(a) - avenue(b))


def squares(s):
    """Returns a new list containing square roots of the elements of the
    original list that are perfect squares.

    >>> seq = [8, 49, 8, 9, 2, 1, 100, 102]
    >>> squares(seq)
    [7, 3, 1, 10]
    >>> seq = [500, 30]
    >>> squares(seq)
    []
    """

    def is_square(n):
        return (round(n ** 0.5)) ** 2 == n

    return [int(k ** 0.5) for k in s if is_square(k)]


def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g', ['While', 'For'])
    True
    """
    if n <= 3:
        return n
    return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'g_iter', ['Recursion'])
    True
    """
    first_three = [10, 22, 51]
    if n <= 3:
        return n
    elif n <= 6:
        n = first_three[n-4]
        return n
    else:
        first_n = first_three
        for i in range(n-6):
            n = first_n[n-7] + 2 * first_n[n-6] + 3 * first_n[n-5]
            first_n = first_n + [n]
        return n


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    def has_seven(k):
        if k % 10 == 7:
            return True
        elif k < 10:
            return False
        else:
            return has_seven(k // 10)

    '''def check(index):
        if index < 7:
            return 1 #turn 1 time
        if index % 7 == 0 or has_seven(index):
            return check(index - 1) + 1 #turn n+1 times
        return check(index - 1)
#if turn even times, +; if odd, -
    if n <= 7:
        return n
    if check(n - 1) % 2 == 0:
        return pingpong(n - 1) - 1
    return pingpong(n - 1) + 1'''

    def inc(index, value):
        if index == n:
            return value
        if has_seven(index) or index % 7 == 0:
            return dec(index + 1, value - 1)
        return inc(index+1, value+1)

    def dec(index, value):
        if index == n:
            return value
        if has_seven(index) or index % 7 == 0:
            return inc(index + 1, value + 1)
        return dec(index+1, value-1)

    return inc(1,1)



def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)

def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    def count_partitions(amount, min_coin):
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif min_coin > amount:
            return 0
        else:
            return count_partitions(amount-min_coin, min_coin) + count_partitions(amount, min_coin*2)
    return count_partitions(amount, 1)

###################
# Extra Questions #
###################

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return 'YOUR_EXPRESSION_HERE'