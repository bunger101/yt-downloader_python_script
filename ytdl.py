import pytube
from pytube import Playlist
import re
from datetime import datetime
import os

# It returns /home/YOUR_USER_PATH_HERE/...
username_path=os.path.expanduser(path="~")

print("WELCOME TO THE DOWNLOADER SYSTEM")
print("--------------------------------")

print("Is this a playlist(P) or an unique video(V)?","\n",end="")
response = str(input).capitalize()

dl_data_txt = f"{username_path}/yt-downloader/downloader_compilation.txt"
dl_data_open = open(dl_data_txt, "a")
file_ext = []

today = datetime.now()
today_dl = '{:Date of download: %d %B of %Y : %A at %H:%M:%S}'.format(today)
len_today_dl = len(today_dl)
line = "-"
lines = []
for len_today_dl in range(1,len_today_dl+1):
    lines.append(line)
lines_str = "".join(lines)
common_line = dl_data_open.write(f"{lines_str}" + "\n" + f"{today_dl}" + "\n")
line_incr = "\n" + "\n" + "\n"

folder_a = "output_a/"
folder_hq ="output_hq/"
folder_lq ="output_lq/"

while response == "P" or response != "V":
    print(f'Introduce only "P" or "V": ',end="")
    response = str(input()).capitalize()
    if response == "V":
        url = input("Then, introduce the Youtube URL: ")
        print("")
        regex = r'^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+'
        
        while not re.match(regex, url):
            print("Try with a valid url:", end="")
            url = input(" ")
            if re.match(regex, url):
                print("---------------------")
                break
        
        yt = pytube.YouTube(url)
        title = yt.title
        
        def _download():
            print("Choose the desired option (type: int):")
            print("1 - HD Video")
            print("2 - LD Video") # Adequate for mobile phones.
            print("3 - Audio")
            option = input("Chosen option: ")
            print("")
            
            if(option == "1"):
                print("Downloading the video... Wait a moment, please.")
                videoHD = yt.streams.get_highest_resolution()
                title_ext = title + str("_hq") + str(".mp4")
                videoHD.download(output_path=folder_hq, filename=title_ext)      # type: ignore
                common_line
                print("\n", f"'{title}' has been downloaded in '{folder_hq}'")
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_hq}' folder" + "\n" + lines_str + line_incr)
            elif(option == "2"):
                print("Downloading the video... Wait a moment, please.")
                videoLQ = yt.streams.get_lowest_resolution()
                title_ext = title + str("_lq") + str(".mp4")
                videoLQ.download(output_path=folder_lq)                          # type: ignore
                common_line
                print("\n", f"'{title}' has been downloaded in '{folder_lq}'")
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_lq}' folder" + "\n" + lines_str + line_incr)
            elif(option == "3"):
                print("Downloading the audio... Wait a moment, please.")
                audio = yt.streams.get_audio_only()
                title_end = title.endswith(".")
                
                if title_end == True:
                    title_sum = title + "_"
                    title_ext = title_sum + str(".mp3")
                else:
                    title_ext = title + str(".mp3")
                
                audio.download(output_path=folder_a, filename=title_ext)         # type: ignore
                print("\n", f"'{title_ext}' has been downloaded in '{folder_a}'")
                common_line
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_a}' folder" + "\n" + lines_str + line_incr)
            else:
                print("Invalid option")
                print("--------------")
                _download()  
            
        _download()
        break
        
    if response == "P":
        def _download():
            url_playlist_in = \
                input("Then, introduce the youtube Playlist URL: ")
            print("")
            regex_playlist = r'^.*(youtu.be\/|list=)([^#\&\?]*).*'
        
            while not re.match(regex_playlist, url_playlist_in):
                print("Try with a valid url:", end="")
                url_playlist_in = input(" ")
                if re.match(regex_playlist, url_playlist_in):
                    print("--------------------------")
                    break
            
            playlist = Playlist(url_playlist_in)
            
            print("Choose the desired option (type: int):")
            print("1 - HD Video")
            print("2 - LD Video") # Adequate for mobile phones.
            print("3 - Audio")
            option = input("Chosen option: ")
            print("")
            
            count = 1
            
            if(option == "1"):
                dl_data_open.write("\n" + f"Videos High Quality inserted in '{folder_hq}' folder" + "\n")
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    
                    videoHD = yt.streams.get_highest_resolution()
                    title_ext = title + str("_hq") + str(".mp4")
                    
                    videoHD.download(output_path=folder_hq,                      # type: ignore
                                     filename=title_ext)
                    
                    print("Video {} downloaded: {}".format(count, title_ext))
                    
                    dl_data_open.write("\n" + f"Video {count} downloaded: '{title_ext.capitalize()}'")
                    
                    count += 1
                
                dl_data_open.write("\n" + lines_str + line_incr)
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_hq))
                
            elif(option == "2"):
                dl_data_open.write("\n" + f"Videos Low Quality inserted in '{folder_lq}' folder" + "\n")
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    
                    videoLD = yt.streams.get_lowest_resolution()
                    title_ext = title + str("_lq") + str(".mp4")
                    
                    videoLD.download(output_path=folder_lq,                      # type: ignore
                                     filename=title_ext)
                    
                    print("Video {} downloaded: {}".format(count, title_ext))
                    
                    dl_data_open.write("\n" + f"Video LQ {count} downloaded: '{title_ext.capitalize()}'")
                    
                    count += 1
                    
                dl_data_open.write("\n" + lines_str + line_incr)
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_lq))
                     
            elif(option == "3"):
                dl_data_open.write("\n" + f"Audios inserted in '{folder_a}' folder" + "\n")
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    title_end = title.endswith(".")
                
                    if title_end == True:
                        title_sum = title + "_"
                        title_ext = title_sum + str(".mp3")
                    else:
                        title_ext = title + str(".mp3")

                    audio = yt.streams.get_audio_only()
                    audio.download(output_path=folder_a, filename=title_ext)     # type: ignore
                    
                    print("Audio {} downloaded: {}".format(count, title_ext))
                    
                    dl_data_open.write("\n" + f"Audio {count} downloaded: '{title_ext.capitalize()}'")
                    
                    count += 1
                    
                dl_data_open.write("\n" + lines_str + line_incr)    
                print("")    
                print("Audios have been downloaded in the '{}' folder"\
                    .format(folder_a))
                
            else:
                print("Invalid option")
                print("--------------")
                _download() 
            
        _download()
        break
