This is a repository to store/update progams for the Slide Randomizer user interface.

The entire application is run through pythons tool: 'Tkinter'.

The file Page_Integration_Test.py is the parent file, all other files are children to this file. Running this file runs the entire application (the pathologist testing interface).

The file test.py is used if the application is not being run on a Raspberry Pi. The class "Test" outputs which LEDs are turnign on and off in the command window.

The GPIO expander bonnets that are used on the raspberry pi use a library called "IOPi". This library mst be installed on the raspberry pi prior to running the application with the raspberry pi. The IOPi libraries can be found here: https://github.com/abelectronicsuk/ABElectronics_Python_Libraries
The steps to install the libraries are located here:https://www.abelectronics.co.uk/kb/article/23/python-library-and-demos

You will also need to enable to I2C pins on the raspberry Pi to use the GPIO expander bonnets. The steps to enabling the I2C pins on a raspberyy Pi can be found here: https://www.abelectronics.co.uk/kb/article/1/i2c--smbus-and-raspbian-linux

No further intallations are needed.

Once the I2C pins on the raspberry pi are enabled and the IOPi libraries have been installed on the raspberry pi, the application will run on the raspberry pi through the Page_Integration_Test.py file.
