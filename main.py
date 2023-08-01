"""
    Acknowledgement
    https://dev.to/ranewallin/getting-started-with-the-waveshare-2-7-epaper-hat-on-raspberry-pi-41m8
"""
import sys    
import os                                # import sys
libdir = os.path.join("/home/pi/Python_workspace/e-Paper/RaspberryPi_JetsonNano/python/lib")                   # add the lib folder to sys so python can find the libraries
if os.path.exists(libdir):
    sys.path.append(libdir)
from waveshare_epd import epd2in7
#import epd2in7                               # import the display drivers
from PIL import Image,ImageDraw,ImageFont     # import the image libraries
import time                                      
from gpiozero import Button                   # import the Button control from gpiozero

btn1 = Button(5)                              # assign each button to a variable
btn2 = Button(6)                              # by passing in the pin number
btn3 = Button(13)                             # associated with the button
btn4 = Button(19)                             # 

epd = epd2in7.EPD()                          # get the display object and assing to epd
epd.init()                                    # initialize the display
print("Clear...")                             # print message to console (not display) for debugging
epd.Clear(0xFF)                               # clear the display

# Print a message to the screen
# @params string 
def printToDisplay(string):
    """
    # Drawing on the Horizontal image. We must create an image object for both the black layer
    # and the red layer, even if we are only printing to one layer
    HBlackImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*126
    HRedImage = Image.new('1', (epd2in7.EPD_HEIGHT, epd2in7.EPD_WIDTH), 255)  # 298*126

    # create a draw object and the font object we will use for the display
    draw = ImageDraw.Draw(HBlackImage)
    font = ImageFont.truetype('/usr/share/fonts/truetype/google/Bangers-Regular.ttf', 30)

    # draw the text to the display. First argument is starting location of the text in pixels
    draw.text((25, 65), string, font = font, fill = 0)
    
    # Add the images to the display. Both the black and red layers need to be passed in, even
    # if we did not add anything to one of them
    epd.display(epd.getbuffer(HBlackImage), epd.getbuffer(HRedImage))
    """
    print(f"Button get press {string}")
# Handle button presses
# param Button (passed from when_pressed)
def handleBtnPress(btn):
    
    # get the button pin number
    pinNum = btn.pin.number
    
    # python hack for a switch statement. The number represents the pin number and
    # the value is the message we will print
    switcher = {
        5: "5, Hello, World!",
        6: "6, This is my first \nRPi project.",
        13: "13, Hope you liked it.",
        19: "19, Goodbye"
    }
    
    # get the string based on the passed in button and send it to printToDisplay()
    msg = switcher.get(btn.pin.number, "Error")
    printToDisplay(msg)
    
# tell the button what to do when pressed
btn1.when_pressed = handleBtnPress
btn2.when_pressed = handleBtnPress
btn3.when_pressed = handleBtnPress
btn4.when_pressed = handleBtnPress
"""
while True:
    time.sleep(1)
"""
from signal import pause
pause()