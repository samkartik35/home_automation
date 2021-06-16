import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

from signal import signal, SIGINT
from sys import exit

from voice_record import *

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    exit(0)


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command =''
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'ambient' in command:
                #command = command.replace('ambient', '')
                print(command)
    except:
        pass
    return command


def run_ambient(steam,p):
   
    command = take_command()
    
    print(command)
    if 'cord' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'cord' in command:
        talk('Recording wave file. Please wait...')
        file = record_samples(stream,p)
        talk('Recording completed')
        talk(file)

        
    elif 'Arvind' in command:
        talk('Arvind Kumar, director program management Ambient Scientific India. Born in Azamgarh Uttar Pradesh and broughtup in Karnal City. He is B.Tech in Computer Science from NIT Kurukshetra. He has worked with Intel, Ciena, Bharat Electronics, Fujutsu and Ambient Scientific.') #He holds 2 patents in photonics and published 2 papers')
    elif 'my name' in command:
        talk('Arvind Kumar, director program management Ambient Scientific India. Born in Azamgarh Uttar Pradesh and broughtup in Karnal City. He is B.Tech in Computer Science from NIT Kurukshetra. He has worked with Intel, Ciena, Bharat Electronics, Fujutsu and Ambient Scientific.') #He holds 2 patents in photonics and published 2 papers')
    elif 'my hobbies' in command:
        talk("you are a runner, practice yoga, you are a black belt in martial arts and amatuer boxer")

    elif 'Madan' in command:
        talk('Madanjit is Managing Director Ambient Scientific and hails from Varanasi Uttar Pradesh')
    elif 'exit' in command:
        talk('exiting')
        exit(0)
    elif 'repeat' in command:
        talk(command)
    else:
        talk('Please say the command again.')

# Tell Python to run the handler() function when SIGINT is recieved
signal(SIGINT, handler)

print('Running. Press CTRL-C to exit.')
# init recording
stream,p = init_recording()
while True:
    run_ambient(stream,p)
