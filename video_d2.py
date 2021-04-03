# python program to download any youtube video

#importing necessary librariers
from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['youtube_video_url'])#copy paste the url 