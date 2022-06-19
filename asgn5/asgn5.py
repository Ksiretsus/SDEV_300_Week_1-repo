"""Program author: Ryan Miskovic
Date: 6/18/2022
Program purpose:"""

import pandas as pd
import numpy as np

#Constants for menu
QUIT_CHOICE = 9
POPULATION = 1
HOUSING = 2

housing = pd.read_csv('Housing.csv')

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
        choice = int_input('Enter your choice: ')

        #Perform users selected action.
        if choice == POPULATION:
            population_menu()
        elif choice == HOUSING:
            housing_menu()
        elif choice == QUIT_CHOICE:
            print('Thank you for using the program.')
            print('Goodbye.')

def population_menu():

    print('You selected population data.')

    menu_choice = 0

    while menu_choice != 4:
        population_display()

        menu_choice = int_input('Enter your choice: ')

        if menu_choice == 1:
            pass
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            pass


def housing_menu():
    pass

def welcome_message():
    """Displays opening message to user."""

    print('\nHello! Welcome to the Python Data Analysis App!\n')

def display_menu():
    """Program main menu.

    displays the menu options to the user each time the
    main loop is repeated."""

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' Select the file you want to analyze ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Enter "1" for population data')
    print('Enter "2" for housing data')
    print('Enter "9" to exit program.')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def population_display():
    print('Select the column to analyze:')
    print('1) Population April 1st')
    print('2) Population July 1st')
    print('3) Change population')
    print('4) Go back')

def housing_display():
    pass

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

main()
