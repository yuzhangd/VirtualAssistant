
import sys
import yaml
import speech_recognition as sr

from brain import brain
from GreyMatter.SenseCells.tts import tts

# fetch data from profile
profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# functioning variablea
name = profile_data['name']
city_name = profile_data['city_name']
city_code = profile_data['city_code']

# welcome message
tts('Welcome ' + name + ' systems are now ready to run. How can I help you?')

def main():
    # record waht been said in audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    # recognize the message (STT) and print
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Darong thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Darong cound not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    # call brain
    brain(name, speech_text, city_name, city_code)

main()
      