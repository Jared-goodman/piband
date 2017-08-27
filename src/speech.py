from os import system

def say(text):
	system("pico2wave -w speech.wav \"" + text + "\"")
def saywithplay(text):
	say(text)
	system("play speech.wav")
