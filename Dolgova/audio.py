
import pyttsx3

engine = pyttsx3.init()
engine.say(input('Введите: '))
engine.runAndWait()