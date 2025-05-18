from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

# Initialises the sensors
ultrasonic_sensor = UltrasonicSensor(Port.S1)
touch_sensor = TouchSensor(Port.S2)

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

while True:
    # Touch sensor starts the program if it's pressed
    if touch_sensor.pressed():
        ev3.speaker.beep()
    
        # This is the robot's first turn on the bottom right corner
        robot.turn(-10)
        robot.turn(-10)
        robot.straight(180)
        robot.turn(-40)
        robot.turn(-42)

        # This is the robot going from the bottom right corner to the yellow block
        robot.straight(500)

        # If an object is 20cm away from the robot it will beep
        if ultrasonic_sensor.distance() > 200:
            ev3.speaker.beep

        # Turn to retrieve the red block
        robot.turn(-50)
        robot.turn(-50)

        # Top right to left, collects red block on the way
        robot.straight(440)

        # From top left to bottom left
        robot.turn(-45)
        robot.turn(-45)
        robot.turn(-20)
        robot.straight(520)

        # Turns and pushes blocks into start zone
        robot.turn(-100)
        robot.straight(40)#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

line_sensor = ColorSensor(Port.S3)

robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

DRIVE_SPEED = 100

PROPORTIONAL_GAIN = 1.2

while True:
    deviation = line_sensor.reflection() - threshold

    turn_rate = PROPORTIONAL_GAIN * deviation

    robot.drive(DRIVE_SPEED, turn_rate)

    wait(10)
