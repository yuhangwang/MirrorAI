import numpy


def label_image(img, target=0):
    """Return
        1 if the target is at the left half of the image
        0 if the target is at the middle
        -1 if the target is at the right half of the image
    """
    def isEven(x):
        return x % 2 == 0
    n = numpy.prod(numpy.shape(img))
    flat = numpy.reshape(img, (n,))
    index = numpy.argwhere(flat == target)[0]
    if isEven(n):
        if (index + 1) <= (n // 2):
            return -1
        else:
            return 1
    else:
        middle = n // 2
        if index == middle:
            return 0
        elif index < middle:
            return -1
        else:
            return 1
