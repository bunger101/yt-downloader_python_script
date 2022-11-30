I created this script for personal uses with the "pytube" library.

The unique library needed to be installed is pytube with the command:
"pip install pytube"

Videos will be created in the actual directory "yt-downloader" you have with 
new folders in, created by the script. You could change it modifying the 
necessary rows in the code.

The root should be:
"/home/YOUR_USER_PATH_HERE/yt-downloader"
(You could change those parameters, in the ""line 9"" and ""line 17"")

,and the folders created:

1- "output-hq/" for the highest quality videos in ".mp4" extension.
2- "output-lq/" for the lowest quality videos in ".mp4" extension.
3- "output-a/" for the audio in ".mp3" extension.

Also it will be created a file with the name "download_compilation.txt" where
all downloads ar archived to have a data follow of the time every download
was effected. 

Videos formats accepted (as I know, maybe could be other ones):
· https://www.youtube.com/watch?v=ICzJvJpbALk

Playlists formats accepted (as I know, maybe could be other ones):
· https://www.youtube.com/playlist?list=PLba0qjqjWby7Sga35PEcYTahVH3xF3TY2
· https://www.youtube.com/watch?v=hMkkLQxJOac&list=PLba0qjqjWby7Sga35PEcYTahVH3xF3TY2&index=1

(I think it's sufficient).


"---------------------------------IMPORTANT-----------------------------------"

THIS SCRIPT IT HAS  A SOLVING FOR VIDEOS THAT INCLUDES A
SLASH LINE ("/") IN THE VIDEOS TITLES. FOR EXAMPLE:

>Title 1: "歌詞付き】 REPLAY/三代目 J SOUL BROTHERS from EXILE TRIBE"
>Title 2: "Mind Relax Lo-fi | Mashup Lofi Songs | Feel The Music | Remix / Lofi/"

IT'S NOT ANYMORE A PROBLEM because all those strange characters are ignored
in the ""line 36"" where the "list_comand" variable is defined. 
If you want to exlude any other character you just need to introduce it in this 
variable.

"-----------------------------------------------------------------------------"

Also in the ""line 38"" you can change, if you desire, the maximum length
the string, defined in the variable "title", must have.

Hope it was useful for you.

Thanks.