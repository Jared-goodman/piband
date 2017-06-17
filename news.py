#This is a demonstration of a simple script that gets news from an API and tells them to you.
import urllib2
import os
response = urllib2.urlopen("https://newsapi.org/v1/articles?source=abc-news-au&sortBy=top&apiKey=0b048c3a81aa42d08381279c729cefae")
json = str(response.read())
#print json
sources = open("newssource.txt")
rope = str(sources.read())
temp = 0
newLine = False
recording = False
for x in rope:
	if newLine:
		if not x == "#":
			print temp
			recording = True
			temp = ""
		newLine = False
	if recording:
		temp = temp + x
	if x == "\n":
		newLine = True

os.system("espeak -ven+f4 \"Here are the top headlines from ABC news today:\"")
#Parsing the json and reading articles aloud:
while "title" in json:
	json = json[json.index("title") + 8:]
	title = json[0:json.index("\"")]
	print title
#	os.system("espeak -ven+f4 \"" + title + "\"")


