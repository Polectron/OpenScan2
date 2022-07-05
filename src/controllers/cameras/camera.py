import abc


class Camera(abc.ABC):
    @abc.abstractmethod
    def picture():
        raise NotImplementedError

    @abc.abstractmethod
    def preview():
        raise NotImplementedError
