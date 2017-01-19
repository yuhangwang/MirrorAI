from MirrorAI.tk import functional


def test():
    data = [1, 2, 3]

    def f(x, y): return x + y
    answer = functional.reduce(f, data, 0)
    solution = 6
    assert answer == solution
