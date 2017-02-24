import numpy
from .image import image
from .data_and_label import data_and_label


def sample(N, size, low=1, high=9):
    """
    Return a dictionary with data
    and their labels
    Mirror object will be labeled as 0.

    Args:
        N (int): total number of samples to make
        size (int): size of the image
        low (int): lower bound of non-mirror objects
        high (int): upper bound for non-mirror objects
    """
    raw = [data_and_label(image(size, low, high))
           for i in range(N)]
    return {
        "data": numpy.array([x[0] for x in raw]),
        "labels": numpy.array([x[1] for x in raw]),
    }
