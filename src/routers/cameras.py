from fastapi import APIRouter, Response
from fastapi.encoders import jsonable_encoder

from src.controllers.cameras.v4l2 import V4l2Controller
from src.controllers.cameras.cameras import (
    get_camera,
    get_camera_controller,
    get_cameras,
)

router = APIRouter(
    prefix="/cameras",
    tags=["cameras"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def cameras():
    return jsonable_encoder(get_cameras())


@router.get("/{camera_id}/preview")
async def preview(camera_id: int):
    camera = get_camera(camera_id)
    controller = get_camera_controller(camera)
    return Response(controller.preview(camera).read())


@router.get("/{camera_id}/photo")
async def photo(camera_id: int):
    camera = get_camera(camera_id)
    controller = get_camera_controller(camera)
    return Response(controller.photo(camera).read())
