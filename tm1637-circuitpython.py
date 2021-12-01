import tm1637
import board
import digitalio
import microcontroller
import time

def button_handler(event):
    print("Button press being handled")

def button():
    button = digitalio.DigitalInOut(microcontroller.Pin(16))
    button.switch_to_input(pull=digitalio.Pull.UP)

def clock():
    lcd = tm1637.TM1637(clk=Pin(0), dio=Pin(1))

    colon = True

    while True:
        local_t = time.localtime()
        print(local_t)
        hour = local_t[6]
        minute = local_t[4]

        lcd.numbers(hour, minute, colon)
        colon = not colon
        time.sleep(1)

if __name__ == '__main__':
    lock = _thread.allocate_lock()
    button()
    _thread.start_new_thread(clock, ())
