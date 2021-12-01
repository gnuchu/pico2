import tm1637
import machine

lcd1 = tm1637.TM1637(clk=Pin(0), dio=Pin(1))
lcd2 = tm1637.TM1637(clk=Pin(2), dio=Pin(3))


