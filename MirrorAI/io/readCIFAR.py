"""
Read the CIFAR data set
"""


def readCIFAR(meta_file, data_files):
    """Read CIFAR data files
    Args:
        meta_file (str): the CIFAR meta file
        data_files (list): a list of CIFAR data files
    Returns:
        a python dictionary containing all the data
    """
    