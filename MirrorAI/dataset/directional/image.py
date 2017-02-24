import numpy

def image(n, low=1, high=9):
    """Return a 1D array with randomly chosen location for mirror"""
    output = numpy.random.randint(low, high=high, size=n)
    index = numpy.random.randint(0, len(output))
    output[index] = 0
    return output
