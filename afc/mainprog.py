import FourLineDisplay
import constants

display = FourLineDisplay.Display()

# Send some centred test
display.lcd_string("--------------------", constants.LCD_LINE_1, constants.Justification.CENTRED)
display.lcd_string("John Pi", constants.LCD_LINE_2, constants.Justification.CENTRED)
display.lcd_string("Model B", constants.LCD_LINE_3, constants.Justification.CENTRED)
display.lcd_string("--------------------", constants.LCD_LINE_4, constants.Justification.CENTRED)

#   while True:
 
#     # Send some centred test
#     lcd_string("--------------------",LCD_LINE_1,2)
#     lcd_string("Rasbperry Pi",LCD_LINE_2,2)
#     lcd_string("Model B",LCD_LINE_3,2)
#     lcd_string("--------------------",LCD_LINE_4,2)
 
#     time.sleep(3) # 3 second delay
 
#     lcd_string("Raspberrypi-spy",LCD_LINE_1,3)
#     lcd_string(".co.uk",LCD_LINE_2,3)
#     lcd_string("",LCD_LINE_3,2)
#     lcd_string("20x4 LCD Module Test",LCD_LINE_4,2)
 
#     time.sleep(3) # 20 second delay
 
#     # Blank display
#     lcd_byte(0x01, LCD_CMD)
 
#     time.sleep(3) # 3 second delay