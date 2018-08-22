def fibo(n):
    """
    >>> [fibo(n) for n in range(1,7)]
    [1, 1, 2, 3, 5, 8]
    """
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)


def username(email):
    """
    >>> username('hovno@gmail.com')
    'hovno'
    """
    return email.split('@')[0]

import doctest

doctest.testmod()