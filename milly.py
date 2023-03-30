
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Make a function to speak something
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Make a function to wish me according to time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Milly Sir. Please tell me how may I help you")

def takeCommand():
    # It takes microhone input from the user and return string output

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
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    # call wish me function
    wishMe()
    
    while True:
        query = takeCommand().lower()

        # Logic for executing task based on query

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open hackerrank' in query:
            webbrowser.open("hackerrank.com")

        elif 'open javatpoint' in query:
            webbrowser.open("javatpoint.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoerflow.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\HP\\Music\\Half_girlfriend'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'your name' in query:
            speak("My name is Milly Sir. Speed 1 terahertz, Memory 1 Zigabyte.")

        elif 'about you' in query:
            speak("Hi, I am Milly, the Robot. Speed 1 terahertz, Memory 1 Zigabyte.")

        elif 'sorry' in query:
            speak("i don't have feeling. I am a robot")

        elif 'good morning' in query:
            speak("Good Morning")

        elif 'good afternoon' in query:
            speak("Good Afternoon")

        elif 'good evening' in query:
            speak("Good Evening")
        
        elif 'how are you' in query:
            speak("I am fine sir. How are you")

        elif 'quit' in query:
            exit()

        elif 'exit' in query:
            exit()

        elif 'close' in query:
            exit()