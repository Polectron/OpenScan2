from fastapi import APIRouter

from src.controllers.cameras.cameras import get_cameras

router = APIRouter(
    prefix="/cameras",
    tags=["cameras"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def cameras():
    return {"cameras": get_cameras()}

@router.get("/{camera_id}/preview")
async def preview(camera_id: str):
    ...

@router.get("/{camera_id}/photo")
async def preview(camera_id: str):
    ...