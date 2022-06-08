"""Program author: Ryan Miskovic
Date: 6/6/2022
program purpose: This program is to demonstrate skills learned using
operations on different data structures, using imported modules,
creating image plots and graphs with matplotlib."""

import os
from heapq import nlargest
import matplotlib.pyplot as plt

#Constants for menu
QUIT_CHOICE = 9
ALL_STATES = 1
STATE_SEARCH = 2
BAR_GRAPH = 3
UPDATE_POPULATION = 4

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
        if choice == ALL_STATES:
            displ_all_states()
        elif choice == STATE_SEARCH:
            search_state()
        elif choice == BAR_GRAPH:
            bar_graph()
        elif choice == UPDATE_POPULATION:
            update_population()
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
    print('1) Print all states and info')
    print('2) Search for info by state name')
    print('3) Show a bar graph of the largest states')
    print('4) Update a states population value.')
    print('9) Quit')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def welcome_message():
    """Displays opening message to user."""

    print('Hello! Welcome to the state information program!')
    print('Below you will find several useful options!')

def displ_all_states():
    """Displays all state information in a list.

    function creates and alphabetizes a list of state names from dictionary keys,
    then displays info to the user by iterating through its list and calling
    the state_info() function for each state in the list."""

    all_states = list(us_states)
    all_states.sort()
    print('\nList start ~~~~~~~~~~~~~~\n')
    for state in all_states:
        state_info(state)
    print('List end ~~~~~~~~~~~~\n')

def state_info(state):
    """Displays specified state info to user.

    When called, this function extracts data from us_states dictionary
    and creates variables for name, capital, population, and flower
    from dictionary values. The function then displays the data to the user."""

    state_name = state
    capital = us_states[state][0]
    population = us_states[state][1]
    flower = us_states[state][2]

    print(state_name)
    print('Capital: '+ capital)
    print('Population: '+ population)
    print('State flower: ' + flower + '\n')

def state_info_img(state):
    """This function dispplays state info and a state flower image.

    function creates a variable for absolute path to the .jpeg file
    that matches the state passed in. The .jpeg file is then read into
    an image variable which is displayed to the user in a matplotlib window.
    The specified states information is also displayed."""

    #variables created to hold filepath.
    flower_img = us_states[state][3]

    #current working directory and filname held in dictionary are joined here.
    flower_path = os.path.abspath(os.path.join(os.getcwd(), flower_img))

    #state flower image is generated here.
    img = plt.imread(flower_path)
    state_info(state)

    #call to display flower image.
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def valid_state(text):
    """Validates that user input matches an existing dictionary key.

    A validation tool which requests a state name from the user, then
    interates through the state list in an attempt to find a match.
    If a match is found, the input is returned to the calling function.
    If no match is found the user is prompted to try again."""

    state_list = list(us_states)
    state_input = None
    while state_input is None:
        state_input = input(text)
        state_input = state_input.title()
        print('You entered: ' + state_input)
        if state_input in state_list:
            return state_input

        state_input = None
        print('I\'m sorry, I don\'t know that state name.')

def search_state():
    """Searches for a user requested state info.

    This is the top level function which takes input from the user and uses
    the validate_state() and state_info_img() functions to display the
    requested state info to the user."""

    state = valid_state('Please enter a state name to search: ')
    state_info_img(state)

def state_pop(dictionary):
    """function to create new dictionary for state populations.

    function iterates through us_states and creates a new dictionary
    with state names as keys and only population as values.
    the new dictionary is the returned to the calling function."""

    state_pops = {}
    for key in dictionary:
        state_pops[key] = int(dictionary[key][1])
    return state_pops

def max_names(dictionary):
    """Generates a list of the 5 top population states.

    The new population dictionary is searched for the 5 highest
    population states with nlargest(). The resulting list of state
    names is returned to the calling function."""

    five_names = nlargest(5, dictionary, key=dictionary.get)
    return five_names

def bar_graph():
    """Generates a bar graph of populations for the five largest states.

    state_pop() and five_states() are used to create a list of names and a list of numbers.
    The values are passed into matplotlib and processed into a viewable graph."""
    dictionary = us_states
    populations = state_pop(dictionary)
    five_states = max_names(populations)
    five_pops = [populations[name] for name in five_states]

    plt.figure(figsize=(7,7))
    plt.bar(five_states, five_pops)
    plt.axis([-1,5,0,40000000])
    plt.title('Highest five state populations')
    plt.ylabel('Population in 10\'s of millions')
    plt.xlabel('U.S. State')
    plt.show()

def update_population():
    """Updates a states population value.

    Function changes the population value in the value list of
    a state specified by the user. It then displays the old and new
    values to the user."""

    mod_state = valid_state('Enter a state to modify: ')
    population = int_input('Enter a new population number: ')
    population = str(population)

    print(mod_state + '\'s old population value is: ' + us_states[mod_state][1])
    us_states[mod_state][1] = population
    print(mod_state + '\'s new population value is: ' + us_states[mod_state][1])


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

us_states = {
    'Alabama':['Montgomery','4918689','Camellia', r'flowers\camellia.jpg'],
    'Alaska':['Juneau', '727951', 'Forget Me Not', r'flowers\forgetmenot.jpg'],
    'Arizona':['Phoenix', '7399410', 'Saguaro Cactus Blossom', r'flowers\saguaroflower.jpg'],
    'Arkansas':['Little Rock', '3025875', 'Apple Blossom', r'flowers\arappleblossom.jpg'],
    'California':['Sacramento', '39562858', 'California Poppy', r'flowers\californiapoppy.jpg'],
    'Colorado':['Denver', '5826185', 'Columbine', r'flowers\columbine.jpg'],
    'Connecticut':['Hartford', '3559054', 'Mountain Laurel', r'flowers\mountainlaurel.jpg'],
    'Delaware':['Dover', '982049', 'Peach Blossom', r'flowers\peachblossom.jpg'],
    'Florida':['Tallahassee', '21711157', 'Coreopsis', r'flowers\coreopsis.jpg'],
    'Georgia':['Atlanta', '10723715', 'Cherokee Rose', r'flowers\cherokeerose.jpg'],
    'Hawaii':['Honolulu', '1411151', 'Hibiscus', r'flowers\hibiscus.jpg'],
    'Idaho':['Boise', '1823594', 'Syringa', r'flowers\syringa.jpg'],
    'Illinois': ['Springfield', '12620571', 'Purple Violet', r'flowers\illinoisviolet.jpg'],
    'Indiana':['Indianapolis', '6768941', 'Peony', r'flowers\peony.jpg'],
    'Iowa': ['Des Moines', '3161522', 'Wild Prairie Rose', r'flowers\wildprairierose.jpg'],
    'Kansas':['Topeka', '2915269', 'Sunflower', r'flowers\sunflower.jpg'],
    'Kentucky':['Frankfort', '4474193', 'Goldenrod', r'flowers\kygoldenrod.jpg'],
    'Louisiana':['Baton Rouge', '4637898', 'Magnolia', r'flowers\magnolia.jpg'],
    'Maine':['Augusta', '1349367', 'White Pine Cone and Tassel', r'flowers\whitepinecone.jpg'],
    'Maryland':['Annapolis', '6055558', 'Black-Eyed Susan', r'flowers\blackeyedsusan.jpg'],
    'Massachusetts':['Boston', '6902371', 'Mayflower', r'flowers\mayflower.jpg'],
    'Michigan':['Lansing', '9989642', 'Apple Blossom', r'flowers\miappleblossom.jpg'],
    'Minnesota':['Saint Paul', '5673015', 'Pink and White Lady Slipper',
    r'flowers\pinkwhiteladysslipper.jpg'],
    'Mississippi':['Jackson', '2971278', 'Magnolia', r'flowers\magnolia.jpg'],
    'Missouri':['Jefferson City', '6153233', 'White Hawthorn Blossom',
    r'flowers\hawthornblossom.jpg'],
    'Montana':['Helena', '1076891', 'Bitterroot', r'flowers\bitterroot.jpg'],
    'Nebraska':['Lincoln', '1943202', 'Goldenrod', r'flowers\negoldenrod.jpg'],
    'Nevada':['Carson City', '3132971', 'Sagebrush', r'flowers\sagebrush.jpg'],
    'New Hampshire':['Concord', '1365957', 'Purple Lilac', r'flowers\purplelilac.jpg'],
    'New Jersey':['Trenton', '8878355', 'Violet', r'flowers\njviolet.jpg'],
    'New Mexico':['Santa Fe', '2100917', 'Yucca Flower', r'flowers\yucca.jpg'],
    'New York':['ALbany', '19376771', 'Rose', r'flowers\rose.jpg'],
    'North Carolina':['Raleigh', '10594553', 'Dogwood', r'flowers\dogwood.jpg'],
    'Ohio':['Columbus', '11701859', 'Scarlet Carnation', r'flowers\redcarnation.jpg'],
    'Oklahoma':['Oklahoma City', '3973707', 'Oklahoma Rose', r'flowers\oklahomarose.jpg'],
    'Oregon':['Salem', '4253588', 'Oregon Grape', r'flowers\oregongrape.jpg'],
    'Pennsylvania':['Harrisburg', '12803056', 'Mountain Laurel', r'flowers\pamountainlaurel.jpg'],
    'Rhode Island':['Providence', '1060435', 'Violet', r'flowers\riviolet.jpg'],
    'South Carolina':['Columbia', '5213272', 'Yellow Jessamine', r'flowers\yellowjessamine.jpg'],
    'North Dakota':['Bismark', '766044', 'Wild Prairie Rose', r'flowers\wildprairierose.jpg'],
    'South Dakota':['Pierre', '890620', 'Pasque Flower', r'flowers\pasque.jpg'],
    'Tennessee':['Nashville', '6886717','Iris', r'flowers\tniris.jpg'],
    'Texas':['Austin', '29363096', 'Bluebonnet', r'flowers\bluebonnet.jpg'],
    'Utah':['Salt Lake City', '3258366', 'Sego Lily', r'flowers\segolily.jpg'],
    'Vermont':['Montpelier', '623620','Red Clover', r'flowers\redclover.jpg'],
    'Virginia':['Richmond', '8569752', 'Dogwood', r'flowers\vadogwood.jpg'],
    'Washington':['Olympia', '7705917', 'Pink Rhododendron', r'flowers\pinkrhododendron.jpg'],
    'West Virginia':['Charleston', '1780003', 'Rhododendron', r'flowers\rhododendron.jpg'],
    'Wisconsin':['Madison', '5837462', 'Wood Violet', r'flowers\woodviolet.jpg'],
    'Wyoming':['Cheyenne', '579917', 'Indian Paintbrush', r'flowers\indianpaintbrush.jpg']

}

main()
