from MirrorAI.dataset.directional.label_image import label_image
import numpy


def test():
    d = numpy.array([1, 1, 0])
    answer = label_image(d, target=0)
    solution = 1
    assert answer == solution
