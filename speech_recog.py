import time
from logging import exception

import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import pyjokes
import os
import pathlib
from PIL import Image


r = sr.Recognizer()
# def Speak_To_Text(command):
#     engine=pyttsx3.init()
#     voices=engine.getProperty('voices')
#     engine.setProperty('voice',voices[1].id)
#     rate=engine.getProperty('rate')
#     engine.setProperty('rate',175)
#     engine.say(command)
#     engine.runAndWait()
# with sr.Microphone() as source2:
#     print("Silence please , calibrating background noise")
#     r.adjust_for_ambient_noise(source2,duration=2)
#     print("calibrated, Now speak---")
#
#     audio2=r.listen(source2)
#     MyText=r.recognize_google(audio2)
#     MyText=MyText.lower()
#     print(MyText)
def Speak_To_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source2:
        print("Silence please , calibrating background noise")
        r.adjust_for_ambient_noise(source2,2)
        print("calibrated, Now speak---")
        audio2 = r.listen(source2)
        try:
            print("recognizing---")
            MyText = r.recognize_google(audio2)
            return MyText
        except sr.UnknownValueError:
            return "Not Understand Please speak again."

def Text_to_speech(command):
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate=engine.getProperty('rate')
    engine.setProperty('rate',175)
    engine.say(command)
    engine.runAndWait()
def Text_to_Handwritting():
   # txt="""Python is a oject orianted programming language So, to perform operations and prevent
   #        your program from crashing, it is a helpful first step to check if a file exists on a given path.
   #        Thankfully, Python has multiple built-in ways of checking whether a file exists, like the built-in os.path and pathlib modules.
   #        Specifically, when using the os.path module, you have access to:"""
   # if pathlib.Path("C:/Users/mohda/OneDrive/Desktop/project/txt_to_hdw.png").is_file() :
   #   os.remove("txt_to_hdw.png")
   # pw.text_to_handwriting(txt,"txt_to_hdw.PNG",[0,0,138])
   # Open the text file which you have to convert into handwriting
   txt = open("D:/Dummy.txt")  # path of your text file
   # path of page(background)photo (I have used blank page)
   bgg_color = (1, 1, 1, 1)
   BG = Image.open("D:/bg.png", )
   sheet_width = BG.width
   gap, ht = 0, 0

   for i in txt.read().replace("\n", ""):
       cases = Image.open("D:/bg.png".format(str(ord(i))),"w")
       BG.paste(cases, (gap, ht))
       size = cases.width
       height = cases.height
       # print(size)
       gap += size
       if sheet_width < gap or len(i) * 115 > (sheet_width - gap):
           gap, ht = 0, ht + 140
   txt.close()

# data2 = Speak_To_Text()
# Text_to_speech(data2)
if __name__ =='__main__':
    while True:
        data1 = Speak_To_Text().lower()
        if "your name" in data1:
            name="my name is Abuzar"
            Text_to_speech(name)
        elif "old are you" in data1:
            age = "i am 20 year old"
            Text_to_speech(age)
        elif "time" in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            Text_to_speech(time)
        elif "youtube" in data1:
            webbrowser.open("https://www.youtube.com/watch?v=Y6WV7v4zuNM")
        elif "web" in data1:
            webbrowser.open("https://thecodingtracker.com/")
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language="en",category="neutral")
            print(joke_1)
            Text_to_speech(joke_1)
        elif 'play song' in data1:
            add="D:\song"
            listsong = os.listdir(add)
            os.startfile(os.path.join( add,listsong[0]))
        elif "convert" in data1:
            Text_to_Handwritting()
        elif "exit" in data1:
            print("Thanks for visit")
            break
        time.sleep(5)





