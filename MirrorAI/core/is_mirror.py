from numpy import ndarray
import numpy


def is_mirror(I, R):
    """Identify whether the object is from a mirror

    Args:
        I (ndarray): input matrix
        R (ndarray): response matrix
    Returns:
        True | False
    """
    return numpy.array_equal(I, R)
