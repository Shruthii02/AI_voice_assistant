


import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia


s = sr.Recognizer()

def speak(command):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.say(command)
    engine.runAndWait()

def commands():
    try:
        with sr.Microphone() as source:
            s.adjust_for_ambient_noise(source)
            print('listening....ask now...')
            my_audio = s.listen(source)
            my_text = s.recognize_google(my_audio)
            my_text = my_text.lower()
            print(my_text)

           # to play song
            if 'play' in my_text:
                my_text = my_text.replace('play','')
                speak('playing'+my_text)
                pywhatkit.playonyt(my_text)
            
            # to know the person
            if "who is" in my_text:
                person = my_text.replace('who is','')
                info = wikipedia.summary(person,1)
                speak(info)
  
    except:
        print('error')
        
commands()