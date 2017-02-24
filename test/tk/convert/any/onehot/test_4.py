from MirrorAI.tk import convert
import numpy


def test():
    categories = [-1, 0, 1]
    x = 0
    answer = convert.any.onehot(x, categories)
    solution = numpy.array([0, 1, 0])
    assert (answer == solution).all()
