import RPi.GPIO as GPIO
import time
import constants


class Display():
  def __init__(self):
    # Main program block
 
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
    GPIO.setup(constants.LCD_E, GPIO.OUT)  # E
    GPIO.setup(constants.LCD_RS, GPIO.OUT) # RS
    GPIO.setup(constants.LCD_D4, GPIO.OUT) # DB4
    GPIO.setup(constants.LCD_D5, GPIO.OUT) # DB5
    GPIO.setup(constants.LCD_D6, GPIO.OUT) # DB6
    GPIO.setup(constants.LCD_D7, GPIO.OUT) # DB7
    GPIO.setup(constants.LED_ON, GPIO.OUT) # Backlight enable
 
    # Initialise display
    self.lcd_init()
  
  def lcd_init(self):
    # Initialise display
    self.lcd_byte(0x33,constants.LCD_CMD) # 110011 Initialise
    self.lcd_byte(0x32,constants.LCD_CMD) # 110010 Initialise
    self.lcd_byte(0x06,constants.LCD_CMD) # 000110 Cursor move direction
    self.lcd_byte(0x0C,constants.LCD_CMD) # 001100 Display On,Cursor Off, Blink Off
    self.lcd_byte(0x28,constants.LCD_CMD) # 101000 Data length, number of lines, font size
    self.lcd_byte(0x01,constants.LCD_CMD) # 000001 Clear display
    time.sleep(constants.E_DELAY)
 
  def lcd_byte(self, bits, mode):
    # Send byte to data pins
    # bits = data
    # mode = True  for character
    #        False for command
  
    GPIO.output(constants.LCD_RS, mode) # RS
  
    # High bits
    GPIO.output(constants.LCD_D4, False)
    GPIO.output(constants.LCD_D5, False)
    GPIO.output(constants.LCD_D6, False)
    GPIO.output(constants.LCD_D7, False)
    if bits&0x10==0x10:
      GPIO.output(constants.LCD_D4, True)
    if bits&0x20==0x20:
      GPIO.output(constants.LCD_D5, True)
    if bits&0x40==0x40:
      GPIO.output(constants.LCD_D6, True)
    if bits&0x80==0x80:
      GPIO.output(constants.LCD_D7, True)
  
    # Toggle 'Enable' pin
    self.lcd_toggle_enable()
  
    # Low bits
    GPIO.output(constants.LCD_D4, False)
    GPIO.output(constants.LCD_D5, False)
    GPIO.output(constants.LCD_D6, False)
    GPIO.output(constants.LCD_D7, False)
    if bits&0x01==0x01:
      GPIO.output(constants.LCD_D4, True)
    if bits&0x02==0x02:
      GPIO.output(constants.LCD_D5, True)
    if bits&0x04==0x04:
      GPIO.output(constants.LCD_D6, True)
    if bits&0x08==0x08:
      GPIO.output(constants.LCD_D7, True)
  
    # Toggle 'Enable' pin
    self.lcd_toggle_enable()
 
  def lcd_toggle_enable(self):
    # Toggle enable
    time.sleep(constants.E_DELAY)
    GPIO.output(constants.LCD_E, True)
    time.sleep(constants.E_PULSE)
    GPIO.output(constants.LCD_E, False)
    time.sleep(constants.E_DELAY)
 
  def lcd_string(self, message,line,style):
    # Send string to display
    # style=1 Left justified
    # style=2 Centred
    # style=3 Right justified
  
    if style==1:
      message = message.ljust(constants.LCD_WIDTH," ")
    elif style==2:
      message = message.center(constants.LCD_WIDTH," ")
    elif style==3:
      message = message.rjust(constants.LCD_WIDTH," ")
  
    self.lcd_byte(line,constants.LCD_CMD)
  
    for i in range(constants.LCD_WIDTH):
      self.lcd_byte(ord(message[i]),constants.LCD_CHR)
 
  def lcd_backlight(self, flag):
    # Toggle backlight on-off-on
    GPIO.output(constants.LED_ON, flag)