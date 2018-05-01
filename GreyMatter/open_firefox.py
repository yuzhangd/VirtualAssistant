
from selenium import webdriver

from GreyMatter.SenseCells.tts import tts

def open_firefox():
    tts("Openning Firefox")
    webdriver.Firefox()
    
    
    
