inputtext = input()
from yandex_translate import YandexTranslate
import os, sys
key = "trnsl.1.1.20170402T171203Z.69851206a4c59331.b4d7b72f80578f5d857aaff5b52f84628eee54fb" #my API key, if you copy this code PLEASE DO NOT USE THIS KEY, GET YOUR OWN 
translate = YandexTranslate(key)
languages = ["spanish", "esperanto", "french", "russian", "chinese", "mandarin", "mandarin chinese", "polish", "german", "afrikaans", "bosnian", "catalan", "czech", "danish", "greek", "finnish", 
"croatian", "hungarian", "italian", "kannada", "latvian", "dutch", "portuguese", "kurdish", "romanian", "slovak", "serbian", "swedish", "swahili", "tamil", "turkish", "welsh", "hindi", "armenian", "indonesian", "icelandic", "georgian", "latin", "macedonian", "norwegian", "albanian", "vietnamese"]
languageCodes = ["es", "eo", "fr", "ru", "zh", "zh", "zh", "pl", "de", "af", "bs", "ca", "cs", "da", "el", "fi", "hr", "hu", "it", "kn", "lv", "nl", "pt", "ku", "ro", "sk", "sr", "sv", "sw", "ta", "tr",
"cy", "hi", "hy", "id", "is", "ka", "la", "mk", "no", "sq", "vi"]
containsLanguage = False
for l in languages:
	temp = "to " + l
	if temp in inputtext:
		language = l
		containsLanguage = True
		end = inputtext.index("to " + l)
		if "into" in inputtext:
			end = inputtext.index("into " + l)

if "to english" in inputtext and inputtext.index("to english")+10 == len(inputtext):
	print("Sorry, but I can only translate to other languages as my speech recognition is english-only.")
	sys.exit(0)


if not containsLanguage:
	end = len(inputtext)
#	language = input("Please tell me the language you want to translate. Supported languages are spanish, esperanto, french, russian, mandarin chineese, german, and polish.")
	print ("Sorry, you must specify a language, such as saying \"translate hello to esperanto.\"")
	sys.exit(0)
while (language not in languages):
	language = input("I\'m sorry, that is not a supported language. Please tell me a supported language.")

textToTranslate = inputtext[inputtext.index("translate")+10:end]
languageCode = languageCodes[languages.index(language)]
data = translate.translate(textToTranslate, "en-"+ languageCode)
#print(data)
data = str(data)
print(data)
data = data[data.index("[")+2:data.index("]")-2]
print("\"" + textToTranslate + "\" translated to " + language + " is \"" + data + "\".")
os.system("espeak \"" + textToTranslate + " translated to " + language + " is\" -ven+f4")
os.system("espeak -v" + languageCode + "+f4 \"" + data + "\"")
