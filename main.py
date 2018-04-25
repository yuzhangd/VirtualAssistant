
import sys
import yaml
import speech_recognition as sr
from GreyMatter.SenseCells.tts import tts

profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

# functioning variablea
name = profile_data['name']
city_name = profile_data['city_name']

tts('Welcome ' + name + 'from ' + city_name + ', systems are now ready to run. How can I help you?')

def main():
    # record waht been said in audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    
    # print audio
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        print("Melissa thinks you said '" + speech_text + "'")
    except sr.UnknownValueError:
        print("Melissa cound not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    # speak out audio    
    tts(speech_text)

main()
      