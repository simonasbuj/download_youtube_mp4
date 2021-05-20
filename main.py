from __future__ import unicode_literals
import youtube_dl
import os, sys

output_folder = "downloaded_videos"
input_file_name = "sarasas.txt"

file_path = os.path.join(sys.path[0], input_file_name)
print(file_path)

f = open(file_path, "r")
video_list = f.read().splitlines()
f.close()


ydl_opts = {
    'format':' bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',
    'outtmpl': 'Q:/Projects/Python/DownloadYoutube/downloads/{}/%(title)s.%(ext)s'.format(output_folder),
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for i, v in enumerate(video_list):
        print()
        print(f"{i+1}: Trying to download video url: {v}")

        #if url doesnt exist ignore error and continue with loop 
        try:
            ydl.download([v])
        except:
            pass
