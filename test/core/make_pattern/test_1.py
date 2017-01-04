from MirrorAI.core import make_pattern


def test():
    shape = (2, 2)
    answer = make_pattern(shape)
    print(answer)
    assert (answer == answer).all()
