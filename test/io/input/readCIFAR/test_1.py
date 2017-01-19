from MirrorAI.io.read import readCIFAR
import os


def test():
    dir_data = os.path.join("../../../..",
        "data/cifar/cifar-10-batches-py"
        )
    f_meta = os.path.join(dir_data, "batches.meta")
    data_files = [
            os.path.join(dir_data, "data_batch_1")
        ]
    answer = readCIFAR(f_meta, data_files)
    print(answer.keys())
