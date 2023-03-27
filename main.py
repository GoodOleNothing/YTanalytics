from workshop.channel import Channel
from workshop.video import Video
from workshop.plvideo import PLVideo
from workshop.playlist import PlayList




#video1 = Video('9lO06Zxhu88')
#print(video1)
#video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
#print(video2)

gg = PlayList('PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb')
print(gg.title)
print(gg.url)
duration = gg.total_duration
print(duration)
print(type(duration))
print(duration.total_seconds())
gg.show_best_video()
