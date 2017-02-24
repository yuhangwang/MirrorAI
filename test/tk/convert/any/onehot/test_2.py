from MirrorAI.tk import convert
import numpy


def test():
    categories = [True, False]
    x = False
    answer = convert.any.onehot(x, categories)
    solution = numpy.array([0, 1])
    assert (answer == solution).all()
