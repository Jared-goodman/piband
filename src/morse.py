import os
from time import sleep

texttotranslate = raw_input()

alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

codes = [" ", ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----.", "-----"]

translated = []

for x in texttotranslate:
	translated.append(codes[alphabet.index(x.upper())])

for x in translated:
	for i in x:
		if i == ".":
			os.system("play /home/pi/piband/src/sounds/dit.wav")
		if i == "-":
			os.system("play /home/pi/piband/src/sounds/dah.wav")
		if i == " ":
			sleep(0.5)
		print i
	sleep(0.25)
