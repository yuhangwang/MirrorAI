from MirrorAI.dataset.directional import sample
import numpy


def test():
    numpy.random.seed(100)
    n = 1
    size = 3
    low = 1
    high = 8
    answer = sample(n, size, low, high)
    solution = {
        "data": numpy.array([[0, 1, 4]]),
        "labels": numpy.array([[1, 0, 0]])
    }
    for i in range(len(solution['data'])):
        assert (answer['data'][i] == solution['data'][i]).all()
        assert (answer['labels'][i] == solution['labels'][i]).all()
