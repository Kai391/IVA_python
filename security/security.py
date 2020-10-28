import os
from win32com.client import Dispatch
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__ == "__main__":
    speak("Please Varify your self")
    speak("Write your name please")
    name=input('name: ')
    if name == "krishna"  or name == "krishna murti dubey" or name=="Krishna" or name == "Krishna Murti" or name == "Krishna Murti Dubey" or name=="krishna murti":
        print("It's okay Boss")
        speak("It's okay Boss")
        # speak("Boss")
        exit()
    else:
        shutdown="shutdown /s /t 5"
        print("Unauthorized person can't access system")
        speak("Unauthorized person can't access system")
        print('system will be shutdown in t-5sec')
        speak('system will be shutdown in t minus 5sec')
        os.system(shutdown)
        exit()