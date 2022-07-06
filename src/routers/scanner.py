from fastapi import APIRouter

from src.controllers.scanner import ScannerController

router = APIRouter(
    prefix="/scanner",
    tags=["scanner"],
    responses={404: {"description": "Not found"}},
)


@router.get("/ringlight/on")
async def ringlight_on():
    ScannerController.turn_light_on()


@router.get("/ringlight/off")
async def ringlight_off():
    ScannerController.turn_light_off()
