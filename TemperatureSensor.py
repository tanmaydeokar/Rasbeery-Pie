import Adafruit_DHT
import time 
import RP1.GPIO as GPIO
led-18 
sensor=16
GPIO.setmode (GPIO.BCM)
GPIO.setup(sensor,GPIO.IN) 
GPIO.setup(led, GPIO.OUT)
while True:
humidity, temperature = Adafruit_DHT.read_retry(11,16) 
print(temperature, humidity)
time.sleep(1)
if (humidity>50):
GPIO.input (sensor)
GPIO.output (led, True)
else:
GPIO.output (led,False)
