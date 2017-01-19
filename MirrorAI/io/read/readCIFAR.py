"""
Read the CIFAR data set
"""
from ...tk.io.pypickle import readPyPickle
import numpy
from ...tk import functional


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
            return functional.reduce(lambda x, y: x + y, xs, [])
        elif type(xs[0]) == numpy.ndarray:
            return numpy.concatenate(xs)
        else:
            return xs

    def arrayToRGB(a):
        """Convert the CIFAR 1D array to 32x32x3 RGB image"""
        return numpy.transpose(
            numpy.array(
                [a[1024*i:1024*(i+1)].reshape((32,32))
                for i in range(3)]),
            axes=[1,2,0])

    output = readPyPickle(meta_file, encoding="latin1")
    data = [readPyPickle(d, encoding="latin1") for d in data_files]
    if len(data) == 0:
        return output
    else:
        for k in data[0].keys():
            output[k] = merge([d[k] for d in data])
        output["data"] = list(map(arrayToRGB, output["data"]))
        return output
