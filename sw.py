import speech_recognition as sr
import subprocess
from gtts import gTTS
import cv2
import face_recognition
import numpy as np
import math
import os
import time

def listne():
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                if "bye" in text:
                    break
                elif "time" in text:
                    tm()
                elif "you are a bad" in text:
                    subprocess.call(["afplay","fail.mp3"])
                    
                elif text=="terminate":
                    text2sp("Bye sir have a nice day")
                    quit()
                else:
                    dice(text)
                    
            except:
                print("")
                
def imgreg():
    video=cv2.VideoCapture(0)
    deep_image = face_recognition.load_image_file("deep.jpg")
    deep_face_encoding = face_recognition.face_encodings(deep_image)
    print("System Start working!")

    while True:
        rit,frame=video.read()
        small_frame = cv2.resize(frame, (0, 0), fx=1, fy=1)
        rgb_small_frame=small_frame[:,:,:: -1]
        face_locations=face_recognition.face_locations(rgb_small_frame,)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(deep_face_encoding, face_encoding)
            if True in matches:
                print("Hello sir how can i help you!")
                subprocess.call(["afplay","deep.mp3"])
                listne()
            else:
                print("Waiting for master!")




    video.release()
    cv2.destroyAllWindows()
    
def text2sp(text):
    arr = os.listdir()
    fname=text+".mp3"
    if fname in arr:
        subprocess.call(["afplay",fname])
        #print("found")
    elif "time" in text:
        speach= gTTS(text)
        speach.save(fname)
        subprocess.call(["afplay",fname])
        os.remove(fname)
    else:
        speach= gTTS(text)
        speach.save(fname)
        subprocess.call(["afplay",fname])
        #print("download")
        
def dice(text):
    commands={
        "hello":"hi! how can i help you?",
        "what is your name":"my name is Swadesh",
        "hi":"hello! how can i help you?",
        "what you can do for me":"i can recognise my master, chat with him, and take photos",
        "who is the Prime Minister of India":"Shree Narendra Modi is the prime minister of the India",
        "what is the capital of India":"Delhi is the capital of india",
        "who is Sachin Tendulkar":"Sachin Tendulkar is a cricketer, he is also known as the god of cricket",
        "where is Tajmahal located":"tajmahal located in Agra",
        "who is the CEO of Google":"Sundar Pichai is the ceo of google",
        "I love you":"i love myself only",
        "tell me a joke":"the biggest joke is that you are a joke ha ha ha",
        "ok":"welcome sir!",
        "you are very cute":"awwwwwwwwwww",
    }
    if text in commands:
        print("Responce: ",commands[text])
        text2sp(commands[text])
    else:
        text2sp("Sorry that is not in my program!")
def tm():
    named_tuple = time.localtime() # get struct_time
    time_string = time.strftime("the time is %I %M  %p", named_tuple)
    print(time_string)
    text2sp(time_string)
    

imgreg()
