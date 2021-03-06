import youtube_dl

options = {
  'format': 'bestaudio/best',
  'extractaudio' : True,  # only keep the audio
  'audioformat' : "mp3",  # convert to mp3 
  'outtmpl': '%(id)s',    # name the file the ID of the video
  'noplaylist' : True,    # only download single song, not playlist
}

with youtube_dl.YoutubeDL(options) as ydl:
    ydl.download([raw_input("enter url...")])
