from MirrorAI.dataset import symmetric
import numpy


def test():
    height = 3
    width = 2
    low = 1
    high = 9
    count = 2
    result = symmetric.sample(
        count,
        height,
        width,
        low,
        high)
    print("results")
    for i, d in enumerate(result['data']):
        print(numpy.reshape(d, (height, width)))
        print(result['labels'][i])
