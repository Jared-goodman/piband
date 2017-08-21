import os
from speech import say

def summon():
	print "Ok. Summoning cthulhu now..."
	say("Ok. Summoning Cuhtulu now...")
	os.system("aplay /home/pi/piband/src/sounds/cthulhu.wav")
	print "cthulhu successfuly summoned."
	say("Cuthulu successfuly summoned.")

