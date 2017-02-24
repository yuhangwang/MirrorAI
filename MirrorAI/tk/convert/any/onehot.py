import numpy


def onehot(x, categories):
    """
    Return a one-hot vector
    """
    output = numpy.zeros(len(categories))
    index = categories.index(x)
    output[index] = 1
    return output

