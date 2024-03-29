import os
import sys

def tts(message):
    """ this function takes a message as an argument and converts it
    to speech depending on the os
    """
    if   sys.platform == 'darwin':
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        tts_engine = 'espeak'
        return os.system(tts_engine + ' "' + message + '"')
    
