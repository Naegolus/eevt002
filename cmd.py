#!/usr/bin/python
#
# eevidtron example code (youtube.com/eevidtron)
# written by Clifford Wolf (www.clifford.at)
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

# boilerplate code
from __future__ import division
from __future__ import print_function

# used standard libraries
import readline
import sys

# import device drivers
from vxi11Device import Vxi11Device
from usbtmcDevice import UsbtmcDevice

# check arguments
if len(sys.argv) != 2:
    print('Usage: %s <cmd>', file=sys.stderr)
    exit(1)

# open VXI-11 connection, if requested by user
#if sys.argv[1] == 'vxi11':
#    dev = Vxi11Device(sys.argv[2], 'inst0')

# open USBTMC connection, if requested by user
#if sys.argv[1] == 'usbtmc':
#    dev = UsbtmcDevice(sys.argv[2])

dev = UsbtmcDevice('/dev/usbtmc0')

# read and execute commands
cmd = sys.argv[1]
if cmd.find('?') >= 0:
	answer = dev.ask(cmd).strip()
	print(answer)
else:
	dev.write(cmd)
