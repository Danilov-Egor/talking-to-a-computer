import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
from gtts import gTTS
import smtplib

def talk(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en', slow = False)
    tts.save('audio1.mp3')
    os.system('start audio1.mp3')
    
    
def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 2
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        zadanie = r.recognize_google(audio).lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("I didn't understand")
        zadanie = command()
    return zadanie

def makeSomething(zadanie):
    if 'open wikipedia' in zadanie:
        talk("Opening")
        url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
        webbrowser.open(url)
    elif 'open vk' in zadanie:
        talk("Opening")
        url = 'https://vk.com/feed'
        webbrowser.open(url)
    elif 'how are you doing' in zadanie:
        talk("I am doing alright how are you")
    elif 'stop' in zadanie:
        talk("goodbye")
        sys.exit()

talk("hello, ask me something")

while True:
    makeSomething(command())
