from pytube import YouTube
from sys import argv

path = "D://DOWNLOADS//ytdownloads"

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Number of views: ", yt.views)


video = yt.streams.get_highest_resolution()
video.download(path)