import urllib2, urllib, json, datetime, os.path, sys, os, re, random
from time import sleep
from yandex_translate import YandexTranslate
from threading import Thread

try:
	import apiai
except ImportError:
	sys.path.append(
		os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
	)
	import apiai

def say(txt):
	os.system("espeak -ven+f4 \"" + txt + "\"")

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

def find(x):     #simple dictionary code copy-pasted from stack overflow
    srch=str(x)
    x=urllib2.urlopen("http://dictionary.reference.com/browse/"+srch+"?s=t")
    x=x.read()
    items=re.findall('<meta name="description" content="'+".*$",x,re.MULTILINE)
    for x in items:
        y=x.replace('<meta name="description" content="','')
        z=y.replace(' See more."/>','')
        m=re.findall('at Dictionary.com, a free online dictionary with pronunciation,              synonyms and translation. Look it up now! "/>',z)
        if m==[]:
            if z.startswith("Get your reference question answered by Ask.com"):
                print "Word not found! :("
		say ("Word not found")
            else:
                z = z[z.index(',')+2:z.index("See more")]
               # print z
		say(z)
                return z


CLIENT_ACCESS_TOKEN = 'f1f4bd11d9b84401aa53684d6f8833d0'


def chatbot(arg):
	ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

	request = ai.text_request()

	request.lang = 'en'  # optional, default value equal 'en'

	request.session_id = "<SESSION ID, UNIQUE FOR EACH USER>"

	request.query = arg

	response = request.getresponse()

	rope = str(response.read())

	rope = rope[rope.index("speech")+10:]

	rope = rope[0:rope.index("\"")]

	print rope
	say(rope)


while True:
	try:
		input = raw_input("").lower()
	
		weather = ["what's the weather", "what's the weather like", "how's the weather", "what's the weather like today", "what's the weather like here", "what is the weather", "what is the weather like", "what is the weather like today", "what is the weather like here"]
		timeis = ["what time is it", "what's the time", "what is the time"]
		dateis = ["what day is it", "what's the date", "what is the date", "what day is it today", "what's the date today", "what is the date today"]
		playplaylist = ["play some music", "play music", "play a playlist", "play my playlist"]

		if input in weather:
			baseurl = "https://query.yahooapis.com/v1/public/yql?"
			yql_query = "select item.condition from weather.forecast where woeid in (select woeid from geo.places(1) where text=\"seattle\")"
			yql_url = baseurl + urllib.urlencode({'q':yql_query}) + "&format=json"
			result = urllib2.urlopen(yql_url).read()
			data = json.loads(result)
			raw =  str(data['query']['results']).lower()
			#print raw
			tempvar = raw[raw.index("u\'temp\'")+11:]
			#print tempvar
			tempvar = tempvar[0:tempvar.index("\'")]
			toPrint =  "In your current location, it is " + tempvar + " degrees "
			#print toPrint
			tempvar = raw[raw.index("u\'text\'")+11:]
			tempvar = tempvar[0:tempvar.index("\'")]
			#print tempvar
			toPrint = toPrint + "and it is " + tempvar + " outside."
			print toPrint
			say (toPrint)

		elif input in timeis:
			time = str(datetime.datetime.now().time())
			hour = time[0:time.index(":")]
			time = time[time.index(":")+1:]
			if hour>12:
				hour = str(int(hour) -12)
			minute = time[0:time.index(":")]
			print "The time is " + hour + ":" + minute
			say("The time is " + hour + ":" + minute)

		elif input in dateis:
			days = ["sunday", "monday", "tuesday", "wenesday", "thursday", "friday", "saturday"]
			day = days[int(datetime.datetime.now().strftime("%w"))]
			months = ["january", "febuary", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
			month = months[int(datetime.datetime.now().strftime("%m"))]
			toSay = "Today is " + day + ", " + month + datetime.datetime.now().strftime(" %d, 20%y")
			print toSay
			say(toSay)
		elif "set an alarm" in input or "wake me up at " in input:
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

		elif "set a timer" in input:
			if "for" not in input:
				input = "for " + raw_input("For how long?")

			if "for" in input:
				hours = 0
				minutes = 0
				seconds = 0
				if "hour" in input:
					hours = int(input[input.index("for ") + 4 : input.index("hour")])
					#print hours
				if "minute" in input:
					index = input.index("minute") #right before the number of minutes
					spaces = 0
					while spaces<2:
						if input[index] == ' ':
							spaces = spaces + 1
						index = index - 1
					num = input[index+2:]
					num = num[0:num.index(' ')]
					#print num
					mintues = int(num)
				if "second" in input:
					index = input.index("second") #right before the number of seconds
		                        spaces = 0
		                        while spaces<2:
		                                if input[index] == ' ':
		                                        spaces = spaces + 1
		                                index = index - 1
		                        num = input[index+2:]
		                        #num = num[0:num.index(' ')]
		                        print num
					seconds = int(num)
				sum = hours*3600 + minutes*60 + seconds
				toSay = "Timer set for " + hours + " hours " + minutes + " minutes " + seconds + " seconds"
				print toSay
				say(toSay)
				thread = Thread(target = timer, args = (sum, ))
				thread.start()

		elif input in playplaylist:
			os.system("python playsongs.py")

		elif "say" in input:
			say(input[input.index("say")+3:])
		elif "xkcd" in input:
			nums = "1234567890"
			comic = ""
			for x in nums:
				if x in input:
					comic = comic + x

			if comic == "":
				if not ("current" in input or "new" in input):
					comic = raw_input("Please enter the number of the comic...")


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

			if lines == "transcript: ":
				print ("There is no transcript avalible for this comic. Please try again later.")
				say("There is no transcript avalible for this comic. Please try again later.")
			else:
				print lines
				say(lines)

		elif "define" in input:
			try:
				print find(input[7:])
		#		say(input[7:])
			except:
				print "word not found!"
				say("word not found")
		elif "synonym" in input or "antonym" in input:
			if "of" in input:
				os.system("echo \"" + input[input.index("of")+3:] + "\" | python thesaurus.py")
			elif "for" in input:
				os.system("echo \"" + input[input.index("for")+4:] + "\" | python thesaurus.py")

		elif input[0:6] == "script": #excecutes script, similar to an alexa skill but for the piband which is better because I made it
			print ("excecuting python script \"" + input[7:] + ".py\"...")
			os.system("python " + input[7:] + ".py")

		elif "translate" in input:
			os.system("echo \"" + input + "\" | python3 translate.py")

		elif "how many genders are there" in input:
			print "Some people say two, some people say eighty-someting. I will stay netural in this issue."
			say("Some people say two, some people say eighty-something. I will stay netural in this issue.")
		elif "summon cthulu" in input:
			print "Ok. Summoning Chtulu now..."
			say("Ok. Summoning Cuhtulu now...")
			os.system("aplay cthulu/cthulu.wav")
			print "Cthulu successfuly summoned."
			say("Cuthulu successfuly summoned.")
		elif "how many popes per square mile" in input:
			print "There are about 5.9 popes per square mile in Vatican City."
			say("There are about 5.9 popes per square mile in Vatican City.")
		elif "statistics made up" in input or "statistics are made up" in input:
			toSay = "About " + str(int(random.random()*100)+1) + " percent of statistics are made up on the spot."
			print toSay
			say(toSay)
		else:
			chatbot(input)
	except:   #me being a lazy programmer
		print "Sorry, that cannot be done. Please try again."
