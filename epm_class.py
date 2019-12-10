import RPi.GPIO as GPIO
import time

# Pin Definitions
output_pin = 18  # BOARD pin 12, BCM pin 18

GPIO.setmode(GPIO.BCM)
#GPIO.setup(output_pin, GPIO.OUT, initial=GPIO.HIGH)

def epm(input):
	
	if(input == True):

		try:
			curr_value = GPIO.HIGH
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(output_pin, GPIO.OUT)
			GPIO.output(output_pin, curr_value)
			time.sleep(0.002)
			GPIO.output(output_pin, GPIO.LOW)
			print("Hi Master..!! EPM_PIN-(BCM)18 is High Now ")
		except Exception as e:
			print('exception at high_epm',e)

	elif(input == False):

		try:
			curr_value = GPIO.HIGH
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(output_pin, GPIO.OUT)
			GPIO.output(output_pin, curr_value)
			time.sleep(0.001)
			GPIO.output(output_pin, GPIO.LOW)
			print("Hi Master..!! EPM_PIN-(BCM)18 is Low Now ")
		except Exception as e:
			print('exception at low_epm',e)
			
			
def gpio_clean():

	print('gpio-cleaned')
	
	GPIO.cleanup()			
