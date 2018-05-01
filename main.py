
import sys
import yaml
import speech_recognition as sr
import os

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
proxy_username = profile_data['proxy_username']
proxy_password = profile_data['proxy_password']

# welcome message
tts('Welcome ' + name + ' systems are now ready to run. How can I help you?')

"""
voice_file = os.getcwd() + '/uploads/' + sys.argv[1]
"""

def main():
    # record waht been said in audio
    r = sr.Recognizer()
   
    """
    with sr.WavFile(voice_file) as source:
        audio = r.record(source)
   """
    
 
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    
    # recognize the message (STT)
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Darong thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Darong cound not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    # call brain and pass the speech recognized to brain for processing
    brain(name, speech_text,city_name, city_code, proxy_username, proxy_password)

main()
      