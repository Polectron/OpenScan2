from typing import Optional, Union
from time import time

from PIL import Image
import gphoto2 as gp
from fastapi import FastAPI

try:
    # checks if you have access to RPi.GPIO, which is available inside RPi
    import RPi.GPIO as GPIO
except:
    # In case of exception, you are executing your script outside of RPi, so import Mock.GPIO
    import Mock.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
