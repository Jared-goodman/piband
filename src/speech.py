from os import system

def say(text):
	system("pico2wave -w speech.wav \"" + text + "\" && play speech.wav")
