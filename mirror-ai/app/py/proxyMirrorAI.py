from MirrorAI.io.read import readCIFAR
import os


def main():
    dir_data = os.path.join("../../..",
        "data/cifar/cifar-10-batches-py"
        )
    f_meta = os.path.join(dir_data, "batches.meta")
    data_files = [
            os.path.join(dir_data, "data_batch_1"),
            os.path.join(dir_data, "data_batch_2")
        ]
    answer = readCIFAR(f_meta, data_files)
    assert sorted(answer.keys()) == [
        'batch_label',
        'data',
        'filenames',
        'label_names',
        'labels',
        'num_cases_per_batch',
        'num_vis']
    assert len(answer['data']) == 20000
    assert answer['data'][0].shape == (32, 32, 3)
    return 123

if __name__ == '__main__':
    main()
