def is_prime(n):
    """ Return True when {n} is a prime number and False otherwise
    """
    if n <= 1: 
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 1
    return True