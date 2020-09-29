import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
  if GPIO.input(14)==1:
    print("OFF!!")
  else:
    print("ON!!")
  time.sleep(0.5)
