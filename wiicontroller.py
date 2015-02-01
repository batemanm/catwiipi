#!/usr/bin/env python
# This is placed in the public domain, if it breaks you can keep both bits.
#
# Martin Bateman (mbateman@uclan.ac.uk)


import cwiid
import time
import scratch
import getopt
import sys
import threading

class ReceiveThread (threading.Thread):
	def run (self):
		while (True):
			message = s.receive ()
			broadcasts = message['broadcast']
			sensors = message['sensor-update']
			if 'rumble' in broadcasts:
				wm.rumble = 1
				time.sleep (2)
				wm.rumble = 0
			if 'leds' in sensors:
				if sensors['leds'] >= 0 & sensors['leds'] <= 16:
					wm.led = sensors['leds']


print ("Connecting to Scratch")
s = scratch.Scratch(host='192.168.2.1')
s.connect(poll=False)

print ("Press button 1 + 2 on your Wiimote.")
time.sleep(1)

s.sensorupdate ({"CLASSIC_L_STICK_MAX": cwiid.CLASSIC_L_STICK_MAX})
s.sensorupdate ({"CLASSIC_R_STICK_MAX": cwiid.CLASSIC_R_STICK_MAX})
s.sensorupdate ({"IR_X_MAX": cwiid.IR_X_MAX})
s.sensorupdate ({"IR_Y_MAX": cwiid.IR_Y_MAX})

wm=cwiid.Wiimote()
print ("Wiimote connected.")
time.sleep(1)

wm.rpt_mode = cwiid.RPT_BTN | cwiid.RPT_ACC | cwiid.RPT_NUNCHUK | cwiid.RPT_IR

print ("Now start the game")

sensors = {}
buttons = []

receiveThread = ReceiveThread ()
receiveThread.start ()

while (True):
	if wm.state['buttons'] & 2048:
		buttons.append("up")

        if wm.state['buttons'] & 256:
		buttons.append("left")

        if wm.state['buttons'] & 512:
		buttons.append("right")

        if wm.state['buttons'] & 1024:
		buttons.append("down")

        if wm.state['buttons'] & 8:
		buttons.append("a")

        if wm.state['buttons'] & 4:
		buttons.append("b")

        if wm.state['buttons'] & 1:
		buttons.append("2")

        if wm.state['buttons'] & 2:
		buttons.append("1")

        if wm.state['buttons'] & 16:
		buttons.append("minus")

        if wm.state['buttons'] & 4096:
		buttons.append("plus")

        if wm.state['buttons'] & 128:
		buttons.append("home")

	if "acc" in wm.state:
		sensors['x'] = wm.state['acc'][0]
		sensors['y'] = wm.state['acc'][1]
		sensors['z'] = wm.state['acc'][2]

	if "nunchuk" in wm.state:
		nunchuk = wm.state['nunchuk']
		if nunchuk['buttons'] & 1:
			buttons.append ("nunchuk_b1")
		if nunchuk['buttons'] & 2:
			buttons.append ("nunchuk_b2")
		sensors['nunchuk_x'] = nunchuk['acc'][0]
		sensors['nunchuk_y'] = nunchuk['acc'][1]
		sensors['nunchuk_z'] = nunchuk['acc'][2]
		sensors['stick_x'] = nunchuk['stick'][0]
		sensors['stick_y'] = nunchuk['stick'][1]

	if "ir_src" in wm.state:
		irstate = wm.state['ir_src']
		if irstate[0] != None:
			sensors['ir1x'] = irstate[0]['pos'][0]
			sensors['ir1y'] = irstate[0]['pos'][1]
		else:
			sensors['ir1x'] = -1
			sensors['ir1y'] = -1

	s.broadcast (buttons)
	del buttons[:]

	s.sensorupdate (sensors)
	sensors.clear ()

	time.sleep(.05)




