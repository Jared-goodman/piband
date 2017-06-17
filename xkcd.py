import urllib2
import os

comic = raw_input("Which comic?")
data = urllib2.urlopen("https://xkcd.com/" + comic + "/info.0.json")
lines = ""
for line in data.readlines():
	lines = lines + line + " "


#print lines
lines = lines[lines.index("transcript"):lines.index(", \"alt\":")]
lines = lines.replace("{", "")
lines = lines.replace("}", "")
lines = lines.replace("\"", "")
lines = lines.replace("[", "")
lines = lines.replace("]", "")
lines = lines.replace("\\n", " ")


print lines
os.system("espeak -ven-us+f2 \"" + lines + "\"")
