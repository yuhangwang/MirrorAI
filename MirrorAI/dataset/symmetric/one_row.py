import numpy


def one_row(n, low, high):
    """Return one row of numbers

    Args:
        n (int): length
        low (int): lowest possible number
        high (int): highest possible number
    Returns:
        1D numpy array
    """
    return numpy.random.randint(low, high=high+1, size=n)
