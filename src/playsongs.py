import os, sys
import glob
from threading import Thread
from gpiozero import Button
from random import shuffle

def waitforpress():
	button = Button(13)
	button.wait_for_press()
	print("Button pressed! Stopping songs...")


def playSongs():
	songs = []
	for file in glob.glob("/home/pi/piband/src/*.mp3"):
		songs.append(file)
	
	for file in glob.glob("/home/pi/piband/src/*.wav"):
		songs.append(file)
	
	shuffle(songs)
	
	for x in songs:
		os.system("play \"" + x + "\"")

thread = Thread(target = playSongs, args = ())
thread.daemon = False
thread.start()
#waitforpress()

sys.exit()
