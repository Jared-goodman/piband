import os, sys, subprocess
import glob
from threading import Thread
from gpiozero import Button
from random import shuffle


button = Button(13)
def playSongs():
	songs = []
	for file in glob.glob("music/*.mp3"):
		songs.append(file)
	
	for file in glob.glob("music/*.wav"):
		songs.append(file)
	
	shuffle(songs)
	print songs	
	for x in songs:
		print x
		os.system("play \"" + x + "\"")

playSongs()

