import string
import secrets

# Constants for menu choices
PASSWORD_GENERATOR = 1
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
        elif choice == QUIT_CHOICE:
            print('Thank you for using the program.')
            print('Goodbye.')



def display_menu():
    print('\nPlease make a selection below:\n')
    print('MENU')
    print('1) Password Generator')
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

def yes_no_input(text):
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

main()