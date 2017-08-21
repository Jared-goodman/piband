import urllib2
from speech import say

def readxkcd(comic):
	data = urllib2.urlopen("https://xkcd.com/" + comic + "/info.0.json")
	lines = ""
	for line in data.readlines():
		lines = lines + line + " "

	lines = lines[lines.index("transcript"):lines.index(", \"alt\":")]
	lines = lines.replace("{", "")
	lines = lines.replace("}", "")
	lines = lines.replace("\"", "")
	lines = lines.replace("[", "")
	lines = lines.replace("]", "")
	lines = lines.replace("\\n", " ")
	print lines
	say(lines)
