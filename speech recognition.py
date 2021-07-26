import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import json
import requests
import getpass
import time
from time import ctime

username= getpass.getuser()
r=sr.Recognizer()
t = datetime.datetime.now()

def Jarvis(audio_string):
    engine = pyttsx3.init()
    print(audio_string)
    engine.say(audio_string)
    engine.runAndWait()


def begin():
    time=t.hour
    if time>=0 and time<12:
        Jarvis('Hey {}, Good morning, What can I do for you ?'.format(username))
    elif time>=12 and time<16:
        Jarvis('Hey {},good afternoon, What can I do for you ?'.format(username))
    else:
        Jarvis('Hey {}, Good evening, What can I do for you ?'.format(username))

def listen():
    
    with sr.Microphone() as source:
        print('listening')
        audio=r.listen(source) 
        voice_data=" "
        try:
            voice_data=r.recognize_google(audio,language='en-in')
            print(username+" : "+ voice_data)

        except:
            Jarvis("Pardon me, please say that again")
            return "None"
    return voice_data

def Jarvis_speaks(voice_data):
    if "your name" in voice_data:
        Jarvis("Hi, I am Jarvis.")
    if "time" in voice_data:
        tim=str(ctime())
        Jarvis(tim)
    if "exit" in voice_data:
        Jarvis("Good bye {}".format(username))
        exit()
    if "shutdown" in voice_data:
        Jarvis("Shutting down the computer, Bye  {}".format(username))
        os.system('shutdown /s /t 10')
    if 'open Google' in voice_data:
        Jarvis("Here you go ")
        webbrowser.open("https://www.google.com")
    if "restart" in voice_data:
        Jarvis(" Restarting the computer, meet you soon {}".format(username))
        os.system('shutdown /r /t 10')
    if "search" in voice_data:
        Jarvis("What do you wanna search for?")
        vdata=listen()
        Jarvis("Searching for {} in google".format(vdata))
        webbrowser.open("https://www.google.com/search?q="+vdata)
    if "YouTube" in voice_data:
        Jarvis("Starting YouTube.")
        webbrowser.open("https://www.youtube.com/")
begin() 
while True:
    voice_data=listen()
    Jarvis_speaks(voice_data)