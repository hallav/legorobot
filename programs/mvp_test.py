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
from pybricks.hubs import InventorHub


class MVP:
    def __init__(self):
        self.steer_motor = Motor(Port.A)
        self.drive_motor = Motor(Port.B,
                                 positive_direction=Direction.COUNTERCLOCKWISE)
        self.hub = InventorHub()

    def calibrate(self):
        self.steer_motor.run_target(speed=1000, target_angle=-20)


# Initialize mvp and straighten its steering.
mvp = MVP()
mvp.calibrate()

distance_sensor = UltrasonicSensor(Port.E)

# Make mvp drive in a circle.
mvp.steer_motor.run_angle(speed=350, rotation_angle=-50)
mvp.drive_motor.run(speed=800) #, rotation_angle=32 * 360)

timer_timeout = StopWatch()
timeout = 30 * 1000 # ms

timer_data = StopWatch()
interval = 0.1 * 1000 # ms

while timer_timeout.time() < timeout:
    if distance_sensor.distance() < 100:
        distance_sensor.lights.on(100)
        mvp.drive_motor.stop()
    else:
        distance_sensor.lights.off()
        mvp.drive_motor.run(speed=800)

    dtime = timer_data.time() 
    if dtime > interval:
        print('delta_time:', dtime, 'ms')
        timer_data.reset()
        print('distance:', distance_sensor.distance(), 'mm')
        print('acceleration:', mvp.hub.imu.acceleration(), 'm/s**2')
