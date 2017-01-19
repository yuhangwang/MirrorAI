"""
Read the CIFAR data set
"""
from ...tk.io.pypickle import readPyPickle
import numpy
import functools


def readCIFAR(meta_file, data_files):
    """Read CIFAR data files
    Args:
        meta_file (str): the CIFAR meta file
        data_files (list): a list of CIFAR data files
    Returns:
        a python dictionary containing all the data
    """
    def merge(xs):
        if type(xs[0]) == list:
            return reduce(+, xs, [])
        elif type(xs[0]) == numpy.ndarray:
            return numpy.concatenate(xs)
        else:
            return xs

    output = readPyPickle(meta_file, encoding="latin1")
    data = [readPyPickle(d, encoding="latin1") for d in data_files]
    if len(data) == 0:
        return output
    else:
        for k in data[0].keys():
            print("key = ", k)
            print(len(data[0][k]))
            print(data[0][k].shape)
            output[k] = numpy.concatenate([d[k] for d in data])
        return output
