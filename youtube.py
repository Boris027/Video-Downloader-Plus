from pytube import YouTube
import flet as ft
import os
import moviepy.editor as mpe

import sys
output = open("output.txt", "wt")
sys.stdout = output
sys.stderr = output

namevideo='V.mp4'
nameaudio='A.mp4'


#download the video
def downloader(url,itag1):
    try:
        print(url)
        print(itag1)
        #print(url)
        
        
        y=YouTube(url)
        
        #download video
        streams=y.streams.get_by_itag(itag1)
        print(streams)
        streams.download()
        os.rename(streams.default_filename,namevideo)
        print('video downloaded')
        #download audio
        streams2=y.streams.filter(only_audio=True).first()
        print(streams2)
        streams2.download()
        os.rename(streams2.default_filename,nameaudio)
        print('audio download')
        
        audio=mpe.AudioFileClip(nameaudio)
        video=mpe.VideoFileClip(namevideo)
        final=video.set_audio(audio)
        final.write_videofile(streams.default_filename)
        print('video merged')
        os.remove(namevideo)
        os.remove(nameaudio)
    except:
        os.remove(namevideo)
        os.remove(nameaudio)
        print('error while downloading the video or audio')


title=[]
#get the name from the video
def getname(url,page:ft.Page):
    cleantitle(page)
    try:
        yt=YouTube(url)
        title.append(ft.Text(value=yt.title))
        page.add(title[len(title)-1])
    except:
        print('error getting the video name')

#where put the code of the buttons
arraybuttons=[]
#get the resolutions for the video
def getresolutions(url,page:ft.Page): #,page:ft.Page
    cleanarray(page)
    print(len(arraybuttons))
    try:
         yt=YouTube(url)
         arrayresolutions=yt.streams.order_by('resolution').filter(file_extension='mp4')
         for x in arrayresolutions:
             print(x)
             text1=x.resolution+'/'+str(x.fps)+'fps'
             #page.add(ft.FilledButton(text=text1,data=x.itag,on_click=lambda event, itag=x.itag :downloader(url,itag) ))
             arraybuttons.append(ft.FilledButton(text=text1,data=x.itag,on_click=lambda event, itag=x.itag :downloader(url,itag) ))
             page.add(arraybuttons[len(arraybuttons)-1])
    except Exception as e:
        print('error getting the resolutions')
        print(e)
    
#clean the array 
def cleanarray(page:ft.Page):
    try:
        for x in arraybuttons:
            page.remove(x)
        arraybuttons.clear()
    except:
        print('Error while cleaning the array')
    
def cleantitle(page:ft.Page):
    try:
        for x in title:
            page.remove(x)
        title.clear()
    except:
        print('Error while cleaning the array')
    

#getresolutions('https://www.youtube.com/watch?v=kfJMECoNFXk')