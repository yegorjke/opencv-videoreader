from typing import Optional, NoReturn, Any

import cv2

from .base import AbstractReader
from utils.unique import generate_unique_id


class Reader(AbstractReader):
    def __init__(self, path: Optional[str] = None, *args, **kwargs):
        self._id: str = generate_unique_id()

        self._path = path
        self._cap: Optional[cv2.VideoCapture] = None

    @property
    def id(self) -> str:
        return self._id

    @property
    def height(self) -> int:
        return self._height

    @property
    def width(self) -> int:
        return self._width

    @property
    def currentPosition(self) -> int:
        return int(self._cap.get(1))  # cv2.CAP_PROP_POS_FRAMES

    def activate(self, path: Optional[str] = None) -> NoReturn:
        if path is None:
            if self._path is None:
                raise AssertionError("path to source must be provided")

            if self.isActivated():
                # it had been activated because self._path had been provided and activated before
                return
        else:
            self.deactivate()  # any way
            self._path = path  # replace path

        self._cap = cv2.VideoCapture(self._path)

        # checking if successfully created
        if not self._cap.isOpened():
            self._cap = None  # because it still has type cv2.VideoCapture
            raise RuntimeError("reader haven't been activated")
        else:
            self._width = int(self._cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            self._height = int(self._cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    def deactivate(self) -> NoReturn:
        self._release()

    def isActivated(self) -> bool:
        return True if (self._cap is not None and self._cap.isOpened()) else False

    def read(self) -> Any:
        ret, mat = self._cap.read()

        if not ret or mat is None:
            raise

        return mat  # if ret else None

    def _release(self) -> NoReturn:
        try:
            self._cap.release()
        except Exception as e:
            print(f"exception: {e}")
        finally:
            self._cap = None

    def __enter__(self):
        self.activate()
        return self

    def __exit__(self, type, value, traceback):
        self.deactivate()
