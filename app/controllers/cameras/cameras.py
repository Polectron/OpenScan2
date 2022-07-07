import re
from typing import Optional
from v4l2py.device import iter_video_capture_devices
import gphoto2 as gp
from app.config import config
from app.controllers.cameras.camera import CameraController
from app.controllers.cameras.gphoto import GphotoController
from app.controllers.cameras.v4l2 import V4l2Controller

from app.models.camera import Camera, CameraType, CameraSettings

def clean_camera_path(name: str) -> str:
    return re.sub(r"\W", "", name)

def get_cameras() -> "dict[str, Camera]":
    cameras = {}
    v4l2_cameras = iter_video_capture_devices()
    cameras.update(
        {   f"{clean_camera_path(c.info.card)}":
            Camera(
                type=CameraType.V4L2,
                name=c.info.card,
                path=str(c.filename),
                settings=get_camera_settings(clean_camera_path(c.info.card)),
            )
            for c in v4l2_cameras
        }
    )
    gphoto2_cameras = gp.Camera.autodetect()
    cameras.update(
        {   f"{clean_camera_path(c[0])}":
            Camera(
                type=CameraType.GPHOTO2,
                name=c[0],
                path=c[1],
                settings=get_camera_settings(clean_camera_path(c[0])),
            )
            for c in gphoto2_cameras
        }
    )

    return cameras


def get_camera_settings(camera_id: str) -> Optional[CameraSettings]:
    return config.cameras.get(camera_id)


def get_camera(camera_id: int) -> Camera:
    cameras = get_cameras()
    if len(cameras) < camera_id + 1:
        raise ValueError(f"Can't find camera with id {camera_id}")
    return cameras[camera_id]


def get_camera_controller(camera: Camera) -> "type[CameraController]":
    if camera.type == CameraType.V4L2:
        return V4l2Controller
    elif camera.type == CameraType.GPHOTO2:
        return GphotoController
    raise ValueError(f"Couldn't find controller for {camera.type}")
