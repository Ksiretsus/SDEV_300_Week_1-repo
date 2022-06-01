"""Author: Ryan Miskovic
   Date: 5/30/22
   Program purpose: This program is a demonstration of a menu based program which
   can be executed from the command line. It contains operations for generating
   passwords, calculating percentages, calculating the number of days until
   July 4th 2025, calculating the leg c of a triangle, and calculating the volume
   of a right cylinder. """

import math
import string
import secrets
from datetime import date

# Constants for menu choices
PASSWORD_GENERATOR = 1
CALCULATE_PERCENTAGE = 2
DAYS_UNTIL = 3
CALCULATE_LEG_C = 4
RIGHT_CYLINDER_VOLUME = 5
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
        elif choice == DAYS_UNTIL:
            days_until()
        elif choice == CALCULATE_LEG_C:
            calculate_side_c()
        elif choice == RIGHT_CYLINDER_VOLUME:
            right_cylinder_vol()
        elif choice == QUIT_CHOICE:
            print('Thank you for using the program.')
            print('Goodbye.')



def display_menu():
    """Program main menu.

    displays the menu options to the user each time the
    main loop is repeated."""

    print('\nPlease make a selection below:\n')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~ MENU ~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('1) Password Generator')
    print('2) Calculate a percentage')
    print('3) Days until July 4th, 2025')
    print('4) Calculate side c of a triangle.')
    print('5) Calulate the volume of a cylinder')
    print('9) Quit')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')


def welcome_message():
    """Displays opening message to user."""

    print('Hello! Welcome to the program!')
    print('Below you will find several useful options!')


def make_password():
    """Function displays a randomly created password.

    password is generated according to parameters set by the user
    to include upper and lower case characters, numbers, special characters
    and password length. This function gathers the user parameters then passes
    that data to alpha_gen(), password_length(), and password_gen(), then
    it displays the return result to the user."""

    print("Please choose y or no for the following options: ")
    upper = yes_no_input('Include uppercase? ')
    numbers = yes_no_input('Include numbers? ')
    special_chars = yes_no_input('Include special characters? ')
    alphabet = alpha_gen(upper, numbers, special_chars)
    pw_length = password_length()
    new_password = password_gen(pw_length, alphabet)

    print('///////////////////////////////////')
    print('Your password is: ' + new_password)
    print('///////////////////////////////////')

def percent_gen():
    """This function generates a percent from user input.

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

def days_until():
    """Function to display days remaining until July 4th, 2025.

    it takes no arguments."""

    today = date.today()
    countdown_date = date(2025, 7, 4)
    time_left = abs(countdown_date - today)
    days_left = str(time_left.days)

    print('\n///////////////////////////////////////////////')
    print('There are ' + days_left + ' days to go until July 4th, 2025!')
    print('///////////////////////////////////////////////')

def calculate_side_c():
    """Function calculates and displays side c length of a triangle.

    function takes no arguments. User is prompted to input sides a and b
    and also angle C of a triangle. The input is verifed to be in integer format
    then the calculation is performed. The result is then displayed to the user."""

    print('Please input the following data to calculate side c length:')
    side_a = int_input('Enter side a length: ')
    side_b = int_input('Enter side b length: ')
    angle_c = int_input('Enter angle c in degrees: ')
    angle_c_rad = math.radians(angle_c)

    side_c_squared = (math.pow(side_a, 2) + math.pow(side_b, 2) -
    (2 * side_a * side_b * math.cos(angle_c_rad)))

    side_c = math.sqrt(side_c_squared)
    side_c = round(side_c, 2)

    print('\n/////////////////////////////////////')
    print('Side c length is equal to ' +  str(side_c) + ' units.')
    print('/////////////////////////////////////')

def right_cylinder_vol():
    """Function calculates the volume of a right circular cylinder.

    funtion takes no arguments. User is prompted to input the cylinders
    base radius and height, and the input is validated to be integer format.
    The volume calculation is performed and the result is displayed to the user."""

    print('Please input the following information to calculate volume of a cylinder')
    radius = int_input('Enter the radius of the cylinders base: ')
    height = int_input('Enter the height of the cylinder: ')

    volume = math.pi * math.pow(radius, 2) * height
    volume = round(volume,2)

    print('\n///////////////////////////////////////////////')
    print('The volume of the cylinder is ' + str(volume) + ' units cubed')
    print('///////////////////////////////////////////////')

def yes_no_input(text):
    """Function verifies user input is either 'y' or 'n'.

    this function is utilized in the same manner as input(), it accepts one argument
    which is diplayed as a message to the user who responds and the input
    is saved as a variable. However this function will only accept 'y' or 'n'
    as input from the user and it validates that input."""

    yes_no = None
    while yes_no is None:
        yes_no = input(text)
        print('You entered: ' + yes_no)
        if yes_no == 'y' or yes_no == 'n':
            break

        yes_no = None
        print('Error: please enter only "y" or "n".')

    return yes_no

def int_input(text):
    """Function verifies user input is an integer.

    function is utilized in the same manner as input(). it accepts one argument
    which is diplayed as a message to the user who responds and the input
    is saved as a variable. However this function will only accept an integer as
    an input and will validate input and display an error if it recieves anything else."""

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
    """Function verifies password length input is an integer of at least 8.

    function asks user to input a number for password length. If the input is not
    an integer and/or the length is less than 8, an error message is displayed
    with the entry parameters and prompting the user to enter again."""

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
    """Function creates the string which determines the alphabet used in password_gen().

    function takes three 'y/n' arguments which are passed in from password_maker().
    a 'y' input for an argument indicates that the character set corresponding to
    the arg's name should be included in the string. The string is then returned
    back to the calling function."""

    alphabet = string.ascii_lowercase

    if upper == 'y':
        alphabet += string.ascii_uppercase
    if numbers == 'y':
        alphabet += string.digits
    if special_chars == 'y':
        alphabet += string.punctuation

    return alphabet

def password_gen(length, alphabet):
    """Function generates random password.

    function takes two arguments, length and alphabet, passed in from password_maker.
    returns a randomly generated password of 'length' using the characters available
    in the string 'alphabet'."""

    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

def percent_maker(num, denom, precision):
    """Function calculates and formats a percentage of value a to value b.

    function takes three arguments, num, denom, and precision. num is divided
    by denom to obtain a ratio. Ratio is multiplied by 100 to obtain a percent,
    then percent is rounded to the number of digits in 'precision'. The output
    is returned to the calling function."""

    ratio = num/denom
    percent = ratio*100
    rounded_percent = round(percent, precision)
    return rounded_percent

main()
