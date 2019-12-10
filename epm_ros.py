import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Bool 

GPIO.setmode(GPIO.BOARD) # GPIO-Board pin config
GPIO.setup(12, GPIO.OUT)
pwm = GPIO.PWM(12, 50)
pwm.start(0.0)

def cleanup():
    pwm.stop()
    GPIO.cleanup()

def epm_cb(msg):
    print('cb')
    if(msg.data):
        pwm.ChangeDutyCycle(10.0)
        time.sleep(0.1)
        print('sent - 10 ')
    else:
        pwm.ChangeDutyCycle(5.0)
        time.sleep(0.1)
        print('sent -5 ')
        #pwm.ChangeDutyCycle(0.0)
#    pwm.ChangeDutyCycle(0.0)



rospy.spin()
