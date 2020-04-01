from typing import Optional

import cv2
import numpy as np


def waitKey(timeout: Optional[int] = None):
    return cv2.waitKey(timeout) & 0xFF


def imshow(winname: str, mat: np.ndarray):
    cv2.imshow(winname, mat)


def destroyAllWindows():
    cv2.destroyAllWindows()
