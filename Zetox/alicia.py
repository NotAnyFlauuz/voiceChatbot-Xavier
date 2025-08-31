import speech_recognition as sr  
import webbrowser
import pyttsx3 
import pyaudio 
from selenium import webdriver
from random import choice 
from musics import music
 
recognizer = sr.Recognizer() 
engine = pyttsx3.init() 
voices = engine.getProperty('voices')

# Change voice (0 for male, 1 for female, or try other indexes)
engine.setProperty('voice', voices[1].id)  # Change index if needed

# Set speech rate (optional)
engine.setProperty('rate', 150)  # Adjust speed if necessary

def speak(text): 
    engine.say(text) 
    engine.runAndWait()  
def procommand(c): 
    def openWeb(a,b,d): 
      if ('open' in c.lower() and a in c.lower()): 
        speak(f'opening {b}')
        webbrowser.open(f'https://{d}.com') 
    openWeb('google','google','google') 
    openWeb('jio cinema','jiocinema','jiocinema') 
    openWeb('facebook','facebook','facebook') 
    openWeb('hotstar','hotstar','hotstar') 
    openWeb('chat GPT','chat GPT','openai') 
    openWeb('cricbuzz','cricbuzz','cricbuzz') 
    openWeb('youtube','youtube','youtube') 
    if (c.lower().startswith('play')): 
      text = c.lower().strip() 
      words = text.split() 
      song = ''.join(words[1:]) 
      link = music[song] 
      speak(f'Playing {words[1:]}') 
      webbrowser.open(link) 
    if (c.lower().startswith('add')): 
       num = c.lower().strip() 
       nums = num.split() 
       num1 = int(nums[1])
       num2 = int(nums[3]) 
       speak(f'The sum is { num1 + num2}') 
    if ('greet' in c.lower()): 
       speak('greetings I am Alicia,the sister of Xavier,Pleasure to meet you')

    if (c.lower().startswith('multiply')): 
       num = c.lower().strip() 
       nums = num.split() 
       num1 = int(nums[1])
       num2 = int(nums[3])  
       print(f'The product is {num1 * num2}')
       speak(f'The product is {num1 * num2}') 
    if (c.lower().startswith('subtract')): 
       num = c.lower().strip() 
       nums = num.split() 
       num1 = int(nums[1])
       num2 = int(nums[3]) 
       speak(f'The answer is {num1 - num2}')
    if (c.lower().startswith('divide')): 
       num = c.lower().strip() 
       nums = num.split() 
       num1 = int(nums[1])
       num2 = int(nums[3]) 
       speak(f'The answer is {num1 / num2}') 
    

if __name__ == "__main__": 
    speak('Initializing Alicia...') 
    while True: 
        r = sr.Recognizer() 
            # recognize speech using Sphinx
        try:  
            with sr.Microphone() as sorce:
              print("Listening...")
              audio = r.listen(sorce)  
            ch = choice([1,2])
            word = r.recognize_google(audio) 
            if ('alicia' in word.lower()): 
                if ch == 1:   
                    speak('Yea') 
                if ch == 2: 
                    speak('How can I help?')   
                with sr.Microphone() as sorce:
                  print("alicia is active....")
                  audio = r.listen(sorce, timeout = 3, phrase_time_limit=3)  
                command = r.recognize_google(audio) 
                print(command)  
                procommand(command)  
            elif (word.lower() == 'arise'): 
                speak('Give commands') 
                speak('Your Majesty!')
                with sr.Microphone() as sorce:
                  print("Alicia is active....")
                  audio = r.listen(sorce, timeout = 2, phrase_time_limit=2)  
                command2 = r.recognize_google(audio) 
                print(command2)  
                procommand(command2)    

           
        except Exception as e: 
           print("Couldnt recognize; {0}".format(e))

            # recognize speech using Google Speech Recognition  
                

