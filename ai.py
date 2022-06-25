import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Austin Sir. PLease how may I be of your service?")

def takeCommand():

r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio =r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('austinchrisiwu@gmail.com','Austin321')
    server.sendmail('austinchrisiwu@gmail.com'to, content)
    server.close()

    if_name_== "__main__":
        wishMe()
        while True:
            query = takeCommand().lower()

            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'play music' in query:
                music_dir = ""
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'open code' in  query:
                codePath = 'c:\Users\HP\OneDrive\Desktop\new'
                os.startfile(codePath)

            elif 'email to friend' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "iwuaustinchris@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")

                except Exception as e:
                    print(e)
                    speak("Sorry, I am not able to send this mail")
    