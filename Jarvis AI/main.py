import pyttsx3
import speech_recognition as sr
import datetime
import armstrong
import os
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening....")
        uinput = r.listen(m)
        r.pause_threshold = 1
        query = r.recognize_google(uinput, language="en-in")
        return query

def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning! Sir I am Jarvis how may I help you?")

    elif hour>=12 and hour<18:
        speak("Good Afternoon! Sir I am Jarvis how may I help you?")

    else:
        speak("Good Evening! Sir I am Jarvis how may I help you?")


if __name__ == "__main__":
    wishme()
    
    jarvistm = True
    while jarvistm:
        userinput = takeCommand().lower()
        # print(userinput)
        if 'date' in userinput:
            print(userinput)
            print("Sir, The date is ", datetime.datetime.today().strftime('%d'))
            print("The Month is", datetime.datetime.today().strftime('%m'))
            print("and the year is", datetime.datetime.today().strftime('%Y'))
            
            speak("Sir, The date is " + datetime.datetime.today().strftime('%d'))
            speak("The Month is " + datetime.datetime.today().strftime('%m'))
            speak("and the year is " + datetime.datetime.today().strftime('%Y'))
        
        elif 'find armstrong number' in userinput:
            print(userinput)
            speak("Sir, Please speak the armstrong number")
            # second microphone
            with sr.Microphone() as m1:
                print("sir, please speak the armstrong number")
                uinput1 = r.listen(m1)
                query1 = r.recognize_google(uinput1, language="en-in")
                armstrong.func(int(query1))
        elif 'open code' in userinput:
            print(userinput)
            print("Opening Visual Studio Code...")
            speak("Opening Visual Studio Code...")
            os.startfile(r"C:\Users\Krrish Bhandari\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif 'wikipedia' in userinput:
            print(userinput)
            userinput = userinput.replace("wikipedia", "")
            results = wikipedia.summary(userinput, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open google' in userinput:
            print(userinput)
            speak("Opening Google....")
            webbrowser.open("https://www.google.com/")
        
        elif 'open youtube' in userinput:
            print(userinput)
            speak("Opening Youtube....")
            webbrowser.open("https://www.youtube.com/")
        
        elif 'open my online reference' in userinput:
            print(userinput)
            speak("Opening your reference....")
            webbrowser.open("http://krrishbhandari.hyperphp.com/")

        elif 'exit' in userinput:
            print("bye")
            speak("Good Bye Sir....")
            jarvistm = False