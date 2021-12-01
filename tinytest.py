from machine import Pin, Timer
import time

red = Pin(18, Pin.OUT)
green = Pin(19, Pin.OUT)
blue = Pin(20, Pin.OUT)

timer = Timer()

def ledblink(timer):
    red.toggle()
    time.sleep(0.5)
            
    green.toggle()
    time.sleep(0.5)
    
    blue.toggle()
    time.sleep(0.5)

    

timer.init(freq=1000, mode=timer.PERIODIC, callback=ledblink)