from MirrorAI.dataset.directional.label_image import label_image
import numpy


def test():
    d = numpy.array([1, 0, 1])
    answer = label_image(d, target=0)
    solution = [0, 1, 0]
    assert (answer == solution).all()
