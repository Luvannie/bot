import pyttsx3
import datetime
import speech_recognition as s
import webbrowser as wb
Friday=pyttsx3.init()
voice= Friday.getProperty('voices')
Friday.setProperty('voice',voice[1].id)
def speak(audio):
    print("F.R.I.D.A.Y: "+ audio)
    Friday.say(audio)
    Friday.runAndWait()
def time():
    Time=datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)
def welcome():
    hour=datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning Sir")
    elif hour >= 12 and hour<18:
        speak("Good afternoom Sir")
    elif hour >=18 and hour <24:
        speak("Good evening Sir")
    else :
        speak("Good night Sir")
    speak("How can i help you")

def command():
    order= s.Recognizer()
    with s.Microphone() as source:
        order.pause_threshold= 2
        audio= order.listen(source)
    try:
        query=order.recognize_google(audio,language='en')
        print("Luvannie :"+ query)
    except s.UnknownValueError:
        print("Please repeat or typing the command")
        query= str(input("your order is: "))
    return query

    

if __name__=="__main__":
    welcome()
    while True:
        print("************************")
        query= command().lower()
        if "google" in query:
            speak("What should i search boss ?")
            search_word=command().lower()
            u=f"https://www.google.com/search?q={search_word}"
            wb.get().open(u)
            speak(f"Here is your {search_word} on Google")
        elif "youtube" in query:
            speak("What should i search boss ?")
            search_word=command().lower()
            u=f"https://www.youtube.com/search?q={search_word}"
            wb.get().open(u)
            speak(f"Here is your {search_word} on Youtube")
        elif query=="what's your name?":
            speak("My name is Friday")
            print("My name is Friday")
        elif "time" in query:
            time()
        elif "quit" or "shutdown" in query:
            speak(" turn off, good bye sir")
            break
        else:
            speak("I don't understand your order, try again")
    