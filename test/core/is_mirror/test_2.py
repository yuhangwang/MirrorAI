from MirrorAI.core import is_mirror
import numpy


def test():
    I = numpy.array([[1, 1], [2, 2]])
    R = numpy.array([[1, 2], [2, 2]])
    answer = is_mirror(I, R)
    solution = False
    assert answer == solution
