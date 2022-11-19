import RPi.GPIO as GPIO
import time

sensor = 16
led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

GPIO.output(led,False)
print ("Water Sensor Ready.....")
print (" ")

try: 
   while True:
      if GPIO.input(sensor):
          GPIO.output(led,True)
          print ("Water Detected")          
	    while GPIO.input(sensor):
              time.sleep(0.2)
      else:
          GPIO.output(led,False)
	    print ("Water  Not Detected")

except KeyboardInterrupt:
    GPIO.cleanup()
