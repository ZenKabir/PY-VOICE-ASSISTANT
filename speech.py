import os
import time
import playsound
from gtts import gTTS
from pyttsx3 import engine
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import pyttsx3

davina = pyttsx3.init()
davina.setProperty("rate", 120)
while True:
    

    def get_audio():
     r = sr.Recognizer()
     with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            davina.say('Sorry I Didnt catch that do you mind repeating it?'+str(e))
     return said
    

    apps = []
    warzone = "C:\\Users\\zenka\\Desktop\\Battle.net\\Battle.net.exe"
    

    def runApps():
        os.startfile(warzone)

    def runDiscord():
        os.startfile("C:\\Users\\zenka\\Documents\Discord\\app-1.0.9001\\Discord.exe")
        
    def mainApp():
        os.startfile('C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Brave.lnk')
        os.startfile('C:\\Users\\zenka\\AppData\\Roaming\\Microsoft\Windows\\Start Menu\Programs\\Visual Studio Code\\Visual Studio Code.lnk')

    text = get_audio()


    if 'hello' in text:
     davina.say('Hey , I am your personal python assisstant . what is your name.')
     davina.runAndWait()
     name = get_audio()
     davina.say('Hello there,'+name)
     davina.runAndWait
     davina.say('My name is Davina')
     davina.runAndWait()

    if 'Davina Run games' in text:
     runApps()

    if 'Davina run discord' in text:
        runDiscord()

    if 'Davina exit' in text:
        davina.say('terminating  program and deleting all your files')
        davina.runAndWait()
        sys.exit()
    if 'Davina play music' in text:
        os.startfile('C:\\Users\\zenka\\Documents\\VOICE ASSISTANT\\relax.mp3')


    if 'Davina shut down my computer' in text:
        davina.say("Shutting system down")
        davina.runAndWait()
        os.system("shutdown /s /t 1")

    if 'Davina play drill' in text:
        os.startfile('C:\\Users\\zenka\Documents\\VOICE ASSISTANT\\drill.mp3')

    if 'Davina play red bone' in text:
        os.startfile('C:\\Users\\zenka\Documents\\VOICE ASSISTANT\\song.mp3')

    if 'Davina code' in text:
        mainApp()
    if 'Davina what makes a good burger' in text:
        davina.say('If it naaarrggggh go moo, you know what to do')
        davina.runAndWait()
    
        

    

    
        

            

           
            
            


    



    
