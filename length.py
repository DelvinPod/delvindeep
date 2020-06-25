import os
from mutagen.mp3 import MP3

statinfo = os.stat('eps\ep5.mp3')
size = str(statinfo.st_size)

audio = MP3('eps\ep5.mp3')
duration = str(audio.info.length)

print('Size: {}, Duration: {}'.format(size,duration))
