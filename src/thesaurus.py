import urllib2
import sys
from speech import say

#Finds synonyms and antonyms of a given word.
def thesaurus(word):
	key = "8819e1fa984180cc5ead63d985844309"
	try:
		response = urllib2.urlopen('http://words.bighugelabs.com/api/2/'+key+'/'+word+'/')
		data = response.read()
	except:
		print("Word not found!")
		say("word not found!")
		sys.exit(0)

	data = data.replace("adjective", "")
	data = data.replace("noun", "")
	data = data.replace("adverb","")
	data = data.replace("verb","")
	data = data.replace("|", "")
	
	ar = data.split("\n")
	
	ar = ar[0:len(ar)-1] #ar has an empty string at the end, this removes it
	print ar
	
	print "Synonyms:"
	say("Some synonyms for " + word + " are ")
	count = 0
	for x in ar:
		if x[0:3] == "syn":
			if count<5:   #BigHugeThesaurus returns a lot of words and this filters 4/5 of the words out
				print x[3:]
				say(x[3:])
			count = count + 1
	
	

	hasAntonyms = False
	count = 0
	for x in ar:
		if x[0:3] == "ant":
			if not hasAntonyms:
				hasAntonyms = True
				print "Antonyms:"
				say("Some antonyms for " + word + " are:")
	
			print x[3:]
			say(x[3:])
			count = count + 1
