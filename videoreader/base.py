import abc


class AbstractReader(abc.ABC):
    @abc.abstractmethod
    def activate(self):
        pass

    @abc.abstractmethod
    def deactivate(self):
        pass

    @abc.abstractmethod
    def isActivated(self) -> bool:
        pass

    @abc.abstractproperty
    def id(self) -> str:
        pass

    @abc.abstractmethod
    def read(self):
        pass

    @abc.abstractproperty
    def currentPosition(self) -> int:
        pass

    @abc.abstractproperty
    def height(self) -> int:
        pass

    @abc.abstractproperty
    def width(self) -> int:
        pass

    def __enter__(self):
        raise NotImplementedError()

    def __exit__(self, type, value, traceback):
        pass
