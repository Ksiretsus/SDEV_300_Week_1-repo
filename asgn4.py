"""Program Author: Ryan Miskovic
Date 6/12/2022
Program purpose: This program is to demonstrate the use of the numpy
and regular expressions modules. It shows regular expressions by
verifying user input phone numbers, zip codes, and numbers for a matrix.
Then it shows uses for numpy by manipulating the user matrixes using
various operations.  """

import re
import numpy as np

#Constants for menu
QUIT_CHOICE = 9
PLAY_MATRIX = 1

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
        if choice == PLAY_MATRIX:
            play_matrix()
        elif choice == QUIT_CHOICE:
            print('Thank you for using the program.')
            print('Goodbye.')

def display_menu():
    """Program main menu.

    displays the menu options to the user each time the
    main loop is repeated."""

    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' Do you want to play the Matrix Game? ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('Enter "1" for yes')
    print('Enter "9" for no')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def welcome_message():
    """Displays opening message to user."""

    print('\nHello! Welcome to the Python Matrix application!\n')

def play_matrix():
    """Runs the matrix game sequence."""

    input_phonenum()
    input_zipcode()
    print('Now input matrix #1:')
    matrix_1 = get_user_matrix()
    print('\nYour first 3x3 matrix is:')
    print(matrix_1)
    print('And now input matrix #2: ')
    matrix_2 = get_user_matrix()
    print('\nYour second 3x3 matrix is:')
    print(matrix_2)
    matrix_menu()
    matrix_operations(matrix_1, matrix_2)

def input_phonenum():
    """Gathers a valid phone number from user.

    Function takes no arguments. Both a test pattern for phone number format
    and a message requesting user input are declared as variables. This information
    is passed to the validate_input() function which returns only a valid user entry
    which matches the pattern."""

    test_pattern = r'\d\d\d[-. ]\d\d\d[-. ]\d\d\d\d'
    ask_for_num = 'Please enter a phone number, format: XXX-XXX-XXXX\n'
    phonenum = validate_input(ask_for_num, test_pattern)
    print(phonenum + ' Got it!\n')

def input_zipcode():
    """Gathers a valid zip code from user.

    Function takes no arguments. Both a test pattern for zip code format
    and a message requesting user input are declared as variables. This information
    is passed to the validate_input() function which returns only a valid user entry
    which matches the pattern."""

    test_pattern = r'\d\d\d\d\d[- ]\d\d\d\d'
    ask_for_num = 'Please enter a zip code, format: XXXXX-XXXX\n'
    zipcode = validate_input(ask_for_num, test_pattern)
    print(zipcode + ' Got it!\n')

def validate_input(message, test_pattern):
    """Funtion checks that input matches a pattern passed in.

    Function takes 2 arguments; a message and test pattern. The pattern is compiled
    as a regular expression and then compared to input from the user. The comparison
    result is stored as a variable which represents either a pattern match or None. If
    a pattern match exists, the result is returned to the calling funciton. If the pattern
    is None, the user is notified of the error and asked to input again."""

    pattern = re.compile(test_pattern)
    users_number = None

    while users_number is None:
        users_number = input(message)
        print('You entered: ' + users_number)
        input_match = pattern.match(users_number)
        #print(input_match)
        if input_match is not None:
            return users_number

        users_number = None
        print("Sorry, that format won't work.")

def get_user_matrix():
    """Starts the matrix creation sequence.

    Function takes no arguments. This function is the last stage of input validation
    and it serves to validate input length. create_matrix() throws a ValueError if the
    user does not enter exactly 9 numbers. This function catches the error and runs
    create matrix until the proper number of inputs is recieved before returning."""

    user_matrix = None
    while user_matrix is None:
        try:
            user_matrix = create_matrix()
        except ValueError:
            print('You must enter exactly 9 numbers.')
    return user_matrix

def create_matrix():
    """Gathers input from user to create at 3x3 number matrix.

    Function takes no arguments. User input of 9 numbers is requested and then
    split into list items using a space as the deliniator. The list of numbers
    is passed to test_format() and recieves back either a validated list or None.
    if a list is recieved it is converted into a 3x3 numpy array, and returned to
    the calling function. If None is recieved the user is notified of a format
    error and asked to try again."""

    user_nums = input('enter 9 integers or decimal numbers separated by a single space'+
        '\ni.e. "XX XX" or "XX.XX XX.XX"\n')
    split_nums = re.split(r' ', user_nums)
    checked_nums = test_format(split_nums)

    if checked_nums is not None:
        checked_nums = np.array(checked_nums)
        user_matrix = checked_nums.reshape(3,3)
        return np.array(user_matrix)

    print('You entered: ' + user_nums)
    print('Your input does not follow the format requested.')
    return None

def test_format(number_list):
    """Checks that passed in list is either all integers or all floats.

    Funtion takes 1 argument, a list of numbers in string format. A test pattern
    is declared for integers and for floats. The function calls test_input() for
    both and if it recieves back a list, the list is returned to the calling
    function. If None is recieved from test_input() then None is returned to
    the calling function."""

    int_pattern = re.compile(r'\d+')
    float_pattern = re.compile(r'\d*\.\d+')

    if test_input(number_list, int_pattern) is not None:
        new_list = [int(i) for i in number_list]
        return new_list

    if test_input(number_list, float_pattern) is not None:
        new_list = [float(i) for i in number_list]
        return new_list

    return None

def test_input(number_list, test_pattern):
    """Verifies that all items in a list match the passed in pattern.

    Function takes 2 arguments, a list and test pattern. The list is
    iterated in a for loop which tests each item against a pattern.
    If every item matches, then the list is returned. If any item
    doesn't match, the loop ends and None is returned."""

    pattern = re.compile(test_pattern)

    for number in number_list:
        test_num = pattern.fullmatch(number)
        if test_num is None:
            return None

    return number_list



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

def matrix_menu():
    """A sub-menu displying various matrix operations."""

    print('\nSelect an operation to perform: ')
    print('a) Addition')
    print('b) Subtraction')
    print('c) Matrix Multiplication')
    print('d) Element by Element Multiplication')

def matrix_operations(matrix_1, matrix_2):
    """Gathers and executes a matrix operation selection.

    Function takes 2 arguments, two matrixes as inputs. Menu constants are declared
    and user input is gathered by a call to matrix_selection(). An if/elif/else
    block checks which option the user selected and performs the operation. The result
    is passed to result_print() for display to the user."""

    addition = 'a'
    subtraction = 'b'
    matrix_multiply = 'c'

    mat_input = matrix_selection()

    if mat_input == addition:
        added_matrix = matrix_1 + matrix_2
        result_print(added_matrix, 'addition')
    elif mat_input == subtraction:
        sub_matrix = matrix_1 - matrix_2
        result_print(sub_matrix, 'subtraction')
    elif mat_input == matrix_multiply:
        mat_mul = matrix_1 @ matrix_2
        result_print(mat_mul, 'matrix multiplication')
    else:
        ele_mul = matrix_1 * matrix_2
        result_print(ele_mul, 'element multiplication')


def matrix_selection():
    """Validates user input for the matrix sub-menu options.

    User input is verified to be between 'a' and 'e by a regular expression.
    If anything other than a through e is recieved the user is notifed of
    the error and prompted for input.'"""

    pattern = re.compile(r'[a-d]')
    selection = None
    while selection is None:
        selection = input('\nChoose a, b, c, or d: ')
        test_selection = pattern.fullmatch(selection)
        if test_selection is not None:
            return selection
        print('You chose ' +selection+ ', which is not an option.')
        selection = None

def result_print(in_matrix, op_select):
    """Displays the matrix operation result to the user.

    User is shown what option they chose from the matrix menu, then the
    result of the operation is shown along with the transverse of the result
    and the means of the columns and rows."""

    print('\nYou selected '+ op_select +' , the results are:')
    print(in_matrix)
    print('\nThe transpose is:')
    print(in_matrix.T)
    print('\nThe row and column mean values of the results are:')
    print('\nRow mean values:')
    print(np.mean(in_matrix, axis=0))
    print('\nColumn mean values:')
    print(np.mean(in_matrix, axis=1))

main()
