#This is a demonstration of a simple script that gets news from an API and tells them to you.
import urllib2
import os

def say(text):
	os.system("pico2wave -w speech.wav \"" + text + "\" && play speech.wav")
#os.system("espeak -ven+f4 \"news script running\"")
sources = open("/home/pi/piband/src/newssource.txt")
rope = str(sources.read())
temp = ""
ar = []
for x in rope:
	if x == "\n":
		ar.append(temp)
		temp = ""
	else:
		temp += x
print ar

say("Here are the top headlines from the news sources that you chose today:")
#Parsing the json and reading articles aloud:

for x in ar:
	response = urllib2.urlopen("https://newsapi.org/v1/articles?source=" + x + "&sortBy=top&apiKey=0b048c3a81aa42d08381279c729cefae")
	json = str(response.read())

	json = json[json.index("title") + 8:]
	title = json[0:json.index("\"")]
	print title
	say(title)


