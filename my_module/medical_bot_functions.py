"""All of the functions used for the Medical Bot, an extension of the Chatbot assignment in A3.
    Some parts are used from the Chatbot assignment, but other than that I wrote the majority of the code."""

# Functions from A3 Chatbot Assignment
import string

global chat

def end_chat(user_input):
    """Exits out of the chat if user says 'no.'
    
    Parameters
    ----------
    user_input : string
        The string that the user inputs
        
    Returns
    ----------
        boolean
    If the input was 'no' or not
    """
    
    global chat
    
    if 'no' in user_input:
        output = True
    else:
        output = False
    return output

# Functions I wrote

def start():
    """This prints the first message the Medical Bot displays"""
    print('Hi! Welcome to the Medical Helpline')
    print('I am here to help you get the right kind of care')
    print('Are you here to receive medical advice? Type yes or no')
    print('At any point if you would like to exit this chat, type no')
    
def check_yes_no(user_input):
    """Checks if user_input was 'yes' or 'no.'
    
    Parameters
    ----------
    user_input : string
        Will be either 'yes' or 'no'
    
    Returns
    ----------
    output : string
        Prints either yes statement or no statement
        After no statement, will exit out
    """
    
    global chat 
    
    if user_input == 'no':
        print('That is okay, I am always here if you change your mind!')
        chat = False
    elif user_input == 'yes':
        print('Great! Is this medical advice for a child or an adult?')
        chat = True
    input_type = 'child_adult'
            
def check_child_adult(user_input):
    """Checks if user_input was 'child' or 'adult.'
    
    Parameters
    ----------
    user_input : string
        Will be either 'child' or 'adult'
    
    Returns
    ----------
    output : string
        Prints either child statement or adult statement
        Then continues with chat
    """
    
    if user_input == 'child':
        print('Pick what specialization the advice is needed for: Neonatology, '\
                  'Cardiology, Oncology, Pulmonology, Psychiatry, Infectious Diseases, or Other')
        chat = True
    elif user_input == 'adult':
        print('Pick what specialization the advice is needed for: Neurology, '\
                'Dermatology, Gynaecology, Psychiatry, Cardiology, or Other')
        chat = True
    input_type = 'specialization'
            
def check_specialization(user_input):
    """Checks what specialization user_input was.'
    
    Parameters
    ----------
    user_input : string
        Will be a type of specialization
    
    Returns
    ----------
    output : string
        Prints specific string for each specialization
    """
    
    global chat
    
    if user_input == 'Neonatology':
        print('Call 510-739-4729')
        chat = False
    if user_input == 'Cardiology':
        print('Call 927-984-1629')
        chat = False
    if user_input == 'Oncology':
        print('Call 639-274-9584')
        chat = False
    if user_input == 'Pulmonology':
        print('Call 937-948-5296')
        chat = False
    if user_input == 'Psychiatry':
        print('Call 827-364-9364')
        chat = False
    if user_input == 'Infectious Diseases':
        print('Call 394-057-9473')
        chat = False
    if user_input == 'Other':
        print('Call 387-2847-4829')
        chat = False
    if user_input == 'Neurology':
        print('Call 394-947-2846')
        chat = False
    if user_input == 'Dermatology':
        print('Call 397-374-8294')
        chat = False
    if user_input == 'Gynaecology':
        print('Call 394-508-2848')
        chat = False

def get_medical_advice():
    
    global chat
    """This is the main function used to run the Medical Bot
    It will use all of the functions that were previously defined
    """
    
    # Prints first message Medical Bot says
    start()
    
    # Begins the Medical Bot
    input_type = 'start'
    
    # Sets chat as True so chat may begin
    chat = True
    
    while chat:
        
        # This gets the message from the user
        # This was taken from the Chatbot assignment
        user_input = input()
        
        # Exits of out of chat if user types 'no'
        if end_chat(user_input):
            out_msg = 'That is okay, I am always here if you change your mind!'
            chat = False
            break
            
        # Checks message after first question
        # Responds according to message from user
        if input_type == 'start':
            yes_no = check_yes_no(user_input)
            input_type = 'child_adult'
            
        # Checks message after second question
        # Responds according to message from user
        elif input_type == 'child_adult':
            child_adult = check_child_adult(user_input)
            input_type = 'specialization'
            
        # Checks message after third question
        # Responds according to message from user
        elif input_type == 'specialization':
            specialization = check_specialization(user_input)