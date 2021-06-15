import pyttsx3
import speech_recognition as sr
import time

engine = pyttsx3.init('sapi5')
voice= engine.getProperty('voices')
engine.setProperty('voice', 'voice[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

class tc():

    def takeCommand():
        r = sr.Recognizer()
        r.pause_threshold = 1
        r.energy_threshold = 1000
        r.dynamic_energy_threshold = False
        with sr.Microphone() as source:
            speak("Listening Now")
            audio = r.listen(source)
                
        try:
            #begin = time.time()
            tc.query = r.recognize_google(audio, language='en-in').lower()
            #print(f"User said: {tc.query}\n")
                
        except Exception:
            speak("Say that again please... or check your internet connection")
            return None
        #end = time.time()

        #print(f"Total time for speech recog {end - begin}")
        
    def speak_for_me():
        mic = sr.Recognizer()
        mic.pause_threshold = 1
        mic.energy_threshold = 1000
        mic.dynamic_energy_threshold = False
        with sr.Microphone() as input:
            speak("Speak now")
            sound = mic.listen(input)
        try:
            tc.query2 = mic.recognize_google(sound, language='en-in').lower()
            #print(f"   User said: {query2}\n")
            
        except Exception:
            speak("Say that again please... or check your internet connection")
            return tc.speak_for_me()
