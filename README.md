# [SOLED](https://github.com/1zc/SOLED)
SOLED is a python-based library that can be used to operate various monochrome SSD/SSH-driver OLED displays with a Raspberry Pi.

A list of all display modules SOLED is currently compatible is available below.

 
### Setup

SOLED is fairly simple to install.

First, perform a simple update.
> sudo apt -y update && sudo apt -y upgrade

Next, we can begin setting up some dependencies by:
> sudo python -m pip install --upgrade pip setuptools wheel

Finally, we install SOLED using:
> git clone https://github.com/1zc/SOLED.git && cd SOLED && sudo python setup.py install

### List of Compatible Display Modules

This list can also be found in DISPLAYS.txt
If a display module is marked compatible, it applies for both i2C and SPI variants.

Module | Resolution | Compatibility | Status
------------ | ------------- | ------------- | -------------
SSD1306 | 128x64 | ✔️ Compatible | ✔️ Tested
SSD1306 | 128x32 | ✔️ Compatible | ✔️ Tested
SSD1306 | 96x16 | ✔️ Compatible | ☀️ Not Tested
SSD1306 | 96x48 | ✔️ Compatible | ✔️ Tested
SSD1306 | 64x48 | ✔️ Compatible | ☀️ Not Tested
SSD1306 | 64x32 | ❌ Incompatible | 🔄 Will be added soon
SSD1306 | 72x40 | ❌ Incompatible | 🔄 Will be added soon
SSD1306 | 96x64 | ❌ Incompatible | 🔄 Will be added soon
SSD1306 | 128x128 | ❌ Incompatible | 🔄 Will be added soon
// | // | // | //
SSH1106 | 128x64 | ✔️ Compatible | 🌐 In dev. Please create an issue if there are any problems!
// | // | // | //
SSD1351 | 128x64 | ❌ Incompatible | 🌐 In dev.
SSD1351 | 128x32 | ❌ Incompatible | 🌐 In dev.