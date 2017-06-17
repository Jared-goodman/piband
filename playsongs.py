import os
import glob
from random import shuffle

songs = []
for file in glob.glob("*.mp3"):
	songs.append(file)

for file in glob.glob("*.wav"):
	songs.append(file)

shuffle(songs)

for x in songs:
	os.system("aplay " + x)
