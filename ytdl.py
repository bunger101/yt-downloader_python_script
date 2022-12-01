import pytube
from pytube import Playlist
from pytube import YouTube
import re
from datetime import datetime
import os
from os import remove
from os import path
from moviepy.video.io.VideoFileClip import AudioFileClip

# It returns /home/YOUR_USER_PATH_HERE/...
username_path=os.path.expanduser(path="~")

print("WELCOME TO THE DOWNLOADER SYSTEM")
print("--------------------------------")

print("Is this a playlist(P) or an unique video(V)?","\n",end="")
response = str(input).capitalize()

dl_data_txt = f"{username_path}/yt-downloader/downloader_compilation.txt"
dl_data_open = open(dl_data_txt, "a")
# file_ext = []

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

list_comands = ['\"', '|', ',', '/', '\\', '//', ':', '*', '?', '<', '>', '.', ';', '~', '{', '}', 'º', 'ª', '%', '$', '#']

mod_par = 30
# Modificable Parameter: Maximum length the string must have 
# (without including the extension ".mp4").
# With extension len(title) = 34

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

        for index in title:
            if index in list_comands:
                title = title.replace(index ,"")

        if len(title) > mod_par:
            title_range = len(title) - mod_par
            title = title[:-title_range]

        time_file = YouTube(url).length
        if 2 < time_file < 60:
            time_fill = "{} Seconds".format(time_file)
        elif time_file < 2:
            time_fill = "{} Second".format(time_file)
        else:
            time_fill = "{0:.2f} Minutes".format(time_file/60)

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
                print("\n", f"'{title_ext}' has been downloaded in '{folder_hq}' folder; Duration: {time_fill}")
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_hq}' folder; Duration: {time_fill}" + "\n" + lines_str + line_incr)
            elif(option == "2"):
                print("Downloading the video... Wait a moment, please.")
                videoLQ = yt.streams.get_lowest_resolution()
                title_ext = title + str("_lq") + str(".mp4")
                videoLQ.download(output_path=folder_lq)                          # type: ignore
                common_line
                print("\n", f"'{title_ext}' has been downloaded in '{folder_lq}' folder; Duration: {time_fill}")
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_lq}' folder; Duration: {time_fill}" + "\n" + lines_str + line_incr)
            elif(option == "3"):
                print("Downloading the audio... Wait a moment, please.")
                print()
                audio = yt.streams.get_audio_only()
                title_ext = title + str("_a") + str(".mp4")
                Audio = audio.download(output_path=folder_a, filename=title_ext)         # type: ignore
                
                clip = AudioFileClip(Audio)
                clip.write_audiofile(Audio[:-4] + ".mp3")
                remove(f'{folder_a}{title_ext}')
                clip.close()

                common_line
                dl_data_open.write("\n" + f"'{title_ext.capitalize()}' has been downloaded in '{folder_a}' folder; Duration: {time_fill}" + "\n" + lines_str + line_incr)
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
            n_urls = len(playlist.video_urls)
            
            count = 1
            
            dl2_data_txt = f"{username_path}/yt-downloader/info-videos.txt"
            dl2_data_open = open(dl2_data_txt, "w")
            dl2_data_open.write(f"N | Artist/Title/Author/Characters" + "\n" + "----------------------------------" + "\n")
            for url_title in playlist.video_urls:
                yt_url_title = pytube.YouTube(url_title)
                title_url = yt_url_title.title
                if len(title_url) > mod_par:
                    title_fast = len(title_url) - mod_par
                    title_url = title_url[:-title_fast]
                dl2_data_open = open(dl2_data_txt, "a")
                dl2_data_open.write(f"{count} | {title_url}'" + "\n")
                count += 1
            dl2_data_open.close()

            print("Before responding! To see 'N' column, take a view at the 'info-videos.txt' generated file and chose the range between these integers.")
            print("Do you want to begin downloading between some range of videos? [Yes/No]: ", end="")
            switch = str(input().capitalize())
            print("")

            while "Yes" or "No" in switch:
                if switch == "Yes":
                    print(f"Introduce the initial and the final range between them [1-{n_urls}] -> (NOTE: if IR < 1 then IR=1 ; if FR > {n_urls} then FR={n_urls}: ")
                    print("Initial range (IR): ", end="")
                    i_range = int(input())
                    if i_range < 1:
                        print("You've assigned a number less than 1, so it will begin from the first one.")
                        i_range = 1
                    print("Final range (FR): ", end="")
                    f_range = int(input())
                    if f_range > n_urls:
                        print(f"You've assigned a number bigger than {n_urls}, so it will give the last video's URL.")
                        f_range = n_urls
                    break
                elif switch == "No":
                    i_range = 1
                    f_range = n_urls
                    break
                print("Try again, only 'Yes' or 'No': ", end="")
                switch = str(input()).capitalize()
            print("")

            print("Choose the desired option (type: int):")
            print("1 - HD Video")
            print("2 - LD Video") # Adequate for mobile phones.
            print("3 - Audio")
            option = input("Chosen option: ")
            print("")

            if(option == "1"):
                dl_data_open.write("\n" + f"Videos High Quality inserted in '{folder_hq}' folder" + "\n")
                for url in playlist.video_urls[i_range-1:f_range]:
                    yt = pytube.YouTube(url)
                    title = yt.title

                    for index in title:
                        if index in list_comands:
                            title = title.replace(index ,"")

                    if len(title) > mod_par:
                        title_range = len(title) - mod_par
                        title = title[:-title_range]

                    time_file = YouTube(url).length
                    if 2 < time_file < 60:
                        time_fill = "{} Seconds".format(time_file)
                    elif time_file < 2:
                        time_fill = "{} Second".format(time_file)
                    else:
                        time_fill = "{0:.2f} Minutes".format(time_file/60)

                    videoHD = yt.streams.get_highest_resolution()
                    title_ext = title + str("_hq") + str(".mp4")

                    videoHD.download(output_path=folder_hq,                      # type: ignore
                                     filename=title_ext)

                    print("Video {} of {} downloaded: {}".format(count, n_urls, title_ext))

                    dl_data_open.write("\n" + f"Video {count} with a duration of {time_fill} downloaded: '{title_ext.capitalize()}'")

                    count += 1

                dl_data_open.write("\n" + lines_str + line_incr)
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_hq))

            elif(option == "2"):
                dl_data_open.write("\n" + f"Videos Low Quality inserted in '{folder_lq}' folder" + "\n")
                for url in playlist.video_urls[i_range-1:f_range]:
                    yt = pytube.YouTube(url)
                    title = yt.title

                    for index in title:
                        if index in list_comands:
                            title = title.replace(index ,"")
                            
                    if len(title) > mod_par:
                        title_range = len(title) - mod_par
                        title = title[:-title_range]

                    time_file = YouTube(url).length
                    if 2 < time_file < 60:
                        time_fill = "{} Seconds".format(time_file)
                    elif time_file < 2:
                        time_fill = "{} Second".format(time_file)
                    else:
                        time_fill = "{0:.2f} Minutes".format(time_file/60)

                    videoLD = yt.streams.get_lowest_resolution()
                    title_ext = title + str("_lq") + str(".mp4")

                    videoLD.download(output_path=folder_lq,                      # type: ignore
                                     filename=title_ext)

                    print("Video {} of {} downloaded: {}".format(count, n_urls, title_ext))

                    dl_data_open.write("\n" + f"Video LQ {count} with a duration of {time_fill} downloaded: '{title_ext.capitalize()}'")

                    count += 1

                dl_data_open.write("\n" + lines_str + line_incr)
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_lq))

            elif(option == "3"):
                dl_data_open.write("\n" + f"Audios inserted in '{folder_a}' folder" + "\n")
                for url in playlist.video_urls[i_range-1:f_range]:
                    yt = pytube.YouTube(url)
                    title = yt.title

                    for index in title:
                        if index in list_comands:
                            title = title.replace(index ,"")
                            
                    if len(title) > mod_par:
                        title_range = len(title) - mod_par
                        title = title[:-title_range]

                    time_file = YouTube(url).length
                    if 2 < time_file < 60:
                        time_fill = "{} Seconds".format(time_file)
                    elif time_file < 2:
                        time_fill = "{} Second".format(time_file)
                    else:
                        time_fill = "{0:.2f} Minutes".format(time_file/60)

                    title_ext = title + str("_a") + str(".mp4")

                    audio = yt.streams.get_audio_only()
                    Audio =audio.download(output_path=folder_a, filename=title_ext)     # type: ignore

                    clip = AudioFileClip(Audio)
                    clip.write_audiofile(Audio[:-4] + ".mp3")
                    remove(f'{folder_a}{title_ext}')
                    clip.close()

                    dl_data_open.write("\n" + f"Audio {count} with a duration of {time_fill} downloaded: '{title_ext.capitalize()}'")

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
