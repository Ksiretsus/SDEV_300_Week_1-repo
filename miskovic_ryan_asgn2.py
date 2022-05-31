import string
import secrets
import time
from datetime import date

# Constants for menu choices
PASSWORD_GENERATOR = 1
CALCULATE_PERCENTAGE = 2
QUIT_CHOICE = 9


def main():
    """This is the mainline program logic."""

    #The choice variable controls the menu loop
    #and holds the users choice
    choice = 0

    welcome_message()

    while choice != QUIT_CHOICE:
        #display the menu
        display_menu()

        #Get the users choice.
        choice = int(input('Enter your choice: '))

        #Perform users selected action.
        if choice == PASSWORD_GENERATOR:
            make_password()
        elif choice == CALCULATE_PERCENTAGE:
            percent_gen()
        elif choice == QUIT_CHOICE:
            print('Thank you for using the program.')
            print('Goodbye.')



def display_menu():
    print('\nPlease make a selection below:\n')
    print('         MENU')
    print('1) Password Generator')
    print('2) Calculate a percentage')
    print('9) Quit')
    print('~~~~~~~~~~~~~~~~~~~~~~\n')


def welcome_message():
    print("Hello! Welcome to the program!")

def make_password():

    print("Please choose y or no for the following options: ")
    upper = yes_no_input('Include uppercase?')
    numbers = yes_no_input('Include numbers?')
    special_chars = yes_no_input('Include special characters?')
    alphabet = alpha_gen(upper, numbers, special_chars)
    pw_length = password_length()
    new_password = password_gen(pw_length, alphabet)
    print('///////////////////////////////////')
    print('Your password is: ' + new_password)
    print('///////////////////////////////////')

def percent_gen():
    """This function generates a percent using user input.
    
    it asks for a numerator, denominator, and number of decimal places, 
    then passes those inputs to percent_maker()."""

    print('To generate a percent, please provide the following:')

    numerator = int_input('Enter a numerator: ')
    denominator = int_input('Enter a denominator: ')
    precision = int_input('Enter the number of decimal places: ')
    percent = percent_maker(numerator, denominator, precision)
    print('/////////////////////////')
    print('The result is:')
    print(str(percent) + '%')
    print('/////////////////////////')


def yes_no_input(text):
    """This function displays the text argument passed in
        and checks that the response is either y or n."""
    yes_no = None
    while yes_no is None:
        yes_no = input(text)
        print('You entered: ' + yes_no)
        if yes_no == 'y' or 'n':
            break
        else:
            yes_no = None
            print('Error: please enter only "y" or "n".')

    return yes_no

def int_input(text):
    """This function displays the text argument passed in
    and checks that the user input is an integer."""
    number = None
    while number is None:
        number = input(text)
        try:
            number = int(number)
        except ValueError:
            number = None
            print('Error: please enter integers only.')
    print('You entered: ' + str(number))
    return number

def password_length():
    length = None
    while length is None:
        length = input('enter a number of 8 or greater for password length: ')
        try:
            length = int(length)
            if length < 8:
                length = None
                print('Error: please enter a password length greater than 8.')
        except ValueError:
            length = None
            print('Error: please enter integers only.')
    print('You entered: ' + str(length))
    return length

def alpha_gen(upper, numbers, special_chars):
    alphabet = string.ascii_lowercase
    
    if upper == 'y':
        alphabet += string.ascii_uppercase
    if numbers == 'y':
        alphabet += string.digits
    if special_chars == 'y':
        alphabet += string.punctuation
    #print(alphabet)
    return alphabet

def password_gen(length, alphabet):
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    #print(password)
    return password

def percent_maker(num, denom, precision):
    ratio = num/denom
    percent = ratio*100
    rounded_percent = round(percent, precision)
    return rounded_percent

main()