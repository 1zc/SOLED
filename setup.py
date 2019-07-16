import os
import io
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

classifiers = ['Development Status :: 3 - Alpha',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: MIT License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(name              = 'SOLED',
      version           = '1.0.1',
      author            = 'Liam Charles',
      author_email      = 'liamzcharles@gmail.com',
      description       = 'The SOLED (SSD1306 OLED) Engine is a library for the Raspberry Pi to use small SSD/SSH-driver OLED displays using the SPI/i2C bus.',
      long_description  = long_description,
      long_description_content_type="text/markdown",
      license           = 'MIT',
      classifiers       = classifiers,
      url               = 'https://github.com/1zc/SOLED',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.6.5'], ### Adafruit GPIO Package
      install_requires  = ['Adafruit-GPIO>=0.6.5'],
      packages          = find_packages()
      )