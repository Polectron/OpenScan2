from v4l2py import Device

from .camera import CameraController


class V4l2Controller(CameraController):
    def picture():
        raise NotImplementedError

    def preview():
        raise NotImplementedError
