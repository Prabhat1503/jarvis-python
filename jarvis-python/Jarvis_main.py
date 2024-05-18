import os
import pyttsx3
import pyaudio
import requests
import datetime
import keyboard
import pyautogui
import random
import speedtest
import webbrowser
import speech_recognition 
from pygame import mixer
from plyer import notification
from bs4  import BeautifulSoup

 
for i in range(3):
    a = input("Enter password to open JARVIS: ")
    pw_file = open(r"D:\VS code - F-end\1_Projects\jarvis-python\jarvis-python\important.txt", "r")

    pw = pw_file.read()
    pw_file.close()
    if(a==pw):
        print("welcome sir! please speak wake up to start.")
        break
    elif (i == 2 and a != pw): 
        exit()
    elif (a!=pw):
        print("Try Again")

from INTRO import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("Understanding....")
        query = r.recognize_google(audio, language = "en-in")
        print(f"You said: {query} \n")
    except Exception as e:
        print("Could you please repeat.")
        return "None" 
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break 

#  Jarvis  password change
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

#  scheduling day with jarvis
                elif "schedule my day" in query:
                    tasks = []  #empty list 
                    speak("Do you want to clear old tasks (please speak yes or no)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()

#  show  schedule on notepad
                elif "show my schedule" in query:
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                    
#   foucs mode using jarvis 
                elif "focus mode" in query:
                    a = input("Are you sure you want to enter focus mode: [1 for yes, 2 for no]")
                    if (a == 10):
                        speak("Entering focus mode...")
                        os.startfile(r"D:\VS code - F-end\1_Projects\jarvis-python\jarvis-python\FocusMode.py")
                        exit
                    else: 
                        pass
#  opening apps using jarvis  
                elif "open" in query: 
                    query = query.replace("open","")
                    query = query.replace("jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")    

# check speed of internet
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is {download_net}")
                    speak(f"Wifi Upload speed is {upload_net}")

# IPL score
                elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )

# rock paper scissors using jarvis
                elif "play a game" in query:
                    from game import game_play
                    game_play()

# taking screenshots using python
                elif "screenshot" in query:
                    import pyautogui
                    im = pyautogui.screenshot()
                    im.save("ss.jpg")
                
                elif "click my photo" in query:
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")  
                    pyautogui.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                                            

# greetings from jarvis
                elif "hello" in query:
                    speak("hello sir, how are you?")
                elif "i am fine" in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")
                elif "thank you" in query:
                    speak("you are welcome sir")

#  creating a playlist of your favourite song using jarvis
                elif "tired" in query:
                    speak("playing your favourite songs, sir")
                    a = (1, 2, 3)
                    b = random .choice(a)
                    if b == 1:
                        webbrowser.open("https://www.youtube.com/watch?v=au5uNkCKzaY&ab_channel=Badshah")
                    elif b == 2:
                        webbrowser.open("https://youtube.com/watch?v=6AKkh-Rj-nE&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&start_radio=1&rv=au5uNkCKzaY&ab_channel=K%C3%A9oT%C3%A0iX%E1%BB%89u")                
                    elif b == 3:
                        webbrowser.open("https://www.youtube.com/watch?v=yOUbcqO8awA&list=RDGMEMCMFH2exzjBeE_zAHHJOdxg&index=20&ab_channel=GoyalMusicOfficial")

# Fully automated youtube controls  
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")             
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()

#  to open apps and websites
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

# searches everything from google youtube wikipedia
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

# news reader Jarvis
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()

#  calculation using jarvis
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

# sending whatapp messages
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()


# checks temperature 
                elif "temperature" in query:
                    search = "temperature In Una"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text 
                    speak(f"current {search} is {temp}.")

# Works same as temperature
                elif "weather" in query:
                    search = "weather In Una"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_ = "BNeawe").text 
                    speak(f"current {search} is {temp}.")

# set an alarm
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("set the time")
                    a = input("Please tell the time: ")
                    alarm(a)
                    speak("Done, sir")

#  returns the current time
                elif "the time" in query:
                    strTime  = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"mam, the time is {strTime}")   

#  to put jarvis to sleep            
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()

#  set reminders using jarvis
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me"+ rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me " + remember.read())
                
#  shutting device using JARVIS
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                

                


                    
