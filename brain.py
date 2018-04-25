
from GreyMatter import general_conversations, tell_time

def brain(name, speech_text):
    
    def check_message(check):
        """
        this function checks if the items in the list (specified in argument)
        are present in the user's input speech
        """
        words_of_message = speech_text.split()
        
        if set(check).issubset(set(words_of_message)):
            return True
        else:
            return False
    
    # general conversation 
    if check_message(['who', 'are', 'you']):
        general_conversations.who_are_you()
        
    elif check_message(['how', 'i', 'look']) or check_message(['how', 'am', 'i']):
        general_conversations.how_am_i()
    
    elif check_message(['tell', 'joke']):
        general_conversations.tell_joke()
        
    elif check_message(['who', 'am', 'i']):
        general_conversations.who_am_i(name)
    
    elif check_message(['where', 'born']):
        general_conversations.where_born()
        
    elif check_message(['how', 'are','you']):
        general_conversations.how_are_you()
    
    # check time
    elif check_message(['time']):
        tell_time.what_is_time()


    else:
        general_conversations.undefine()
        