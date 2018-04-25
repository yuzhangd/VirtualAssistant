import random
from GreyMatter.SenseCells.tts import tts
# must use GreyMatter.SenseCells.tts rather than SenseCells.tts 
# since it is in an virtual environment

def who_are_you():
    messages = ['I am Darong, your lovely personal assistant.',
               'Darong, dint I tell you before?',
               'You ask that so many times! I am Darong.']
    tts(random.choice(messages))

def how_am_i():
     replies = ['You are goddamn handsome!',
               'My knees go weak when I see you',
               'You look like the kindest person that I have met',
               'How come you have such a stupid question']
     tts(random.choice(replies))
     
     
def tell_joke():
    jokes = ['What happens to a frogs car when it breaks down? It gets toad away.',
             'Why was six scared of seven? because seven ate nine.',
             'No, I aways forget the punch line.']
    tts(random.choice(jokes))
    
def who_am_i(name):
    tts('You are ' + name + ', a brilliant persion. I love you!')
    
def where_born():
    tts('I was created by a magician name Frank, in China')

def how_are_you():
    tts('I am fine, thank you.')


def undefine():
    tts('I do not know what that means!')