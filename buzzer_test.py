import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(12, GPIO.OUT)

try:
    while True:
        GPIO.output(12, True)
        time.sleep(0.5)
    
except KeyboardInterrupt:
    GPIO.cleanup()