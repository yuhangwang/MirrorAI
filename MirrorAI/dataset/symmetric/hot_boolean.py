def hot_boolean(isTrue):
    """Represent boolean as one-hot vector"""
    if isTrue:
        return [1, 0]
    else:
        return [0, 1]
