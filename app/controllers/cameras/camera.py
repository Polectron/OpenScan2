import abc
import io

from src.models.camera import Camera


class CameraController(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def photo(camera: Camera) -> io.BytesIO:
        raise NotImplementedError

    @staticmethod
    @abc.abstractmethod
    def preview(camera: Camera) -> io.BytesIO:
        raise NotImplementedError
