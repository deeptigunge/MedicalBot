from my_module.medical_bot_functions import *

def test_check_yes_no():
    assert callable(check_yes_no)
    user_input = 'no'
    assert print('That is okay, I am always here if you change your mind!')
    user_input = 'yes'
    assert print('Great! Is this medical advice for a child or an adult?')
    
def test_check_child_adult():
    assert callable(check_child_adult)
    user_input = 'child'
    assert print('Pick what specialization the advice is needed for: Neonatology, '\
                  'Cardiology, Oncology, Pulmonology, Psychiatry, Infectious Diseases, or Other')
    user_input = 'adult'
    assert print('Pick what specialization the advice is needed for: Neurology, '\
                'Dermatology, Gynaecology, Psychiatry, Cardiology, or Other') 
    
def test_check_specialization():
    assert callable(check_specialization)
    user_input = 'Neonatology'
    assert print('Call 510-739-4729')
    user_input = 'Cardiology'
    assert print('Call 927-984-1629')
    user_input = 'Oncology'
    assert print('Call 639-274-9584')
    user_input = 'Pulmonology'
    assert print('Call 937-948-5296')
    user_input = 'Psychiatry'
    assert print('Call 827-364-9364')
    user_input = 'Infectious Diseases'
    assert print('Call 394-057-9473')
    user_input = 'Other'
    assert print('Call 387-2847-4829')
    user_input = 'Neurology'
    assert print('Call 394-947-2846')
    user_input = 'Dermatology'
    assert print('Call 397-374-8294')
    user_input = 'Gynaecology'
    assert print('Call 394-508-2848')
