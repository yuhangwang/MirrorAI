import numpy
from ...tk import convert


def label_image(img, target=0):
    """Return
        1 if the target is at the left half of the image
        0 if the target is at the middle
        -1 if the target is at the right half of the image
    """
    categories = [-1, 0, 1]
    def isEven(x):
        return x % 2 == 0
    def onehot(x):
        if x == -1:
            return numpy.array([1, 0, 0])
        elif x == 0:
            return 

    n = numpy.prod(numpy.shape(img))
    flat = numpy.reshape(img, (n,))
    index = numpy.argwhere(flat == target)[0]
    if isEven(n):
        if (index + 1) <= (n // 2):
            return convert.any.onehot(-1, categories)
        else:
            return convert.any.onehot(1, categories)
    else:
        middle = n // 2
        if index == middle:
            return convert.any.onehot(0, categories)
        elif index < middle:
            return convert.any.onehot(-1, categories)
        else:
            return convert.any.onehot(1, categories)
