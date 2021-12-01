# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 10
LCD_D5 = 11
LCD_D6 = 12
LCD_D7 = 13
LED_ON = 15

# Define some device constants
LCD_WIDTH = 20    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line
LCD_LINE_3 = 0x94 # LCD RAM address for the 3rd line
LCD_LINE_4 = 0xD4 # LCD RAM address for the 4th line

# Timing constants
E_PULSE = 0.0005
E_DELAY = 0.0005

class Justifiication(enum):
  LEFT = 1
  CENTERED = 2
  RIGHT = 3
