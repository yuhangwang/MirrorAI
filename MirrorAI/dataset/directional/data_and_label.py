from .label_image import label_image


def data_and_label(img):
    return (img, label_image(img))
