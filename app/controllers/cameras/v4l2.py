import io
from v4l2py import Device

from src.models.camera import Camera

from .camera import CameraController


class V4l2Controller(CameraController):
    def photo(camera: Camera) -> io.BytesIO:
        with Device.from_id(0) as v4l2_camera:
            v4l2_camera_stream = iter(v4l2_camera)
            next(v4l2_camera_stream)  # first frame can be garbage
            return io.BytesIO(next(v4l2_camera_stream))

    def preview(camera: Camera) -> io.BytesIO:
        return V4l2Controller.photo(camera)
