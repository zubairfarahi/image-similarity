import os

import cv2


def image_to_bytes(frame):
    """
    :param frame: WxHx3 ndarray
    """
    _, bts = cv2.imencode(".jpeg", frame)
    bts = bts.tostring()
    return bts


def create_if_not_exists(paths):
    """
    Function checks a list given path if exists and then if not creates each of them.
    """
    for path in paths:
        is_created = create_if_not_exist(path)
        if not is_created:
            return is_created

    return True


def create_if_not_exist(path):
    """
    Function checks if the given path exists and then creates if not.
    """
    exists = os.path.exists(path)
    if not exists:
        try:
            os.makedirs(path)
        except OSError:
            return False

    return True


def save_exception_file(pathdir, filename, file_contents):
    with open(os.path.join(pathdir, filename), "wb") as binary_file:
        binary_file.write(file_contents)
    return
