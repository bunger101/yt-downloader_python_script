import pytube
from pytube import Playlist
import re

print("WELCOME TO THE DOWNLOADER SYSTEM")
print("--------------------------------")

print("Is this a playlist(P) or an unique video(V)?","\n",end="")
response = str(input).capitalize()

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
                print("--------------------------")
                break
        
        yt = pytube.YouTube(url)
        title = yt.title
        
        folder_a = "output_a/"
        folder_hq ="output_hq/"
        folder_lq ="output_lq/"

        def _download():
            print("Choose the desired option (type: int):")
            print("1 - HD Video")
            print("2 - LD Video") # Adequate for mobile phones.
            print("3 - Audio")
            option = input("Option chosen: ")
            
            if(option == "1"):
                print("Downloading the video... Wait a moment, please.")
                videoHD = yt.streams.get_highest_resolution()
                title_ext = title + str(".mp4")
                videoHD.download(output_path=folder_hq, filename=title_ext)      # type: ignore
            elif(option == "2"):
                print("Downloading the video... Wait a moment, please.")
                videoLQ = yt.streams.get_lowest_resolution()
                videoLQ.download(output_path=folder_lq)                          # type: ignore
            elif(option == "3"):
                print("Downloading the audio... Wait a moment, please.")
                audio = yt.streams.get_audio_only()
                title_ext = title + str(".mp3")
                audio.download(output_path=folder_a, filename=title_ext)         # type: ignore
            else:
                print("Invalid option")
                print("--------------")
                _download()
            if(option == "1"):
                print("") 
                print(f"'{title}' has been downloaded in '{folder_hq}'")
            if(option == "2"):
                print("") 
                print(f"'{title}' has been downloaded in '{folder_lq}'")
            if(option == "3"):
                print("") 
                print(f"'{title}' has been downloaded in '{folder_a}'")    
            
        _download()

        break
        
    if response == "P":
        def _download():
            url_playlist_in = \
                input("Then, introduce the youtube Playlist URL: ")
            playlist = Playlist(url_playlist_in)
            
            folder_a = "output_a/"
            folder_hq ="output_hq/"
            folder_lq ="output_lq/"
            
            print("")
            print("Choose the desired option (type: int):")
            print("1 - HD Video")
            print("2 - LD Video") # Adequate for mobile phones.
            print("3 - Audio")
            option = input("Option chosen: ")
            
            if(option == "1"):
                count = 1
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    
                    videoHD = yt.streams.get_highest_resolution()
                    title_ext = title + str(".mp4")
                    
                    videoHD.download(output_path=folder_hq,                      # type: ignore
                                     filename=title_ext)
                    
                    print("Video {} downloaded: {}".format(count, title_ext))
                    
                    count += 1
                    
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_hq))
                
            elif(option == "2"):
                count = 1
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    
                    videoLD = yt.streams.get_lowest_resolution()
                    title_ext = title + str(".mp4")
                    
                    videoLD.download(output_path=folder_lq,                      # type: ignore
                                     filename=title_ext)
                    
                    print("Video {} downloaded: {}".format(count, title_ext))
                    
                    count += 1
                    
                print("")    
                print("Videos have been downloaded in the '{}' folder"\
                    .format(folder_lq))
                     
            elif(option == "3"):
                count = 1
                for url in playlist.video_urls:
                    yt = pytube.YouTube(url)
                    title = yt.title
                    
                    audio = yt.streams.get_audio_only()
                    title_ext = title + str(".mp3")
                    
                    audio.download(output_path=folder_a, filename=title_ext)     # type: ignore
                    
                    print("Music {} downloaded: {}".format(count, title_ext))
                    
                    count += 1
                    
                print("")    
                print("Musics have been downloaded in the '{}' folder"\
                    .format(folder_a))
                
            else:
                print("Invalid option")
                print("--------------")
                _download() 
            
        _download()

        break
