"""
This program is for MVP's basic "Buggy" mode.
Follow the corresponding building instructions in the LEGO® MINDSTORMS®
Robot Inventor App.

Original script in pybricks-projects:
sets/mindstorms-robot-inventor/main-models/mvp/mvp-basic.py
"""

from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Direction, Port
from pybricks.tools import wait, StopWatch


class MVP:
    def __init__(self):
        self.steer_motor = Motor(Port.A)
        self.drive_motor = Motor(Port.B,
                                 positive_direction=Direction.COUNTERCLOCKWISE)

    def calibrate(self):
        self.steer_motor.run_target(speed=1000, target_angle=-20)


# Initialize mvp and straighten its steering.
mvp = MVP()
mvp.calibrate()

distance_sensor = UltrasonicSensor(Port.E)

# Make mvp drive in a circle.
mvp.steer_motor.run_angle(speed=350, rotation_angle=-50)
mvp.drive_motor.run(speed=800) #, rotation_angle=32 * 360)

timer = StopWatch()
timeout = 30 * 1000 # ms

while timer.time() < timeout:
    if distance_sensor.distance() < 100:
        distance_sensor.lights.on(100)
        mvp.drive_motor.stop()
    else:
        distance_sensor.lights.off()
        mvp.drive_motor.run(speed=800)
