# abhi isme specific song select karne ka code nh hai.
# abhi specific jagah vscode open karne ka code nh.
# abhi specific software open nh hota hai.
# abhi voice typing bhi nh hai.
# abhi isme web search nh hai.
# abhi isme wekipidia search nh hai.
# abhi isme security bhi nh hai.
# abhi isme newsreader nh hai.
# abhi isme language translator bhi nh hai.
# abhi isme machine aur deep learning bhi karni hai.
import requests
import pyttsx3
import speech_recognition as sr
import os
import os
import random
from pygame import mixer
while(True):
    try:
        requests.get("https://www.google.com/")
        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices= engine.getProperty('voices')
            # print(voices[1].id)
            engine.setProperty('voice',voices[0].id)
            engine.say(audio)
            engine.runAndWait()
        def listen():
            try:
                requests.get("https://www.google.com/")
                pass
            except:
                print("No connection")
                speak("Boass the internet connection is gone.")
                # exit()
                exit()
            r=sr.Recognizer()
            with sr.Microphone() as source:
                if x==1:
                    print("Hello, I am Maxi...")
                elif x==2:
                    print("Listening...")
                r.pause_threshold=1
                audio=r.listen(source)
                try:
                    text=r.recognize_google(audio)
                    return text
                except:
                    return "abcdefghijklmnop"
        def music(m):
            mixer.init()
            mixer.music.load(m)
            mixer.music.set_volume(0.7)
            mixer.music.play()
        while(True):
            x=1
            text=listen()
            # print(text)
            text=text.lower()
            if 'abcdefghijklmnop' in text:
                os.system('cls')
                pass
            elif 'maxi' in text:
                x=2
                # print('y')
                l=['Yes boass','Haa boass']
                r=random.choice(l)
                speak(r)
                print(r)
                y=0
                while(y<5):
                    t=listen()
                    t=t.lower()
                    if 'abcdefghijklmnop' in t:
                        print('sorry')
                        y+=1
                    else:
                        print(f"you said: {t}")
                        f=f'{t}'
                        if "file" in f:
                            if 'open file' in f:
                                f=f.replace('open file ','')
                                pass
                            elif 'file' in f:
                                f=f.replace('file ','')
                                pass                    
                            p=r'C:\Users\KAi\Desktop'
                            
                                # print(p)
                            # print(p)
                            
                            os.chdir(p)
                            l=os.listdir(p)
                            # print(l)
                            for i in l:
                                # print(i)
                                I=i.split('.')
                                # print(I)
                                # print(I[1])
                                try:
                                    t=I[1]
                                    f=f.lower()
                                    F=f"{f}.{t}"
                                    # print("s")
                                    if F in i:
                                        # print("l")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        y=5
                                        break
                                    f=f.capitalize()
                                    F=f"{f}.{t}"
                                    # print("y")
                                    if F in i:
                                        # print("c")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        y=5
                                        break
                                    f=f.upper()
                                    F=f"{f}.{t}"
                                    # print("y")
                                    if F in i:
                                        # print("u")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        y=5
                                        break
                                except:
                                    pass
                            else:
                                a=0
                                while(a<1):
                                    speak("boass")
                                    print("FIle is not in this root or file doesn't exist.")
                                    speak("FIle is not in this root or file doesn't exist.")
                                    print("Your current directory:",os.getcwd())
                                    print("The files and folders in current directory:",l)
                                    speak("Now you can see files and folder here boass")
                                    speak('boass you can change directory here')
                                    b=0
                                    while(b<1):
                                        try: 
                                            i=listen()
                                            if i in 'abcdefghijklmnop':
                                                print('sorry')
                                                pass
                                            elif i == 'exit':
                                                a+=1
                                                b+=1
                                                speak('okay Boass')
                                                print("Exit")
                                                speak("Exit")
                                            else:
                                                print(f"dir: {i}")
                                                
                                                if i == 'Out' or i == 'Bahar aao' or i == 'Comeout' or i == 'Come out' or i == 'come out' or i == 'Bahar aao' or i == 'out' or i == 'comeout':
                                                    i="../"
                                                P=f'\\{i}'
                                                p=p+P
                                                # print(p)
                                                try:
                                                    os.chdir(p)
                                                    print("Your current directory:",os.getcwd())
                                                    l=os.listdir(p)
                                                    print("The files and folders in current directory:",l)
                                                    for i in l:
                                                        # print(i)
                                                        I=i.split('.')
                                                        # print(I)
                                                        # print(I[1])
                                                        try:
                                                            # f=f.replace('open file ','')
                                                            t=I[1]
                                                            f=f.lower()
                                                            F=f"{f}.{t}"
                                                            # print(F)
                                                            # print("s")
                                                            if F in i:
                                                                # print("l")
                                                                speak("file found boass")
                                                                speak(f"opening file {F}")
                                                                os.system(f'start {F}')
                                                                a+=1
                                                                b+=1
                                                                y=5
                                                                break

                                                            f=f.capitalize()
                                                            F=f"{f}.{t}"
                                                            # print("y")
                                                            if F in i:
                                                                # print("c")
                                                                speak("file found boass")
                                                                speak(f"opening file {F}")
                                                                os.system(f'start {F}')
                                                                a+=1
                                                                b+=1
                                                                y=5
                                                                break
                                                        
                                                            f=f.upper()
                                                            F=f"{f}.{t}"
                                                            # print("y")
                                                            if F in i:
                                                                # print("u")
                                                                speak("file found boass")
                                                                speak(f"opening file {F}")
                                                                os.system(f'start {F}')
                                                                a+=1
                                                                b+=1
                                                                y=5
                                                                break
                                                        except:
                                                            pass
                                                except:
                                                    speak("No such folder or file exist please make sure you type correct name.")
                                                    p=r'C:\Users\KAi\Desktop'
                                                    os.chdir(p)
                                                    print("Your current directory:",os.getcwd())
                                                    l=os.listdir(p)
                                                    print("The files and folders in current directory:",l)
                                                    pass
                                                    
                                        except:
                                            pass     
                        elif "folder" in f: 
                                p=r'C:\Users\KAi\Desktop'
                                    # print(p)
                                # print(p)
                                speak("you are now in desktop directory")
                                os.chdir(p)
                                print("Your current directory:",os.getcwd())
                                l=os.listdir(p)
                                for i in l:
                                    if "." not in i:
                                        print(i)
                                else:
                                    speak("this is the current folders in desktop boass")
                                    a=0
                                    b=0
                                while(a<1): 
                                    print("Do you want to change directory: ",end="")
                                    speak("Do you want to change directory.")
                                    # print(text)
                                    while(b<1):
                                        # print("here")
                                        i=listen()
                                        if i in 'abcdefghijklmnop':
                                            print('sorry')
                                            pass
                                        else:
                                            # print("k")
                                            print(i)
                                            speak("Okay boass")
                                            if i == 'yes' or i == 'Yes' or i == 'ha' or i == 'Ha' or i == 'haa' or i == 'Haa' or i == 'han' or i == 'haan' or i == 'Haan' or i == 'Han':
                                                print("Name of folder: ",end="")
                                                speak("Please give the name of that folder")
                                                a=0
                                                while(True):
                                                    I=listen()
                                                    # print('o')
                                                    # print(I)
                                                    if I in 'abcdefghijklmnop':
                                                        print('sorry')
                                                        pass
                                                    elif I == "exit":
                                                        speak('Okay Boass')
                                                        print('Exit')
                                                        speak("exit")
                                                        b+=1
                                                        a+=1
                                                        y=5
                                                        break
                                                    else:
                                                        print(f'You said: {I}')
                                                        P=f'\\{I}'
                                                        p=p+P
                                                        try:
                                                            os.chdir(p)
                                                            speak(f"opening {I}")   
                                                            print("Your current directory:",os.getcwd())
                                                            speak(f"now you are in {I} directory")
                                                            l=os.listdir(p)
                                                            for i in l:
                                                                BOOL="." not in i 
                                                                if BOOL != False :
                                                                    print(i)
                                                                else:
                                                                    if "." in i:
                                                                        pass
                                                                    else:
                                                                        print("yes")
                                                        except:
                                                            print("Folder is not in this root or folder doesn't exist.")
                                                            speak("Folder is not in this root or folder doesn't exist.")
                                                            p=r'C:\Users\KAi\Desktop'
                                                            speak("now you are in desktop boass")
                                                            os.chdir(p)
                                                            print("Your current directory:",os.getcwd())
                                                            pass
                                            elif i == 'no' or i == 'No' or i == 'nhi' or i == 'Nhi' or i == 'na' or i == 'Na' or i == 'Nahin' or i == 'Nahi' or i == 'nahin' or i == 'nahi':
                                                speak("Okay boass")
                                                print('I stop here and exit')
                                                speak('I stop here and exit')
                                                a+=1
                                                y=5
                                                break
                                            else:
                                                print("Please speak 'yes','no' and also hindi word 'Haa' or 'nahi'")
                                                speak("Please speak correct word")
                                                pass 
                        elif 'play song' in f or 'play music' in f or 'play songs' in f or 'play musics' in f or 'play next song' in f or 'next song' in f or 'play another song' in f or 'play another music' in f or 'play next music' in f or 'next music' in f or 'another song' in f or 'another music' in f:
                            speak("okay boass")
                            p=r'C:\Users\KAi\Music'
                            os.chdir(p)
                            # print(os.getcwd())
                            l=os.listdir(p)
                            # print(l)
                            l.remove('desktop.ini')
                            while(True):
                                try:
                                    t=random.choice(l)
                                except:
                                    print('no music found')
                                    speak('boass no music found on that directory')
                                    break
                                try:
                                    speak("playing song")
                                    music(t)
                                except:
                                    print("Music doesn't play")
                                    print('please try again')
                                    speak("Music doesn't play, please try again")
                                    break
                                print(t)
                                while(True):
                                    break
                                break 
                        elif 'pause the music' in f or 'pause the song' in f or 'Pause music' in f or 'Pause song' in f:
                            try:
                                mixer.music.pause()
                            except:
                                print("no music play")
                                speak(f"boass already no {text} play")
                        elif 'resume the music' in f or 'resume the song' in f or 'resume music' in f or 'resume song' in f:
                            try:
                                mixer.music.unpause()
                            except:
                                print("no music play") 
                                speak(f"boass already no {text} play")               
                        elif 'stop the music' in f or 'stop the song' in f or 'stop music' in f or 'stop song' in f:
                            try:
                                mixer.quit()
                            except:
                                print("no music play")
                                speak(f"boass already no {text} play")
                        elif 'how are you' in f or 'kaisi ho' in f:
                            print("I am fit and fine boass")
                            speak("I am fit and fine boass")
                        elif 'who are you' in f or 'tum kon ho' in f or 'kon ho tum' in f:
                            p='I am Intelligent Voice Assistance(I V A) of this system.\nI was develop by master "Krishna" on 5 2020 August .'
                            print(p)
                            speak(p)
                        else:
                            y=2
                            y+=1
            elif 'who are you' in text or 'tum kon ho' in text or 'kon ho tum' in text:
                P='I am Intelligent Voice Assistance(I V A) of this system.\nI was develop by master "Krishna" on 5 2020 August .'
                print(P)
                speak(P)
            else:
                os.system('cls')
                pass
    except:
        def speak(audio):
            engine = pyttsx3.init('sapi5')
            voices= engine.getProperty('voices')
            # print(voices[1].id)
            engine.setProperty('voice',voices[0].id)
            engine.say(audio)
            engine.runAndWait()
        
        def music(m):
            mixer.init()
            mixer.music.load(m)
            mixer.music.set_volume(0.7)
            mixer.music.play()
        speak("boass Due to no internet connection, I only speak not listen you")
        speak("but don't worry boass, I can read you every command so type here")
        while(True):
            try:
                requests.get("https://www.google.com/")
                speak('boass, I am coming online. So, you can talk to me.')
                print("online Again")
                break
            except:
                pass
            k=input('command: ')
            speak("Okay boass")
            f=f'{k}'
            if "file" in f:
                f=f.replace('open file ','')
                p=r'C:\Users\KAi\Desktop'
                
                    # print(p)
                # print(p)
                
                os.chdir(p)
                l=os.listdir(p)
                # print(l)
                for i in l:
                    # print(i)
                    I=i.split('.')
                    # print(I)
                    # print(I[1])
                    try:
                        t=I[1]
                        f=f.lower()
                        F=f"{f}.{t}"
                        # print("s")
                        if F in i:
                            # print("l")
                            speak("file found boass")
                            speak(f"opening file {F}")
                            os.system(f'start {F}')
                            break
                        f=f.capitalize()
                        F=f"{f}.{t}"
                        # print("y")
                        if F in i:
                            # print("c")
                            speak("file found boass")
                            speak(f"opening file {F}")
                            os.system(f'start {F}')
                            break
                        f=f.upper()
                        F=f"{f}.{t}"
                        # print("y")
                        if F in i:
                            # print("u")
                            speak("file found boass")
                            speak(f"opening file {F}")
                            os.system(f'start {F}')
                            break
                    except:
                        pass
                else:
                    a=0
                    while(a<1):
                        speak("boass")
                        print("FIle is not in this root or file doesn't exist.")
                        speak("FIle is not in this root or file doesn't exist.")
                        print("Your current directory:",os.getcwd())
                        print("The files and folders in current directory:",l)
                        speak("Now you can see files and folder here boass")
                        speak('boass you can change directory here')
                        print("change dir")
                        comeout="comeout"
                        baharaao="baahar aao"
                        i=input('dir: ')
                        speak("okay boass")
                        if i == comeout or i == baharaao:
                            i="../"
                        elif i == 'exit':
                            print("exit")
                            speak("exit")
                            break
                        P=f'\\{i}'
                        p=p+P
                        # print(p)
                        try:
                            os.chdir(p)
                        
                            l=os.listdir(p)
                            # print(l)
                            for i in l:
                                # print(i)
                                I=i.split('.')
                                # print(I)
                                # print(I[1])
                                try:
                                    t=I[1]
                                    f=f.lower()
                                    F=f"{f}.{t}"
                                    # print(F)
                                    # print("s")
                                    if F in i:
                                        # print("l")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        a+=1
                                        break

                                    f=f.capitalize()
                                    F=f"{f}.{t}"
                                    # print("y")
                                    if F in i:
                                        # print("c")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        a+=1
                                        break
                                
                                    f=f.upper()
                                    F=f"{f}.{t}"
                                    # print("y")
                                    if F in i:
                                        # print("u")
                                        speak("file found boass")
                                        speak(f"opening file {F}")
                                        os.system(f'start {F}')
                                        a+=1
                                        break
                                except:
                                    pass
                        except:
                            speak("No such folder or file exist please make sure you type correct name.")
                            p=r'C:\Users\KAi\Desktop'
                            os.chdir(p)
                            speak("boass you are now in desktop")
                            pass
            elif "folder" in f:
                p=r'C:\Users\KAi\Desktop'
                os.chdir(p)
                speak("boass you are in now desktop")
                print("Your current directory:",os.getcwd())
                l=os.listdir(p)
                for i in l:
                    if "." not in i:
                        print(i)
                
                while(True): 
                    print("Do you want to change directory(yes/no): ",end="")
                    speak("Do you want to change directory yes or no")
                    i=input()
                    speak('okay boass')
                    if i == 'yes':
                        print("Name of folder: ",end="")
                        speak("boass write name of that folder")
                        I=input()
                        speak("okay boass")    
                        P=f'\\{I}'
                        p=p+P
                        try:
                            os.chdir(p)
                            print("Your current directory:",os.getcwd())
                            speak(f"boass you are in {P}")
                            l=os.listdir(p)
                            for i in l:
                                BOOL="." not in i 
                                if BOOL != False :
                                    print(i)
                                else:
                                    if "." in i:
                                        pass
                                    else:
                                        print("yes")
                        except:
                            speak("boass")
                            print("Folder is not in this root or folder doesn't exist.")
                            speak("Folder is not in this root or folder doesn't exist.")
                            p=r'C:\Users\KAi\Desktop'
                            os.chdir(p)
                            speak("boass you are in defaultly desktop")
                            print("Your current directory:",os.getcwd())
                            pass
                    elif i == 'no':
                        speak("okay boass")
                        break
                    else:
                        print("Please Type 'y' or 'n")
                        speak("boss Please Type 'yes' or 'no'")
                        pass
            elif 'play song' in f or 'play music' in f or 'play songs' in f or 'play musics' in f or 'play next song' in f or 'next song' in f or 'play another song' in f or 'play another music' in f or 'play next music' in f or 'next music' in f or 'another music' in f or 'another song' in f:
                    p=r'C:\Users\KAi\Music'
                    os.chdir(p)
                    # print(os.getcwd())
                    l=os.listdir(p)
                    # print(l)
                    l.remove('desktop.ini')
                    while(True):
                        try:
                            t=random.choice(l)
                        except:
                            print('no music found')
                            speak('boass no music found on that directory')
                            break      
                        try:
                            music(t)
                        except:
                            print("Music doesn't play")
                            print('please try again')
                            speak("Music doesn't play, please try again")
                            break
                        print(t)
                        while(True):
                            break
                        break 
            
            elif 'pause the  music' in f or 'pause the song' in f:
                try:
                    mixer.music.pause()
                except:
                    print("no music play")
                    speak("boass already no song play")
            elif 'resume the music' in f or 'resume the song' in f:
                try:
                    mixer.music.unpause()
                except:
                    print("no music play") 
                    speak("boass already no song play")               
            elif 'stop  the music' in f or 'stop the song' in f:
            
                try:
                    # mixer.music.stop()
                    mixer.quit()
                except:
                    print("no music play")
                    speak("boass already no song play")
            elif 'who are you' in text or 'tum kon ho' in text or 'kon ho tum' in text:
                P='I am Intelligent Voice Assistance(I V A) of this system.\nI was develop by master "Krishna" on 5 2020 August .'
                print(P)
                speak(P)
            