from v4l2py.device import iter_video_capture_devices
import gphoto2 as gp

from src.models.camera import Camera, CameraType

def get_cameras() -> "list[Camera]":
    cameras = []
    v4l2_cameras = iter_video_capture_devices()
    cameras.extend([Camera(CameraType.V4L2, c.info.card, str(c.filename), None) for c in v4l2_cameras])
    gphoto2_cameras = gp.Camera.autodetect()
    cameras.extend([Camera(CameraType.GPHOTO2, c[0], str(c.filename), None) for c in gphoto2_cameras])

    return cameras
