import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
#GPIO.cleanup()

#Front sensor
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Left sensor
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Right sensor
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Back sensor
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
#LED OUTPUT
GPIO.setup(5, GPIO.OUT)  #Green
GPIO.setup(6, GPIO.OUT)  #Yellow
GPIO.setup(13, GPIO.OUT) #Red

#Buzzer Output
GPIO.setup(12, GPIO.OUT)
"""
result_f = ""
result_l = ""
result_r = ""
result_b = ""

def sensor_func(FA, FB, LA, LB, RA, RB, BA, BB):
    def front_sensor_gas(FA, FB):
        global result_f
        if ((FA==0)&(FB==0)):
            result_f = "Clean Air"
        elif ((FA==1)&(FB==0)):
            result_f = "Low Level Gas"
        elif ((FA==1)&(FB==1)):
            result_f = "High Level Gas"
    return result_f

    def left_sensor_gas(LA, LB):
        global result_l
        if ((LA==0)&(LB==0)):
            result_l = "Clean Air"
        elif ((LA==1)&(LB==0)):
            result_l = "Low Level Gas"
        elif ((LA==1)&(LB==1)):
            result_l = "High Level Gas"
    return result_l

    def right_sensor_gas(RA, RB):
        global result_r
        if ((RA==0)&(RB==0)):
            result_r = "Clean Air"
        elif ((RA==1)&(RB==0)):
            result_r = "Low Level Gas"
        elif ((RA==1)&(RB==1)):
            result_r = "High Level Gas"
    return result_r

    def back_sensor_gas(BA, BB):
        global result_b
        if ((BA==0)&(BB==0)):
            result_b = "Clean Air"
        elif ((BA==1)&(BB==0)):
            result_b = "Low Level Gas"
        elif ((BA==1)&(BB==1)):
            result_b = "High Level Gas"
    return result_b

    front_sensor_gas(FA, FB)
    left_sensor_gas(LA, LB)
    right_sensor_gas(RA, RB)
    back_sensor_gas(BA, BB)
    
    print("Front side =>", front_sensor_gas(FA, FB))
    print("Left side  =>", left_sensor_gas(LA, LB))
    print("Right side =>", right_sensor_gas(RA, RB))
    print("Back side  =>", back_sensor_gas(BA, BB))


try:
    while True:
        FA = (GPIO.input(23))
        FB = (GPIO.input(24))
        LA = (GPIO.input(27))
        LB = (GPIO.input(22))
        RA = (GPIO.input(20))
        RB = (GPIO.input(21))
        BA = (GPIO.input(19))
        BB = (GPIO.input(26))
        sensor_func(FA, FB, LA, LB, RA, RB, BA, BB)
        
        """if ((GPIO.input(23)==False)&(GPIO.input(24)==False)):
            GPIO.output(5, True)
            GPIO.output(6, False)
            GPIO.output(13, False)
        elif ((GPIO.input(23)==True)&(GPIO.input(24)==False)):
            GPIO.output(5, False)
            GPIO.output(6, True)
            GPIO.output(13, False)
        elif ((GPIO.input(23)==True)&(GPIO.input(24)==True)):
            GPIO.output(5, False)
            GPIO.output(6, False)
            GPIO.output(13, True)
            GPIO.output(12, True) #buzzer"""
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
