import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit as kit
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1])
engine.setProperty('voice',voices[1].id)
suraj="+91 92845 45328"
siddarthsir="+91 95457 90418"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Bhushan")
    elif hour>12 and hour<18:
        speak("Good afternoon Bhushan")
    else: speak("Good NIght Bhushan")
    speak("I am your personal assistant! How can I help you?")

def takeCommand():
    # converts sound from mic to string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("can you repeat please...?")
        return "Some thing went wrong Bhushan! Sorry"
    return query

if __name__ == '__main__':
    # speak("Whatsup dude? Hows it going?")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            try:
                speak("Searching Wikipedia")
                query = query.replace("wikipedia","")
                results = wikipedia.summary(query,sentences=2)
                speak("Wikipedia Says...")
                print(results)
                speak(results)
            except Exception as e:
                speak("Something went wrong Bhushan")
                speak("Can you repeat again")
                takeCommand()

        elif 'open youtube' in query:
            speak("Opening Youtube")
            webbrowser.open_new("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open_new("google.com")
        elif 'open gmail' in query:
            speak("opening gmail")
            webbrowser.open("gmail.com")


        elif 'open screenshot' in query:
            codePath = "D:\Pictures\Screenshots"
            os.startfile(codePath)
            takeCommand()
        elif 'open drive' in query:
            codePath = "C:/"
            os.startfile(codePath)
            takeCommand()

        elif 'whatsapp suraj' in query:
            speak("what do you want to send?")
            kit.sendwhatmsg(suraj,takeCommand(), 15,00)
            speak("message will be sent")
            takeCommand()
        elif 'whatsapp siddarth sir' in query:
            speak("what do you want to send?")
            kit.sendwhatmsg(siddarthsir,takeCommand(), 17,47)


