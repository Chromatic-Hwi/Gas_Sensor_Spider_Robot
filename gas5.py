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
        if ((FA==False)&(FB==False)):
            result_f = "Clean Air"
        elif ((FA==True)&(FB==False)):
            result_f = "Low Level Gas"
        elif ((FA==True)&(FB==True)):
            result_f = "High Level Gas"
    return result_f

    def left_sensor_gas(LA, LB):
        global result_l
        if ((LA==False)&(LB==False)):
            result_l = "Clean Air"
        elif ((LA==True)&(LB==False)):
            result_l = "Low Level Gas"
        elif ((LA==True)&(LB==True)):
            result_l = "High Level Gas"
    return result_l

    def right_sensor_gas(RA, RB):
        global result_r
        if ((RA==False)&(RB==False)):
            result_r = "Clean Air"
        elif ((RA==True)&(RB==False)):
            result_r = "Low Level Gas"
        elif ((RA==True)&(RB==True)):
            result_r = "High Level Gas"
    return result_r

    def back_sensor_gas(BA, BB):
        global result_b
        if ((BA==False)&(BB==False)):
            result_b = "Clean Air"
        elif ((BA==True)&(BB==False)):
            result_b = "Low Level Gas"
        elif ((BA==True)&(BB==True)):
            result_b = "High Level Gas"
    return result_b

    print("Front side =>", front_sensor_gas(FA, FB))
    print("Left side  =>", left_sensor_gas(LA, LB))
    print("Right side =>", right_sensor_gas(RA, RB))
    print("Back side  =>", back_sensor_gas(BA, BB))


try:
    while True:
        sensor_func((GPIO.input(23)), (GPIO.input(24)), (GPIO.input(27)), (GPIO.input(22)), (GPIO.input(20)), (GPIO.input(21)), (GPIO.input(19)), (GPIO.input(26)))
        
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
            GPIO.output(12, True) #buzzer
"""
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
