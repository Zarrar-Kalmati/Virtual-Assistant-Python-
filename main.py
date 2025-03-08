import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import os


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://www.instagram.com")
    elif "shutdown" in c.lower():
        os.system("shutdown /s /t 0")
    elif "restart" in c.lower():
        os.system("shutdown /r /t 0")
    elif "open whatsapp" in c.lower():
        os.system("start whatsapp")
    elif "open calculator" in c.lower():
        os.system("calc")
    elif "open file" in c.lower():
        os.system("explorer")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Initializing Python....")
    while True:
        # Listen for the wake word "Python"
        # obtain audio from the microphone
        r = sr.Recognizer()
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "python"):
                speak("Yeah")
                # Listen for command
                with sr.Microphone() as source:
                    print("Python Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
