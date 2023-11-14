import pyttsx3
import speech_recognition as sr

tts = pyttsx3.init()
rate = tts.getProperty('rate')
tts.setProperty('rate', rate-40)

volume = tts.getProperty('volume') 
tts.setProperty('volume', volume+0.9)

voices = tts.getProperty('voices')

tts.setProperty('voice', 'ru') 

for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice', voice.id)


def record_volume():
   print("Пишите: ")
   text = input()
   tts.say(text)
   tts.runAndWait()
    

while True:
    
    record_volume()