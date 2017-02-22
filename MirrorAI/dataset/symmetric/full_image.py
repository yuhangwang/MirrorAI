import numpy
from .half_image import half_image


def full_image(height, width, low, high):
    """Return a matrix
    Returns a symmetric image with 50% probability

    Args:
        height (int): image height
        width (int): image width
        low (int): lowest possible number
        high (int): highest possible number
    Returns:
        2D numpy array
    """
    m = (height - 1) // 2
    coin = numpy.random.random()
    if coin > 0.5:
        return numpy.vstack([
                    half_image(m, width, low, high),
                    numpy.zeros(width),
                    half_image(m, width, low, high)
                ])
    else:
        half = half_image(m, width, low, high)
        return numpy.vstack([
                half,
                numpy.zeros(width),
                half[::-1, :]
            ])
