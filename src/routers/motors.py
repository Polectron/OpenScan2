from fastapi import APIRouter

from src.controllers.scanner import ScannerController
from src.controllers.motor import MotorController

router = APIRouter(
    prefix="/motors",
    tags=["motors"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def motors():
    motors = ScannerController.get_motors()
    return  motors


@router.get("/{motor_id}/move")
async def move(motor_id: int, angle: int):
    motor = ScannerController.get_motor(motor_id)
    MotorController.move(motor, angle)
