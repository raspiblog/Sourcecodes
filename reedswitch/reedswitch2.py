import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.OUT)
while True:
  if GPIO.input(14)==1:
    print("OFF!!")
    GPIO.output(15,True)
  else:
    print("ON!!")
    GPIO.output(15,False)
time.sleep(0.5)
