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

timer = StopWatch()
timeout = 60 * 1000 # ms
interval = 0.1 * 1000 # ms

current_time = 0
previous_readout = 0
is_running = False

while current_time < timeout:
    distance = distance_sensor.distance()
    if distance < 100:
        if is_running:
            distance_sensor.lights.on(100)
            mvp.drive_motor.stop()
            is_running = False
    else:
        if not is_running:
            distance_sensor.lights.off()
            mvp.drive_motor.run(speed=800)
            is_running = True

    
    if current_time - previous_readout > interval:
        # to get all attributes of e.g. imu call dir(mvp.hub.imu)
        print('time: {} ms\n'.format(current_time),
              'distance: {} mm\n'.format(distance),
              'acceleration: {} m/s**2\n'.format(mvp.hub.imu.acceleration()),
              'angular_velocity: {} degree/s\n'.format(mvp.hub.imu.angular_velocity())
        )
        previous_readout = current_time

    current_time = timer.time()
