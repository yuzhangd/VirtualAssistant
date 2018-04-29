import sqlite3
from datetime import datetime

from GreyMatter.SenseCells.tts import tts

def note_something(speech_text):
    conn = sqlite3.connect('memory.db')
    words_of_message = speech_text.split()
    words_of_message.remove('note')
    cleaned_message = ' '.join(words_of_message)
    conn.execute("INSERT INTO notes (notes, notes_date) VALUES (?, ?)", \
                 (cleaned_message, datetime.strftime(datetime.now(), '%d-%m-%Y')))
    conn.commit()
    conn.close()
    
    tts('Your note has been saved')
    
def show_all_notes():
    conn = sqlite3.connect('memory.db')
    tts('Your notes are as follows: ')
    cursor = conn.execute("SELECT notes FROM notes") 
    # the first "note" is one column of the database
    
    for row in cursor:
        print(row[0])
        tts(row[0])
        
    conn.close()
        