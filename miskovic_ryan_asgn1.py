"""
Author: Ryan Miskovic
Date: 5/20/22
Program purpose: This program is a voter registration application"""



#mainline program logic
def main():

    keep_going = 'y'
    first_name = ''
    last_name = ''
    age = 0
    citizenship = ''
    state_res = ''
    zip_code = 0

    welcome_message()
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    continue_reg()
    age = get_age()
    continue_reg()
    citizenship = citizen()
    validate_eligibility(age, citizenship)
    continue_reg()
    state_res = state_of_residence()
    zip_code = get_zip()
    reg_complete(first_name, last_name, age, citizenship, state_res, zip_code)
    
    



#function to get valid age
def get_age():
    age = int(input('Enter your age: '))
    while age > 120:
        print('Sorry, age must be numerical and less than 120')
        age = int(input('Enter your age: '))
    print('You entered: ' + str(age))
    return age

#function to get citizenship
def citizen():
    citizenship = input('Are you a U.S. citizen? y/n: ')
    print('You entered: ' + citizenship)
    return citizenship

def validate_eligibility(age, citizenship):
    if age < 18 or citizenship != 'y':
        print("I'm sorry, it looks like you aren't eligible to vote.")
        print("Thank you for using the voter registration application.")
        exit()
    
    else:
        print('\nLooks like you are eligible!')

def state_of_residence():
    state = input('\nEnter the two letter abbreviation for your state (e.g. "MD, VA"): ')
    state = state.upper()
    while state not in state_list:
        print('\nError: I\'m sorry, '+state+' is not a valid state.')
        state = input('Enter the two letter abbreviation for your state (e.g. "MD, VA"): ')
        state = state.upper()
    print('You entered: ' + state)
    return state

   
def get_zip():
    zc = None
    while zc is None:
        zc = input('\nPlease enter your 5 digit zip code: ')
        if not len(zc) == 5:
            zc = None
            print('\nError: Please enter exactly 5 digits.\n')
        else:
            try:
                zc = int(zc)
            except ValueError:
                zc = None
                print('\nError: Please enter numbers only.\n')
    print('You entered: ' + str(zc))
    return zc


def continue_reg():
    keep_going = input('\nDo you want to continue the registration? y/n: ')
    if keep_going == "n":
        exit()

def reg_complete(first_name, last_name, age, citizenship, state_res, zip_code):
    print("""\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Congratulations!
    You\'re all registered to vote!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    You input the following information: """
    '\nName: ' + first_name +' '+ last_name +
    '\nAge: ' + str(age) +
    '\nU.S. Citizen: ' + citizenship +
    '\nState: ' + state_res +
    '\nZip code: ' + str(zip_code))


#Welcome message function.
def welcome_message():
    print("""\n\n\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Welcome to the voter registration application!
    This program will ask you a few questions to determine
    your eligibility and get you set to vote...or not.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n""")

state_list = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 
    'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
    'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
    'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']


main()