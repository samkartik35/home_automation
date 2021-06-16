import speech_recognition as sr
import pyttsx3
#import pywhatkit
import datetime
import wikipedia
import pyjokes
import telnetlib

HOST = "192.168.43.11"

tn = telnetlib.Telnet(HOST,8888,10)

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    command =' '
    keyword =' '
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                keyword='alexa'
                print(command,keyword)
    except:
        pass
    return command,keyword


def run_alexa():
    command , keyword = take_command()
    print(command)
    if 'alexa' in keyword:

        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            #pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'who the heck is' in command:
            person = command.replace('who the heck is', '')
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except: 
                talk('Unable to find on internet')

        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())

        elif 'Arvind' in command:
            talk('Arvind Kumar, director program management Ambient Scientific India. Born in Azamgarh Uttar Pradesh and broughtup in Karnal City. He is B.Tech in Computer Science from NIT Kurukshetra. He has worked with Intel, Ciena, Bharat Electronics, Fujutsu and Ambient Scientific.') #He holds 2 patents in photonics and published 2 papers')
        elif 'my name' in command:
            talk('Arvind Kumar, director program management Ambient Scientific India. Born in Azamgarh, Uttar Pradesh, and broughtup in Karnal City. He is B.Tech in Computer Science from NIT Kurukshetra. He has worked with Intel, Ciena, Bharat Electronics, Fujutsu and Ambient Scientific.') #He holds 2 patents in photonics and published 2 papers')
        elif 'my hobbies' in command:
            talk("you are a runner, practice yoga, you are a black belt in martial arts and amatuer boxer")

        elif 'Madan' in command:
            talk('Madanjit is Managing Director Ambient Scientific and hails from Varanasi Uttar Pradesh')
        elif 'exit' in command:
            talk('exiting')
            exit(0)
        elif 'repeat' in command:
            talk(command)
        
        elif 'light on' in command:
            
            talk( command)
            message = ("N").encode('ascii')
            tn.write(message)
        elif 'light off' in command:
            talk(command)
            #message = ("OFF"+HOST+"\n\n").encode('ascii')
            message = ("F").encode('ascii')
            tn.write(message)
        

        else:
            talk('Please say the command again.')


while True:
    run_alexa()
