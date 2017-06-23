from urllib.request import urlopen
import os

key = "PG598P-Q6W5GWGA29"

request = "https://api.wolframalpha.com/v1/result?i=" + input().replace(" ", "+") + "%3F&appid=" + key

response = urlopen(request)

data = str(response.read())[2:]
data = data[0:len(data)-1]
print(data)
data = data.replace("\"", " inches ").replace("'", " feet ").replace('\\', " ")

print(data)
os.system("espeak -ven+f2 \"" + data + "\"")
