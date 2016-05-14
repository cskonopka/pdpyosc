import logging
import sys
import time
import OSC
import os

startup = 1
# Init OSC
client = OSC.OSCClient()
client.connect(('127.0.0.1', 7001)) # first argument is the IP of the host, second argument is the port to use

print ("python program started")
while startup == 1:
	for num in range(10, 200):
		client.send(OSC.OSCMessage("/heading", num))	