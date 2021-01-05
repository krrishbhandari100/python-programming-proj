import pyttsx3
import speech_recognition as sr
import datetime
import armstrong
import os

r = sr.Recognizer()

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    print("Good Morning Sir, I am Jarvis, How may I help you?")
    speak("Good Morning Sir, I am Jarvis How may I help you?")
    print("Listening....")
    with sr.Microphone() as m:
        uinput = r.listen(m)
        query = r.recognize_google(uinput, language="en-in")
        # print(query)
    if 1:
        userinput = query.lower()
        if 'date' in userinput:
            print("Sir, The date is ", datetime.datetime.today().strftime('%d'))
            print("The Month is", datetime.datetime.today().strftime('%m'))
            print("and the year is", datetime.datetime.today().strftime('%Y'))
            
            speak("Sir, The date is " + datetime.datetime.today().strftime('%d'))
            speak("The Month is " + datetime.datetime.today().strftime('%m'))
            speak("and the year is " + datetime.datetime.today().strftime('%Y'))
        elif 'find armstrong number' in userinput:
            speak("Sir, Please speak the armstrong number")
            # second microphone
            with sr.Microphone() as m1:
                print("sir, please speak the armstrong number")
                uinput1 = r.listen(m1)
                query1 = r.recognize_google(uinput1, language="en-in")
                armstrong.func(int(query1))
        elif 'open code' in userinput:
            print("Opening Visual Studio Code...")
            speak("Opening Visual Studio Code...")
            os.startfile(r"C:\Users\Krrish Bhandari\AppData\Local\Programs\Microsoft VS Code\Code.exe")
