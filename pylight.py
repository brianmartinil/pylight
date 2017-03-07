import usb.core
import usb.util
import sys
from docopt import docopt

colors = ['off', 'blue', 'red', 'green', 'aqua', 'purple', 'yellow', 'white']

script = sys.argv[0]
valid_colors = ", ".join(colors)

help = '''
Set the color of LED email lights.

Usage:
  {0} <color>
  {0} --bus=<bus> --address=<address> <color>
  {0} --list
  {0} --help

Options:
  -b, --bus=<bus>         : set color based on the bus number
  -d, --address=<address> : set color based on the address number
  -l, --list              : list bus and address for connected lights
  -h, --help              : print this message
  
Valid colors: {1}
'''.format(script, valid_colors)


def match_all():
	return lambda d: True

def match_bus_addr(bus, addr):
	return lambda d: d.bus == bus and d.address == addr

def get_devices(matcher):
	return usb.core.find(find_all=True, custom_match=matcher, idVendor=0x1294, idProduct=0x1320)
	
# __main__	
args = docopt(help)
	
if args['--list']:
	print "BUS ADDRESS"
	print "--- -------"
	for device in get_devices(match_all()):
		print "{0:3d} {1:7d}".format(device.bus, device.address)
	sys.exit(0)
	
# Get command-line arguments
color_str = args['<color>'].lower()
address = args['--address']
bus = args['--bus']

# Validate colors
color_val = 0

try:
	color_val = colors.index(color_str)
except ValueError:
	print "Invalid color \"%s\"." % color_str
	print "Valid colors are: %s" % ", ".join(colors) 
	sys.exit(1)

# Decide what matcher function to use (all or bus/address)
matcher = match_all()
if (bus is not None):
	matcher = match_bus_addr(int(bus), int(address))

# Get the matched devices	
devices = usb.core.find(find_all=True, custom_match=matcher, idVendor=0x1294, idProduct=0x1320)

# Set the color on the matched devices
for device in devices:
	device.set_configuration()
	config = device.get_active_configuration()
	interface = config[(0,0)]
	ep = usb.util.find_descriptor(interface, custom_match = lambda e: usb.util.endpoint_direction(e.bEndpointAddress) == usb.util.ENDPOINT_OUT)
	ep.write(chr(color_val))
		

		