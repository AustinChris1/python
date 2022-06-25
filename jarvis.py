import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import time
from word2number import w2n
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning boss!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon boss!")   

    else:
        speak("Good Evening boss!")  
    speak("Welcome back! I'm Austin's Assistant, Please tell me how I may help you?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    # content = MIMEMultipart()
    # fromaddr = "info@spectrawebx.xyz"
    # to = "iwuaustinchris@gmail.com"
    # msg = MIMEMultipart()
    # msg['From'] = fromaddr
    # msg['To'] = to
    # msg['Subject'] = "Test Subject"
    # content = "Write your message here"
    # msg.attach(MIMEText(content, 'plain'))
    # server = smtplib.SMTP('server236.web-hosting.com:465')
    # server.starttls()
    # server.login(fromaddr, "Blabla789?")
    # text = msg.as_string()
    # server.sendmail(fromaddr, to, text)
    # server.quit()
    server = smtplib.SMTP('smtp.gmail.com', 465)
    server.ehlo()
    server.starttls()
    server.login('spectrawebx@gmail.com', 'Spectra321')
    server.sendmail('spectrawebx@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            try:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to search this ")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'close' in query:
            try:
                speak("What should I close?")
                content = takeCommand()
                run = "taskkill /im "
                end = ".exe /f"
                program = run + content + end
                os.system(program)
            except Exception as e:
                print(e)
                speak(e)
                speak("Sorry, I am not able to run this command ")

        elif 'open' in query:
            try:
                speak("Which app should I open?")
                content = takeCommand()
                run = "start "
                end = ".exe /f"
                program = run + content + end
                os.system(program)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to run this command ")

        elif 'open google' in query:
            webbrowser.open("google.com")


        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'today' in query:
            try:
                date = datetime.datetime.now().strftime("%A, %B %d, %Y")
                print(date)
                speak(date)
            except Exception as e:
                print(e)
                speak(e)
                speak("Can't do this")


        elif 'music' in query:
            try:
                music_dir = 'C:\\Users\\HP\\bluetooth\\'
                songs = os.listdir(music_dir)
                speak("Your music will start playing soon")
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
                time.sleep(60*10)
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to run this command ")
                speak(e)

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")    
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        elif 'open code' in query:
            codePath = "cargame.py"
            os.startfile(codePath)

        elif 'hello' in query:
            speak("I am still at your service, sir!")

        elif 'folder' in query:
            try:
                speak("Name of folder please?")
                name = takeCommand()
                speak("Where should I create the folder?")
                where = takeCommand()
                if where == "desktop":
                    speak("I am creating a folder by name "+ name +"and it will be located on Desktop")
                    os.chdir('C:/Users/HP/OneDrive/Desktop/')
                    os.makedirs(name)
                    speak('Folder' + name + 'created successfully')
                else:
                    speak("I am creating a folder by name "+ name +"and it will be located on " + where)
                    os.chdir('C:/Users/HP/OneDrive/Desktop/' + where)
                    os.makedirs(name)
                    speak('Folder' + name + 'created successfully')
            except Exception as e:
                speak(e)
                print(e)
                speak("Sorry, can't run this command")

        elif 'delete' in query:
            try:
                speak("Name of folder please?")
                name = takeCommand()
                speak("Where should I delete the folder?")
                where = takeCommand()
                if where == "desktop":
                    speak("I am deleting a folder by name "+ name +"and it will be located on Desktop")
                    os.chdir('C:/Users/HP/OneDrive/Desktop/')
                    os.removedirs(name)
                    speak('Folder' + name + 'delete successfully')
                else:
                    speak("I am deleting a folder by name "+ name +"and it will be located on " + where)
                    os.chdir('C:/Users/HP/OneDrive/Desktop/' + where)
                    os.removedirs(name)
                    speak('Folder' + name + 'deleted successfully')
            except Exception as e:
                speak(e)
                print(e)
                speak("Sorry, can't run this command")

        elif 'good job' in query:
             speak("Thank you boss!")

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "iwuaustinchris@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email") 

        elif 'search' in query:
            try:
                speak("What should I search?")
                content = takeCommand()
                word = "https://www.google.com/search?q="
                total = word + content    
                webbrowser.open(total)
                speak("Please wait your result is loading!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to search this ")    
        
        elif 'rest' in query:
            try:
                speak("For how long boss?")
                rest_time = takeCommand()
                print(rest_time)
                mainrest = w2n.word_to_num(rest_time)
                string = "I would rest for "
                totalRest = string + str(mainrest) + "seconds"
                speak(totalRest)
                time.sleep(mainrest)
                speak("I'm back boss")
            except Exception as e:
                print(e)
                speak("Sorry, I didn't hear you.") 

        elif 'goodbye' in query:
            try:
                speak("Alright, goodbye boss!")
                exit()
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to run this command") 
