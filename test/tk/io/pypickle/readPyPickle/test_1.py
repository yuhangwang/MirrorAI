from MirrorAI.tk.io.pypickle import readPyPickle
import pickle


def test():
    obj = {"a": 1}
    f_in = "input/in1.pickle"
    with open(f_in, 'wb') as OUT:
        pickle.dump(obj, OUT, pickle.HIGHEST_PROTOCOL)

    answer = readPyPickle(f_in)
    print(answer)
    assert answer == obj
