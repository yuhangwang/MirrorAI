import numpy


def toGrayScale(rgb):
    """Convert RGB image to Gray Scale image"""
    # ref:
    # en.wikipedia.org/wiki/Grayscale#Converting_color_to_grayscale
    factor = [0.299, 0.587, 0.114]
    return numpy.dot(rgb[..., :3]/255., factor)
