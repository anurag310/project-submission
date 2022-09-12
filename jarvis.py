'''from tkinter.tix import MAIN
from pip import main'''
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishME():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<17:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("hey, I am Anurag Welcome . How may i help you?")


def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your=password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

def takeCommand():
    '''It takes microphone input from the user and returns the string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        print(e)

        print("Please,Say that again..")
        return "None"
    return query


if __name__ == "__main__":
    #speak("Anurag is good boy")
    wishME()
    #while True:
    if 1:
        query = takeCommand().lower()

    #logic for executing task based query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak("Accoding to wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'play music' in query:
            music_dir = "C:\\music"
            songs = os.listdir(music_dir)
            a = random.choice(songs)
            os.startfile(os.path.join(music_dir,a))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Anurag\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open chrome' in query:
            path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)

        elif 'email to anurag' in query:
            try:
                speak("What should i say?")
                content = takeCommand()
                to = "anuragyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend , I am not able to sent the email right now")