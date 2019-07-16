# Copyright (C) 2019
# Liam Charles (github: @1zc)
#
# Original Author: Tony DiCola for ADAFRUIT 2014
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


import math
import time
import Adafruit_GPIO.SPI as SPI # (C) Adafruit Industries (github @adafruit)
import SOLED
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

### Pin Configurations for the Raspberry Pi
RST = 24
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
############################################

#######################################################################################################
### DISPLAY SELECTION:
# 
# To select the correct display, uncomment
# your display resolution and comment 
# everything else.
#
# TO USE SH1106 DRIVERS INSTEAD OF SSD1306,
# REPLACE "R" WITH "S". 
# Eg: SOLED.R128x64(rst=RST) will become SOLED.S128x64(rst=RST)
#
# By default, 128x64 i2C has been uncommented
#

### 128x64 i2C Configuration ###
disp = SOLED.R128x64(rst=RST)

### 128x64 SPI Configuration ###
#disp = SOLED.R128x64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

### 128x32 i2C Configuration ###
#disp = SOLED.R128x32(rst=RST)

### 128x32 SPI Configuration ###
#disp = SOLED.R128x32(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

### 96x16 i2C Configuration ###
#disp = SOLED.R96x16(rst=RST)

### 96x16 SPI Configuration ###
#disp = SOLED.R96x16(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

### 64x48 i2C Configuration ###
#disp = SOLED.R64x48(rst=RST)

### 64x48 SPI Configuration ###
#disp = SOLED.R64x48(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))


# If your resolution is not listed here but is
# compatible with SOLED, uncomment and use the templates
# below for SPI or i2C.
#
# Replace `` with the Width of your resolution, and replace ** with
# the Height of your resolution.

#disp = SOLED.R``x**(rst=RST)
#disp = SOLED.R``x**(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000)) ### FOR SPI


#######################################################################################################


disp.begin()                # Start the display.
width = disp.width          # Fetches display width in pixels.
height = disp.height        # Fetches display height in pixels.
disp.clear()                # Clears the display buffer.
disp.display()              # Renders the contents of the display buffer on the display.

image = Image.new('1', (width, height))     # Creates new image to fit the dimensions of the screen.
font = ImageFont.load_default()             # Loading the default font to render text with.
draw = ImageDraw.Draw(image)                # Create a drawing object based on the image created above.

text = "Hello! This text is waveeeyyyy." # String of text which will be animated in a wave.
maxwidth, unused = draw.textsize(text, font=font) # get total width of the text.

# Set animation and sine wave parameters.
amplitude = height/4
offset = height/2 - 4
velocity = -2
startpos = width

# Animate text to move in a sine wave.
print('Press Ctrl-C to quit this example.')
pos = startpos

while True:
    # Clear image buffer by drawing a black filled box.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    # Enumerate characters and draw them offset vertically based on a sine wave.
    x = pos
    for i, c in enumerate(text):
        # Stop drawing if off the right side of screen.
        if x > width:
            break
        # Calculate width but skip drawing if off the left side of screen.
        if x < -10:
            char_width, char_height = draw.textsize(c, font=font)
            x += char_width
            continue
        # Calculate offset from sine wave.
        y = offset+math.floor(amplitude*math.sin(x/float(width)*2.0*math.pi))
        # Draw text.
        draw.text((x, y), c, font=font, fill=255)
        # Increment x position based on chacacter width.
        char_width, char_height = draw.textsize(c, font=font)
        x += char_width
    # Draw the image buffer.
    disp.image(image)
    disp.display()
    # Move position for next frame.
    pos += velocity
    # Start over if text has scrolled completely off left side of screen.
    if pos < -maxwidth:
        pos = startpos
    # Pause briefly before drawing next frame.
    time.sleep(0.1)
