"""Program author: Ryan Miskovic
Date: 6/18/2022
Program purpose: This program demonstrates the use of Python libraries to
read .csv and .xlsx files, and then access the data within the colums, rows,
and cells to generate analysis and graphs."""

from datetime import date
import pandas as pd
import matplotlib.pyplot as plt

#Constants for menu
QUIT_CHOICE = 9
POPULATION = 1
HOUSING = 2


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
    """Contains logic for population_display() choices.

    Zero arguments. Variable created for PopChange.csv and data read in.
    a while loop begins and user is prompted to input a choice 1-4. The
    fuction will call get_stats() and pass in the column name based on
    user choice."""

    population = pd.read_csv('PopChange.csv')

    print('You selected population data.')
    menu_choice = 0

    while menu_choice != 4:
        population_display()

        menu_choice = int_input('Enter your choice: ')

        if menu_choice == 1:
            col = 'Pop Apr 1'
            uplimit = 250000
            get_stats(population, col, uplimit)
        elif menu_choice == 2:
            col = 'Pop Jul 1'
            uplimit = 250000
            get_stats(population, col, uplimit)
        elif menu_choice == 3:
            col = 'Change Pop'
            uplimit = 20000
            lowlimit = -20000
            get_stats(population, col, uplimit, lowlimit)

def get_stats(dfin, col, uplimit, lowlimit=1):
    """Gets column values, validates values based on input limits

    Four arguments. A dataframe and column to be worked are passed in as dfin and
    col. The dataframe column is iterated row by row and the values in each cell are
    compared to the upper limit and optional lower limit parameters. If a cell is
    found with a value outside the limits, correct_cell() is called on the cell"""

    for index, row in dfin.iterrows():
        if row[col] > uplimit or row[col]< lowlimit:
            print(col +' has an outlier!')
            correct_cell(dfin, index, col, uplimit, lowlimit)

    display_stats(dfin, col)

def correct_cell(dfin, index, col, uplimit, lowlimit):
    """Function allows user to correct a specific cell in data.

    Four arguments, a dataframe, column name, upper limit, and lower limit. If
    get_stats detects a value outside of range, correct_cell alerts the user
    and displays the value, as well as the limits. it then calls cell_value()
    and passes the upper and lower limits as arguments. When it recieves the
    new value, it uses df.replace() to change the specified value."""

    print(str(dfin.at[index, col])+' is outside range of '+str(lowlimit)+' to '+str(uplimit))
    new_value = cell_value(uplimit, lowlimit)
    dfin.at[index, col] = new_value

def cell_value(uplimit, lowlimit):
    """Function verifies input is an integer between an upper and lower limit.

    function asks user to input a number. If the input is not an integer and/or
    the value is outside of "lowlimit < value < uplimit" , an error message is
    displayed with the entry parameters and prompting the user to enter a replacement."""

    length = None
    while length is None:
        length = input('enter a replacement value between '+str(lowlimit)+' and '+str(uplimit)+': ')
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

def display_stats(dfin, col):
    """Displays statistics of the input dataframe column.

    Two arguments, a dataframe and column name. This function calculates
    and prints to console column count, mean, st deviation, min and max.
    then show_histo() is called to display a histogram."""

    print('\nThe column count is: '+str(len(dfin[col])))
    print('The '+col+' mean is: '+str(dfin[col].mean()))
    print('The standard deviation is: '+str(dfin[col].std()))
    print('The '+col+' min is: '+str(dfin[col].min()))
    print('The '+col+' max is: '+str(dfin[col].max()))
    show_histo(dfin, col)

def show_histo(dfin, col):
    """Displays a histogram of the data passed in."""

    dist = dfin[col]
    n_bins = 20
    plt.hist(dist, n_bins)
    plt.xlabel(col)
    plt.show()

def housing_menu():
    """Contains logic for housing_display() choices.

    Zero arguments. Variable created for Housing.csv and data read in.
    A while loop begins and user is prompted to input a choice 1-5. The
    fuction will call get_stats() and pass in the column name based on
    user choice."""

    housing = pd.read_csv('Housing.csv')


    print('You selected housing data.')
    menu_choice = 0

    while menu_choice != 6:
        housing_display()

        menu_choice = int_input('Enter your choice: ')

        if menu_choice == 1:
            col = 'AGE'
            uplimit = 150
            corrected_age(housing)
            get_stats(housing, col, uplimit)
        elif menu_choice == 2:
            col = 'BEDRMS'
            uplimit = 10
            lowlimit = 0
            get_stats(housing, col, uplimit, lowlimit)
        elif menu_choice == 3:
            col = 'BUILT'
            uplimit = date.today().year
            lowlimit = 1850
            get_stats(housing, col, uplimit, lowlimit)
        elif menu_choice == 4:
            col = 'ROOMS'
            uplimit = 15
            get_stats(housing, col, uplimit)
        elif menu_choice == 5:
            col = 'UTILITY'
            uplimit = 1100
            lowlimit = 0
            get_stats(housing, col, uplimit, lowlimit)

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
    """Displays the options for population.

    displays the menu options to the user each time the
    main loop is repeated."""

    print('\nSelect the column to analyze:')
    print('1) Population April 1st')
    print('2) Population July 1st')
    print('3) Change population')
    print('4) Go back')

def housing_display():
    """Displays housing options.

    displays the menu options to the user each time the
    main loop is repeated."""

    print('\nSelect the column to analyze:')
    print('1) House age')
    print('2) Number of bedrooms')
    print('3) Year built')
    print('4) Total number of rooms')
    print('5) Utility')
    print('6) Go back')

def corrected_age(dfin):
    """Adjusts house age to match year built.

    One argument, dataframe. Variable created to hold current year
    using datetime library. For loop iterates through each row and
    calculates house age by subtracting year built from current year.
    The old age figure in the table is replaced with the new age fig."""

    current_year = (date.today().year)
    for index, row in dfin.iterrows():
        build_year = row['BUILT']
        new_age = current_year - build_year
        dfin.at[index, 'AGE'] = new_age

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

    print('You entered: ' + str(number)+'\n')
    return number

main()
