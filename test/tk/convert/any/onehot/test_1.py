from MirrorAI.tk import convert
import numpy


def test():
    categories = [True, False]
    x = True
    answer = convert.any.onehot(x, categories)
    solution = numpy.array([1, 0])
    assert (answer == solution).all()
