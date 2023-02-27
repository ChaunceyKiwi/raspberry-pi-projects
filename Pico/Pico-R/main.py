from machine import Pin
import time

ledG = Pin(11, Pin.OUT)
buttonG = Pin(10, Pin.IN, Pin.PULL_DOWN)
ledY = Pin(13, Pin.OUT)
buttonY = Pin(12, Pin.IN, Pin.PULL_DOWN)
ledR = Pin(15, Pin.OUT)
buttonR = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if buttonG.value():
        ledG.toggle()
        time.sleep(0.5)
    if buttonY.value():
        ledY.toggle()
        time.sleep(0.5)
    if buttonR.value():
        ledR.toggle()
        time.sleep(0.5)
    