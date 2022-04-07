import time
import RPi.GPIO as GPIO
import random
import os
GPIO.setmode(GPIO.BCM)
time.time()
GPIO.setwarnings(False)

#=============GPIO PIN Settings==========================

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

#LED OUTPUT
GPIO.setup(5, GPIO.OUT)  #Green
GPIO.setup(6, GPIO.OUT)  #Yellow
GPIO.setup(13, GPIO.OUT) #Red

#Buzzer Output
GPIO.setup(12, GPIO.OUT)

result_f = ""
result_l = ""
result_r = ""
result_b = ""

#=================Function Define=========================

def front_sensor_gas(FA, FB):
    global result_f
    if ((FA==0)&(FB==0)):
        result_f = random.randrange(0,10)
    elif ((FA==0)&(FB==1)):
        result_f = random.randrange(700,720)
    elif ((FA==1)&(FB==0)):
        result_f = random.randrange(1500,1700)
    elif ((FA==1)&(FB==1)):
        result_f = random.randrange(2000,2200)
    return result_f

def left_sensor_gas(LA, LB):
    global result_l
    if ((LA==0)&(LB==0)):
        result_l = random.randrange(0,10)
    elif ((LA==0)&(LB==1)):
        result_l = random.randrange(700,720)
    elif ((LA==1)&(LB==0)):
        result_l = random.randrange(1500,1700)
    elif ((LA==1)&(LB==1)):
        result_l = random.randrange(2000,2200)
    return result_l

def right_sensor_gas(RA, RB):
    global result_r
    if ((RA==0)&(RB==0)):
        result_r = random.randrange(0,10)
    elif ((RA==0)&(RB==1)):
        result_r = random.randrange(700,720)
    elif ((RA==1)&(RB==0)):
        result_r = random.randrange(1500,1700)
    elif ((RA==1)&(RB==1)):
        result_r = random.randrange(2000,2200)
    return result_r

def back_sensor_gas(BA, BB):
    global result_b
    if ((BA==0)&(BB==0)):
        result_b = random.randrange(0,10)
    elif ((BA==0)&(BB==1)):
        result_b = random.randrange(700,720)
    elif ((BA==1)&(BB==0)):
        result_b = random.randrange(1500,1700)
    elif ((BA==1)&(BB==1)):
        result_b = random.randrange(2000,2200)
    return result_b

def insert_db(d_m, f_m, l_m, r_m, b_m):
    d_m=700
    curl -X POST 'http://127.0.0.1:8086/write?db=gasdb&u=gasadmin&p=gasadmin' --data-binary gasdb,host=spider default_m=d_m
    gasdb,host=spider front_m=front_sensor_gas
    gasdb,host=spider left_m=left_sensor_gas
    gasdb,host=spider right_m=right_sensor_gas
    gasdb,host=spider back_m=back_sensor_gas
    return true

"""def db_update(default_m):
    os.system("default : ", default_m)
    #/curl -X POST 'http://127.0.0.1:8086/write?db=gasdb&u=gasadmin&p=gasadmin' --data-binary "gasdb,host=drone default_m=$d_m
    #/gasdb,host=spidergas front_m=$random_f
    #/gasdb,host=spidergas rear_m=$random_r"
    return true """
#==========================================================

try:
    while True:
        print(time.strftime('%y/%m/%d - %H:%M:%S'))
        
        FA = (GPIO.input(23))
        FB = (GPIO.input(24))
        LA = (GPIO.input(27))
        LB = (GPIO.input(22))
        RA = (GPIO.input(20))
        RB = (GPIO.input(21))
        BA = (GPIO.input(19))
        BB = (GPIO.input(26))
        
        """default_m=700
        front_m=(front_sensor_gas(FA, FB))
        left_m=(left_sensor_gas(LA, LB))
        right_m=(right_sensor_gas(RA, RB))
        back_m=(back_sensor_gas(BA, BB))
        
        db_update(default_m)"""
        
        print(front_sensor_gas(FA, FB)) #front
        print(left_sensor_gas(LA, LB))  #left
        print(right_sensor_gas(RA, RB)) #right
        print(back_sensor_gas(BA, BB))  #back
        print()
        
        if ((GPIO.input(23)==False)&(GPIO.input(24)==False)):
            GPIO.output(5, True)
            GPIO.output(6, False)
            GPIO.output(13, False)     
            GPIO.output(12, False)
            
        elif ((GPIO.input(23)==True)&(GPIO.input(24)==False)):
            GPIO.output(5, False)
            GPIO.output(6, True)
            GPIO.output(13, False)
            GPIO.output(12, False)

        elif ((GPIO.input(23)==True)&(GPIO.input(24)==True)):
            GPIO.output(5, False)
            GPIO.output(6, False)
            GPIO.output(13, True)
            GPIO.output(12, True)
            
        
        time.sleep(1.0)


        
        
except KeyboardInterrupt:
    print("Keyboard Interrupt")
    
except:
    #pass
    print("Wrong key, Some error")
        
finally:
    print("Clean Up")
    GPIO.cleanup()
