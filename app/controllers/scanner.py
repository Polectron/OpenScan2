from app.models.motor import Motor
from app.config import config

try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO


class ScannerController:
    def get_motors() -> "list[Motor]":
        return []

    def get_motor(motor_id: id) -> Motor:
        return None

    def turn_light_on():
        GPIO.setup(config.scanner.ring_light_pin, GPIO.OUT)
        GPIO.output(config.scanner.ring_light_pin, True)

    def turn_light_off():
        GPIO.setup(config.scanner.ring_light_pin, GPIO.OUT)
        GPIO.output(config.scanner.ring_light_pin, False)
