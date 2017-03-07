# pylight
This script drives USB "webmail notifiers".  These all seem to have a USB vendor id of `0x1294` and product id of `0x1320`.  There are [many scripts like it](https://www.google.com/search?q=0x1294+0x1320) but this one is mine.

## Installation
pylight requires the `docopt` and `pyusb` modules, plus an appropriate USB backend on your system.  On Windows I kind of just flailed around until the USB stuff worked.  I think most of it came down to using `inf-wizard` from [libusb-win32](https://sourceforge.net/p/libusb-win32/wiki/Home/) to register `libusb` as the device driver for the notifer.  I have also heard that [Zadig](http://zadig.akeo.ie/) might be better or easier?  I dunno, I somehow got it working and I'm afraid it'll break if I touch it.

## Usage
You can get usage by running `./pylight.py --help`.  By default all connected notifiers will change to the selected color, but you can also use command line options to select a specific notifer.

## Bugs, etc.
Feel free to open issues and pull requests with bugs / improvements.
