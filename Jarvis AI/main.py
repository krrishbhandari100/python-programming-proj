try:
    import pyttsx3
    import speech_recognition as sr
    import datetime
    import os
    import wikipedia
    import webbrowser
    import requests
    import pywhatkit
except Exception as e:
    print(e)
    print("there are some issues in app this might conflict")

# all functions
def func(num):
    # num = int(input("Enter a number: "))
    if(num==""):
        print("blank not allowed")
    else:
        num = int(num)
        # Changed num variable to string,
        # and calculated the length (number of digits)
        order = len(str(num))

        # initialize sum
        sum = 0

        # find the sum of the cube of each digit
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10

        # display the result
        if num == sum:
            return num, "is an armstrong number"
        else:
            return num, "is not an armstrong number"

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as m:
        print("Listening....")
        uinput = r.listen(m)
        r.pause_threshold = 1
        query = r.recognize_google(uinput, language="en-in")
        print(query)
        return query

def takeCommandForArmstrong():
    r1 = sr.Recognizer()
    with sr.Microphone() as m1:
        print("Listening Your Number....")
        uinput1 = r1.listen(m1)
        r1.pause_threshold = 1
        query1 = r1.recognize_google(uinput1, language="en-in")
        print(query1)
        res = func(int(query1))
        print(res)
        speak(res)

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
            speak("Sir, Please speak the armstrong number")
            takeCommandForArmstrong()
                
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
        elif 'google' in userinput:
            print(userinput)
            userinput = userinput.replace("google", "")
            pywhatkit.search(userinput)
        
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
        
        elif 'ip' in userinput:
            ip = requests.get('https://api.ipify.org/').text
            tos = f"Sir your ip address is {ip}"
            print(ip)
            speak(tos)
        
        elif 'who are you' in userinput:
            speak("Sir, I am Jarvis, Your Assistant and I will be making your work easier")

        elif 'exit' in userinput:
            print("bye")
            speak("Good Bye Sir....")
            jarvistm = False
        else:
            speak("The function you want is not there in me, Sorry for inconvenience caused")