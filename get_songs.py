"""This example shows how to get the full message history of a chat, starting from the latest message"""

from pyrogram import Client
import youtube_dl
import stagger
import const

ydl_opts = {
    'format': 'bestaudio/best',
   # 'writethumbnail': True,
    'outtmpl': '/home/ferro/Music' + '/%(title)s.mp3',
    'embed-thumbnail'
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

app = Client(
    "my_account",
    api_id=const.api_id,
    api_hash=const.api_hash
)

target = const.target  # "me" refers to your own chat (Saved Messages)
count = 0
test = ""
with app:
    for message in app.iter_history(target):
        if message.text != None:
            if "youtube.com" in message.text:
                print(message.text.split("&",1)[0])
                test = message.text.split("&",1)[0]
                count += 1
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                        instance = ydl.download([test])
                        #print(ydl.params)
                except Exception as Err:
                    print(Err)
    print("Total Number of Songs: %s"%(count))