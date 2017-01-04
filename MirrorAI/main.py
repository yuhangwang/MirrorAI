from .core import is_mirror, make_pattern


def main(f_response):
    shape = (2, 2)
    I = make_pattern(shape)
    return is_mirror(I, f_response(I))
