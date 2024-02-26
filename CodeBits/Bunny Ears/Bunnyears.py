import time
import busio
import board
import adafruit_lis3dh
import pwmio
from adafruit_motor import servo

# Setup accelerometer
i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
sensor = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19)

# Setup servos
left_pwm = pwmio.PWMOut(board.A1, frequency=50)
right_pwm = pwmio.PWMOut(board.A3, frequency=50)

left_ear = servo.Servo(left_pwm)
right_ear = servo.Servo(right_pwm)

#initialize things
left_ear.angle = 0
right_ear.angle = 0

while True:
    x, _, _ = sensor.acceleration
    if x < -5.0:
        left_ear.angle = 90
    elif x > 5.0:
        right_ear.angle = 90
    elif abs(x) < 4.0:
        left_ear.angle = 0
        right_ear.angle = 0
    time.sleep(0.1)