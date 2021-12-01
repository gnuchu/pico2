import tm1637
from machine import Pin
import time
import _thread

def button_pressed(event):
    if lock.locked():
        lock.release()
    else:
        lock.acquire()

button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
button.irq(handler=button_pressed, trigger=Pin.IRQ_RISING)    

def clock():
    lcd = tm1637.TM1637(clk=Pin(0), dio=Pin(1))    
    colon = True
    
    while True:
        if lock.locked():
            #button has been pressed
            print("yo, you pressed the button.")
            lock.release()
            
        local_t = time.localtime()
        print(local_t)
        hour = local_t[6]
        minute = local_t[4]
        
        lcd.numbers(hour, minute, colon)
        colon = not colon
        time.sleep(1)

if __name__ == '__main__':
    lock = _thread.allocate_lock()
    _thread.start_new_thread(clock(), ())
    clock()
