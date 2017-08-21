import urllib
import urllib2
from bs4 import BeautifulSoup
import youtube_dl

textToSearch = raw_input("Enter search query...")

query = urllib.quote(textToSearch)

url = "https://www.youtube.com/results?search_query=" + query

response = urllib2.urlopen(url)

html = response.read()

print html
#soup = BeautifulSoup(html)

soup =  BeautifulSoup(html, "html5lib")


video = str(soup.find(attrs={'class':'yt-uix-tile-link'}))

print video

print "href=" in video
video = video[video.index("href=")+6:]

video = video[0:video.index("\"")]

print "https://youtube.com" + video

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3
  'outtmpl': '%(id)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download(["https://youtube.com" + video])
