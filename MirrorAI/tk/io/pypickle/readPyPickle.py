from typing import AnyStr, Dict
import pickle


def readPyPickle(file, encoding="latin1"):
    # type: (AnyStr, AnyStr) -> Dict
    """Read a python pickle file
    Args:
        file (str): input file name
        encoding (str): data encoding
    Returns:
        a python object
    """
    with open(file, "rb") as IN:
        return pickle.load(IN, encoding=encoding)
