from .one_row import one_row
import numpy


def half_image(m, n, low, high):
    """Return a matrix

    Args:
        m (int): number of rows
        n (int): number of columns
        low (int): lowest possible number
        high (int): highest possible number
    Returns:
        2D numpy array
    """
    return numpy.vstack([one_row(n, low, high) for i in range(m)])
