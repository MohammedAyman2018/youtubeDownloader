from moviepy.editor import *
import os
arr = os.listdir('./videos')

for i in arr:
    print('📍 Converting:', i)

    mp4_file = './videos/'+i
    mp3_file = './songs/'+i.replace('mp4', 'mp3')
    
    videoclip = VideoFileClip(mp4_file)
    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)
    audioclip.close()
    videoclip.close()

    print('✅ Converted')