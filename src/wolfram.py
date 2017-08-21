from urllib2 import urlopen
import os
from speech import say

def lookup(input):
	key = "PG598P-Q6W5GWGA29"

	request = "https://api.wolframalpha.com/v1/result?i=" + input.replace(" ", "+") + "%3F&appid=" + key
	try:
		response = urlopen(request)
	except Exception as e: #We know it's connected to the internet because of the speech recognition, so the only other possible exception has to be that WA doesn't know the answer.
		print e
		say("Sorry, I don't know the answer to that question. Please try again.")

	data = str(response.read())
	#data = data[0:len(data)-1]
	print(data)
#	data = data.replace("\"", " inches ").replace("'", " feet ").replace('\\', " ")

	print(data)
	say(data)
