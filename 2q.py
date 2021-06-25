# importing the module 
import os
import re
import pytube

# where to save 
SAVE_PATH = "./videos" 

def download_playlist (url):
    print('📍 Getting videos in the playlist:')
    playlist = pytube.Playlist(url=url)
    playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")

    links = playlist.video_urls
    print('✅ There is ', len(links) ,'video in the playlist.')

    idx = 0
    for link in links:
        idx += 1
        print('📍 Downloading:', link)
        try: 
            # object creation using YouTube
            # which was imported in the beginning 
            yt = pytube.YouTube(link)
            stream = yt.streams.filter(only_audio=True)[0]
            stream.download(SAVE_PATH)
            print('✅ Downloaded', idx ,'of', len(links))

            video_id = get_video_id(link)
            write_name_in_file(video_id)
        except: 
            print("Connection Error") #to handle exception 
  

def write_name_in_file (name):
    print('📍 Writing file name in downloaded list:', name)
    file1 = open('./downloaded.txt', 'r')
    names = file1.read().split(',')
    last_one = names[len(names)-1]
    file1.close()


    buffer = open('./downloaded.txt', 'a')

    new_name = ','+name
    buffer.write(new_name)
    buffer.close()
    print('✅ Wrote successfully')


def get_video_id (url):
    print('📍 Getting Video id:')
    try:
        idx = url.index('/watch?v=')
        return url[idx+9:]
    except:
        print('The url doesn\'t contain "/watch?v="')


def convert_mp4_to_mp3 ():
    print('📍 Converting to mp3:')
    arr = os.listdir('./videos')
    id=0
    for i in arr:
        id+=1
        print('📍 Converting:', i)

        mp4_file = './videos/'+i
        try:
            mp3_file = './songs/'+i.replace('mp4', 'mp3')
            os.rename(src=mp4_file, dst=mp3_file)

            print('✅ Converted', id ,'of', len(arr))
        except:
            print('🚨 Can\'t convert mp3')

url = input('Enter Url: ')
download_playlist(url)
convert_mp4_to_mp3()