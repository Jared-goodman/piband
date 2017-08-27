import urllib2, urllib, json, datetime, os.path, sys, os, re, random, subprocess, weather
import speech_recognition as sr
from dictionary import find
from cthulhu import summon
from xkcd import readxkcd
from thesaurus import thesaurus
from speech import say, saywithplay
from wolfram import lookup
from chatbot import chatbot
from sendemail import send
from time import sleep
from gpiozero import PWMLED, Button
from threading import Thread
from recorder import Recorder
from os import path

try:
	import apiai
except ImportError:
	sys.path.append(
		os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
	)
	import apiai

def beep():
	os.system("aplay /home/pi/piband/src/sounds/beep.wav")


def timer(seconds):
	print "timer set"
	sleep(seconds)
	print "Timer finished"
	say("Timer finished! Timer finished! Timer finished!")
def alarm(time):
	while not datetime.datetime.now().strftime("%H:%M") == time:
		sleep(1)

	print "Alarm finished!"
	say("Alarm finished! Alarm finished! Alarm finished!")



r = sr.Recognizer()
print "created r"
#r.energy_threshold = 3000
button = Button(13)
contactemail = ""
led = PWMLED(4)
led.on()
print "created button and led"
first = True
sendingemail = False
print "about to speak"
say("Powered on. Press the button to start.")
while True:
	try:
		
		# obtain audio from the microphone
		button.wait_for_press()
		led.pulse()

		rec = Recorder(channels=2)
		recfile = rec.open('/home/pi/piband/src/recording.wav', 'wb')
		recfile.start_recording()
		button.wait_for_release()
		recfile.stop_recording()
		recfile.close()
		#I have no idea why, but this line makes it work. https://github.com/bobmonkeywarts/piband/issues/1
		if(first):
			say("Closed recfile")
			first = False
		led.blink(on_time=0.75, off_time=0.75)
		print "recorded audio"
#		say("About to play sound")
		thread = Thread(target = beep, args = ())
		thread.start()

		AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "/home/pi/piband/src/recording.wav")
		r = sr.Recognizer()
		with sr.AudioFile(AUDIO_FILE) as source:
			audio = r.record(source)
		
		# recognize speech using Google Speech Recognition
		try:
			# for testing purposes, we're just using the default API key
			# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
			# instead of `r.recognize_google(audio)`
			input = r.recognize_google(audio).lower()
			print ("I think you said: ") + input
		except sr.UnknownValueError:
    			print("Google Speech Recognition could not understand audio")
			led.on()
			saywithplay("Sorry, I couldn't understand that. Can you try saying it again?") #the say command only creates the speech file, it doesn't play it.
			continue
		except sr.RequestError as e:
			say("Please check your internet connection and try again.")
			print("Could not request results from Google Speech Recognition service; {0}".format(e))


#		input = raw_input("").lower()
	

		if "weather" in input:
			weather.conditions()#Reads current conditions out loud

		elif "set an alarm" in input or "wake me up at " in input or "timer" in input:
			'''
			if "half" in input or "until" in input:
				print "I'm sorry, but you need to phrase that as a numerical statement, such as saying \"set an alarm for 5:45.\""
				say("I'm sorry, but you need to phrase that as a nuemrical statemet using non-military time, such as saying set an alarm for five forty five pm.")
				break
			if input == "set an alarm":
				time = raw_input("For what time?")
			else:
				if "set an alarm" in input:
					time = input[input.index("set an alarm for ")+17:]
			#		print time
				else:
					time = input[input.index("wake me up at")+14:]
			#		print time
			if "night" in time or "noon" in time or "pm" in time: #"noon" is part of the word "afternoon"
				ampm = "pm"
			elif "morning" in time or "am" in time:
				ampm = "am"
			else:
				temp = raw_input("AM or PM?")
				if "night" in temp or "noon" in temp or "pm" in temp:
					ampm = "pm"
				elif "morning" in temp or "noon" in temp:
					ampm = "am"
			numscolon = ":1234567890" #This will filter out numbers and the colon to get the time itself
			for c in time:
				if c not in numscolon:
					time = time.replace(c, "")
			#now time is someting like "6" or "5:45"
			#print time
			#print ampm
			if ampm == "pm": #converts to military time for alarm() method
				hour = time[0:time.index(":")]
				hour = str(int(hour)+12)
				time = hour + time[time.index(":"):]
			print ("Alarm set for " + time + " " + ampm)
			say("Alarm set for " + time + " " + ampm)
			alarm(time)
			'''
			say("Sorry, but for the Seattle Mini Maker Faire this featuer has been disabled.")
		if "send" in input and "email" in input:
			send(input)
		elif "music" in input:
			#os.system("python playsongs.py")
			#I don't care about the other exibits, it's just that the music feature was buggy
			say("Sorry, but for the Seattle Mini Maker Faire this feature has been disabled as it could possibly interfere with other exibits.")

		elif "exit" == input:
			say("Ok! Exiting...")
			sys.exit(0)

		elif "xkcd" in input:
			#Filters out the numbers in input. Not exactly the prettiest way to do it, but this is my code, not yours, so shut up.
			nums = "1234567890"
			comic = ""
			for x in input:
				if x in nums:
					comic = comic + x
			
			if "one" in input: #For some reason, the speech recognition software transcribes the number "1" as "one" and all other numbers in standard form.
				comic = "1"
			readxkcd(comic)
		elif "define" in input:
			try:
				print find(input[7:])
		#		say(input[7:])
			except:
				print "word not found!"
				say("word not found")
		elif "synonym" in input or "antonym" in input:
			if "of" in input:
				thesaurus(input[input.index("of")+3:])
			elif "for" in input:
				thesaurus(input[input.index("for")+4:])

		elif input[0:6] == "script": #excecutes script, similar to an alexa skill but for the piband which is better because I made it
			print ("excecuting python script \"" + input[6:] + ".py...")
			say("Excecuting the " + input[6:] + " script...")
			input = input.replace(" ", "")
			print "." + input[6:] + "."
			os.system("python /home/pi/piband/src/" + input[6:] + ".py") #not very portable but whatever shut your facehole

		elif "translate" in input:
			os.system("echo \"" + input + "\" | python3 /home/pi/piband/src/translate.py") #Translate code needs to be in Python3 because of special characters that Python 2.7 can't handle

		elif "cthulhu" in input:
			summon()
		elif "statistics made up" in input or "statistics are made up" in input:
			toSay = "About " + str(int(random.random()*100)+1) + " percent of statistics are made up on the spot."
			print toSay
			say(toSay)
		elif ("how" in input or "when" in input or "what" in input) and not "you" in input:
			lookup(input)
		elif "say" in input:
                        say(input[input.index("say")+3:]) #If you want the speech synth to say something
		elif "power off" in input or "turn off" in input:
			saywithplay("Ok, turning off...")
			os.system("sudo shutdown now")
		elif "reboot" in input:
			saywithplay("Ok, rebooting...")
			os.system("sudo reboot now")
		else:
#			say("About to use chatbot api")
			chatbot(input)
		led.on()
		os.system("play speech.wav")
	except SystemExit:
		sys.exit(0)  #This is basically saying: If a systemexit exception is thrown, throw a systemexit exception because the whole thing is in a giant try-except statement
	except Exception as e:   #can't have bugs if all the code is in a try-except statement
		print "Sorry, that cannot be done. Please try again."
		print e
#		say("about to write to log file")
#		f = open("/home/pi/piband/src/log.txt", "a")
#		f.write(e + "\n")
#		say("Sorry, an error occured. Can you say that again?")
#	say("restarting loop...")
