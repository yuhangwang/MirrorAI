import numpy
from .hot_boolean import hot_boolean


def label_image(a):
    m, n = numpy.shape(a)
    top = a[0:(m-1)//2, :]
    bottom = a[(m+1)//2:, :]
    isMirror = bool(numpy.amax(numpy.absolute(top - bottom[-1::-1])) < 1.0e-5)
    label = hot_boolean(isMirror)
    return (a.reshape((m*n,)), label)
