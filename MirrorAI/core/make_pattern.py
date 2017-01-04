import numpy


def make_pattern(shape, seed=None):
    """Make a pattern matrix of some shape

    Args:
        shape (tuple): the shape of the output
        seed (int): seed of random number generator
    Returns:
        an ndarray of shape ``shape``.
    """
    if seed is not None:
        numpy.random.seed(seed)
    else:
        pass

    return numpy.random.rand(*shape)
