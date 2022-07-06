from time import sleep
from math import cos

from src.models.motor import Motor

try:
    import RPi.GPIO as GPIO
except:
    import Mock.GPIO as GPIO


class MotorController:
    def move(motor: Motor, angle: int):
        step_count = (
            int(angle * motor.settings.steps_per_rotation / 360)
            * motor.settings.direction
        )
        delay = motor.settings.delay

        GPIO.setup(motor.settings.direction_pin, GPIO.OUT)
        GPIO.setup(motor.settings.step_pin, GPIO.OUT)
        if step_count > 0:
            GPIO.output(motor.settings.direction_pin, GPIO.HIGH)
        if step_count < 0:
            GPIO.output(motor.settings.direction_pin, GPIO.LOW)
            step_count = -step_count
        for x in range(step_count):
            GPIO.output(motor.settings.step_pin, GPIO.HIGH)
            if x <= motor.settings.acceleration_ramp and x <= step_count / 2:
                delay = motor.settings.delay * (
                    1
                    + -1
                    / motor.settings.acceleration
                    * cos(
                        1
                        * (motor.settings.acceleration_ramp - x)
                        / motor.settings.acceleration_ramp
                    )
                    + 1 / motor.settings.acceleration
                )
                # delay=delay_init+(ramp-x)*(delay_init)/acc
            elif (
                step_count - x <= motor.settings.acceleration_ramp
                and x > step_count / 2
            ):
                delay = motor.settings.delay * (
                    1
                    - 1
                    / motor.settings.acceleration
                    * cos(
                        1
                        * (motor.settings.acceleration_ramp + x - step_count)
                        / motor.settings.acceleration_ramp
                    )
                    + 1 / motor.settings.acceleration
                )
                # delay=delay_init+(ramp-step_count+x)*(delay_init)/acc
            else:
                delay = motor.settings.delay
            sleep(delay)
            GPIO.output(motor.settings.step_pin, GPIO.LOW)
            sleep(delay)

    def get_points(samples=1):
        from math import pi, sqrt, acos, atan2, cos, sin

        points = []
        phi = pi * (3.0 - sqrt(5.0))
        for i in range(int(samples)):
            y = 1 - (i / float(samples - 1)) * 2
            radius = sqrt(1 - y * y)
            theta = phi * i
            x = cos(theta) * radius
            z = sin(theta) * radius
            r = sqrt(x * x + y * y + z * z)
            theta_neu = acos(z / r) * 180 / pi
            phi_neu = atan2(y, x) * 180 / pi
            points.append((theta_neu - 90, phi_neu))
        points.sort()
        return points

    def create_coordinates(angle_min, angle_max, point_count):
        point_count_final = point_count
        if angle_max < angle_min:
            a = angle_min
            angle_min = angle_max
            angle_max = a
        point_count = point_count * 90 / (angle_max - angle_min)
        actual_points = 0
        while actual_points < point_count_final:
            points = MotorController.get_points(point_count)
            filtered = []
            for x, y in points:
                if (
                    x > angle_min
                    and x < angle_max
                    and len(filtered) < point_count_final
                ):
                    filtered.append((x, y))
            actual_points = len(filtered)

            if point_count - actual_points > 20:
                point_count = point_count + 3
            else:
                point_count = point_count + 1
        return filtered
