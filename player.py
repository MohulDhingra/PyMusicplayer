import requests
import json
import time
import vlc

res=requests.get("https://api.audioboom.com/channels/4668158/audio_clips")
print(res.text)
data=json.loads(res.text)
clips=data["body"]["audio_clips"]
titles=[]
mp3=[]
for i in clips:
    titles.append(i["title"])
    mp3.append(i["urls"]["high_mp3"])
for i in range(0,len(titles)):
    print(i,' ',titles[i])
opt=int(input("Enter the track number:"))

p=vlc.MediaPlayer(mp3[opt])
p.play()


time.sleep(10)

