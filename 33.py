import pyttsx3 # T2s
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os

import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sunshine, Rise and Shine !")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Takao. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Here you go to YOUTUBE")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Here you go to google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("here you go to stack overflow")
            webbrowser.open("stackoverflow.com")   
        elif 'open code safe' in query:
            speak("here you go to codechef")
            webbrowser.open("codechef.com")
        elif 'open hacker rank' in query:
            webbrowser.open("hackerrank.com")
        elif 'github' in query:
            webbrowser.open("github.com")


        elif 'play music' in query:
            music_dir = "C:\\Users\\PS\\Music"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"mam, the time is {strTime}")

        

        elif "what's your name" in query or "What is your name" in query:
            speak("My name is TAKAO.")
            print("My name is  TAKAO")
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Priya.")
            print("I have been created by Priya.")
        elif 'joke' in query:
            speak(pyjokes.get_joke())
        elif "taka" in query:
            speak("Yes, i am listening, Priya")
        elif "thank you" in query:
            speak("You are most welcome Priya.")
        elif "why should we use you" in query:
            speak("you ever wondered how cool it would be to have your own A.I. assistant? Imagine how easier it would be to send emails without typing a single word, doing Wikipedia searches without opening web browsers, and performing many other daily tasks like playing music with the help of a single voice command.")

        elif "what can you do" in query:
            speak("I can do Wikipedia searchs, open any website that you want to visit,make you laugh and many more things.")

        elif "who i am" in query:
            speak("If you talk then definitely your human.")
        
