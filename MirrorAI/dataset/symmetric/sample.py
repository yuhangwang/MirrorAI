import numpy
from .label_image import label_image
from .full_image import full_image


def sample(N, height, width, low, high):
    """Generate reflection samples
    Args:
        N (int): total number of samples
        height (int): height of each image
        width (int): width of each image
        low (int): lowest number
        high (int): highest number
    Returns:
        a list of pairs, i.e., flattened image and its label
    """
    raw = [label_image(full_image(height, width, low, high))
           for i in range(N)]
    return {
        "data": numpy.array([x[0] for x in raw]),
        "labels": numpy.array([x[1] for x in raw]),
    }
