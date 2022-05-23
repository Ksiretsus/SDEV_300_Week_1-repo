"""
Author: Ryan Miskovic
Date: 5/20/22
Program purpose: This program is a voter registration application"""


import sys

def main():

    """Mainline program logic."""

    full_name = ''
    age = 0
    citizenship = ''
    state_res = ''
    zip_code = 0

    welcome_message()
    full_name = get_name()
    continue_reg()
    age = get_age()
    continue_reg()
    citizenship = citizen()
    validate_eligibility(age, citizenship)
    continue_reg()
    state_res = state_of_residence()
    continue_reg()
    zip_code = get_zip()
    reg_complete(full_name, age, citizenship, state_res, zip_code)

def get_name():
    """This function asks for users first and last name, outputs to single string."""
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    full_name = first_name + ' ' + last_name
    print('You entered: ' + full_name)
    return full_name

def get_age():
    """This function asks for age and validates user input."""
    age = None
    while age is None:
        age = input('Enter your age: ')
        try:
            age = int(age)
            if age > 120:
                age = None
                print('Error: please enter a reasonable age')
        except ValueError:
            age = None
            print('Error: input must be a number.')

    print('You entered: ' + str(age))
    return age

def citizen():
    """Function asks user for citizenship status."""
    citizenship = input('Are you a U.S. citizen? y/n: ')
    print('You entered: ' + citizenship)
    return citizenship

def validate_eligibility(age, citizenship):
    """Function checks that user meets minimum age and citizenship."""
    if age < 18 or citizenship != 'y':
        print("I'm sorry, it looks like you aren't eligible to vote.")
        print("Thank you for using the voter registration application.")
        sys.exit()

    else:
        print('\nLooks like you are eligible!')

def state_of_residence():
    """Function asks for state of residence, then checks input against a list of valid states"""
    state = input('\nEnter the two letter abbreviation for your state (e.g. "MD, VA"): ')
    state = state.upper()
    while state not in state_list:
        print('\nError: I\'m sorry, '+state+' is not a valid state.')
        state = input('Enter the two letter abbreviation for your state (e.g. "MD, VA"): ')
        state = state.upper()
    print('You entered: ' + state)
    return state

def get_zip():
    """This function asks user for a 5 digit zip code. It first checks that the entry is
    exactly 5 digits long, then attempts to cast the input to int(). If it fails either
    an error message is displayed and user is prompted for another input."""
    zip_code = None
    while zip_code is None:
        zip_code = input('\nPlease enter your 5 digit zip code: ')
        if not len(zip_code) == 5:
            zip_code = None
            print('\nError: Please enter exactly 5 digits.\n')
        else:
            try:
                zip_code = int(zip_code)
            except ValueError:
                zip_code = None
                print('\nError: Please enter numbers only.\n')
    print('You entered: ' + str(zip_code))
    return zip_code

def continue_reg():
    """Function asks user if they wish to continue. If not it exits the program."""
    keep_going = input('\nDo you want to continue the registration? y/n: ')
    if keep_going == "n":
        print('Thank you for using the voter registration app. Goodbye.')
        sys.exit()

def reg_complete(full_name, age, citizenship, state_res, zip_code):
    """Function takes all user input and displays a final message and the input
    data to the user."""
    print("""\n    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Congratulations!
    You\'re all registered to vote!
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    You input the following information: """
    '\nName: ' + full_name +
    '\nAge: ' + str(age) +
    '\nU.S. Citizen: ' + citizenship +
    '\nState: ' + state_res +
    '\nZip code: ' + str(zip_code))

def welcome_message():
    """Message dispplayed to user on program start. It describes the program
    purpose."""
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
