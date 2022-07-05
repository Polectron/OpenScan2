import abc


class CameraController(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def picture():
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def preview():
        raise NotImplementedError
