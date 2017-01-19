def reduce(f, xs, init):
    """Reduce operation
    Args:
        f (function): a python function for combining two objects
        xs (list): a list of objects
        init (object): the initial object
    Returns:
        a combined object defined by the output of "f"
    """
    output = init
    for x in xs:
        output = f(output, x)
    return output
