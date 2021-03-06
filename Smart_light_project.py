#smart light/led ( change and visulize brightness level)

import Rpi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #switch to increase brightness control 
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)  #switch1 to decrease brightness control 
pwm=GPIO.PWM(18,1000)
bright=1
pwm.start(0)                                    #initially light is off
 
iot_hub="demo.thingsboard.io"
port=1883
username="7nhpCJ2l6iZ5rEj1ghFN"
password=""
topic="v1/devices/me/telemetry"
client=mqtt.Client()
client.username_pw_set(username,password)
client.connect(iot_hub,port)
print("connection access")

data=dict()
while (1):
    if (GPIO.input(16))==0:
        bright=bright/2.             #to decrease brightness
        pwm.ChangeDutyCycle(bright) 
        print("your brightness is:",bright)
        data['gpio']='on'
            data['brightness']=bright
            data_out=json.dumps(data)
            client.publish(topic,data_out) #show status of brightness on dashboard
            time.sleep(0.25)            
    if (GPIO.input(12)==0):
        bright=bright*2              #to increase brightness
        if bright>100:
            bright=100
            print("full brightness")
        pwm.ChangeDutyCycle(bright)                
        print"your brightness is:",bright
        data['gpio']='on'
        data['brightness']=bright
        data_out=json.dumps(data)
        client.publish(topic,data_out)  #show status of brightness on dashboard
        time.sleep(0.25)
        
    

            


