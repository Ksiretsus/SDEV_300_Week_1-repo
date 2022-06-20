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
population = pd.read_csv('PopChange.csv')

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

    population = pd.read_csv('PopChange.csv')

    print('You selected population data.')
    menu_choice = 0

    while menu_choice != 4:
        population_display()

        menu_choice = int_input('Enter your choice: ')

        if menu_choice == 1:
            col = 'Pop Apr 1'
            uplimit = 250000
        elif menu_choice == 2:
            col = 'Pop Jul 1'
            uplimit = 250000
        elif menu_choice == 3:
            pass

def get_stats(dfin, col, uplimit, lowlimit=1):
    """Gets column values, validates values based on input limits
    
    Four arguments. A dataframe and column to be worked are passed in as dfin and
    col. The dataframe column is iterated row by row and the values in each cell are
    compared to the upper limit and optional lower limit parameters. If a cell is
    found with a value outside the limits, correct_cell() is called on the cell"""
    
    for index, row in dfin.iterrows():
        if row[col] > uplimit or row[col]< lowlimit:
            #print(index, row[col])
            correct_cell(dfin[col], row[col], uplimit, lowlimit)
            #print(index, row[col])
    
    display_stats(dfin, col)

def correct_cell(df, cell, uplimit, lowlimit):
    print(str(cell) + ' is outside range of '+str(lowlimit)+' to '+str(uplimit))
    new_value = cell_value(uplimit, lowlimit)
    df.replace(cell, new_value, inplace=True)

def cell_value(uplimit, lowlimit):
    """Function verifies input is an integer between an upper and lower limit.

    function asks user to input a number. If the input is not an integer and/or
    the value is outside of "lowlimit < value < uplimit" , an error message is
    displayed with the entry parameters and prompting the user to enter again."""

    length = None
    while length is None:
        length = input('enter a number between '+str(lowlimit)+' and '+str(uplimit)+': ')
        try:
            length = int(length)
            if length > uplimit or length < lowlimit:
                length = None
                print('Error: please enter a numnber in the suggested range.')
        except ValueError:
            length = None
            print('Error: please enter integers only.')
    print('You entered: ' + str(length))
    return length

def display_stats(df, col):
    print('The column count is: '+str(len(df[col])))
    print('The column mean is: '+str(df[col].mean()))
    print('The standard deviation is: '+str(df[col].std()))
    print('The column min is: '+str(df[col].min()))
    print('The column max is: '+str(df[col].max()))

def housing_menu():

    housing = pd.read_csv('Housing.csv')

    print('You selected housing data.')
    menu_choice = 0

    while menu_choice != 5:
        housing_display()

        menu_choice = int_input('Enter your choice: ')

        if menu_choice == 1:
            pass
        elif menu_choice == 2:
            pass
        elif menu_choice == 3:
            pass
        elif menu_choice == 4:
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
    print('\nSelect the column to analyze:')
    print('1) Population April 1st')
    print('2) Population July 1st')
    print('3) Change population')
    print('4) Go back')

def housing_display():
    print('\nSelect the column to analyze:')
    print('1) House age')
    print('2) Number of bedrooms')
    print('3) Year built')
    print('4) Total number of rooms')
    print('5) Go back')


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

#main()
