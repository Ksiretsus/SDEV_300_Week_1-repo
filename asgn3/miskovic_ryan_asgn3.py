import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import webbrowser

#Constants for menu
QUIT_CHOICE = 9
ALL_STATES = 1
STATE_SEARCH = 2

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
        if choice == ALL_STATES:
            all_states()
        elif choice == STATE_SEARCH:
            search_state()
        #elif choice == DAYS_UNTIL:
            #days_until()
        #elif choice == CALCULATE_LEG_C:
            #calculate_side_c()
        #elif choice == RIGHT_CYLINDER_VOLUME:
            #right_cylinder_vol()
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
    #print('3) Days until July 4th, 2025')
    #print('4) Calculate side c of a triangle.')
    #print('5) Calulate the volume of a cylinder')
    print('9) Quit')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

def welcome_message():
    """Displays opening message to user."""

    print('Hello! Welcome to the state information program!')
    print('Below you will find several useful options!')

def all_states():
    all_states = [state for state in us_states]
    all_states.sort()
    print('\nList start ~~~~~~~~~~~~~~\n')
    for state in all_states:
        state_info(state)
    print('List end ~~~~~~~~~~~~\n')

def state_info(state):

    state_name = state
    capital = us_states[state][0]
    population = us_states[state][1]
    flower = us_states[state][2]

    print(state_name)
    print('Capital: '+ capital)
    print('Population: '+ population)
    print('State flower: ' + flower + '\n')

def state_info_img(state):

    cwd = os.getcwd()

    flower_img = us_states[state][3]
    #print(cwd)
    #print(flower_img)
    flower_path = os.path.realpath(flower_img)
    #print(flower_path)
    img = mpimg.imread(flower_path)
    state_info(state)
    plt.imshow(img)
    #webbrowser.open(flower_path)
    os.system(flower_path)

def valid_state():

    state_list = [state for state in us_states]
    state_input = None
    while state_input == None:
        state_input = input('Please enter a state name to search: ')
        state_input = state_input.capitalize()
        print('You entered: ' + state_input)
        if state_input in state_list:
            return state_input
        else:
            state_input = None
            print('I\'m sorry, I don\'t know that state name.')

def search_state():

    state = valid_state()
    state_info_img(state)

            

us_states = {
    'Alabama':['Montgomery','4918689','Camellia', 'flowers\camellia.jpg'], 'Alaska':['Juneau', '727951', 'Forget Me Not', 'flowers\\forgetmenot.jpg'],
    'Arizona':['Phoenix', '7399410', 'Saguaro Cactus Blossom', 'flowers\saguaroflower.jpg'], 'Arkansas':['Little Rock', '3025875', 'Apple Blossom', 'flowers\\arappleblossom.jpg'],
    'California':['Sacramento', '39562858', 'California Poppy', 'flowers\californiapoppy.jpg'], 'Colorado':['Denver', '5826185', 'Columbine', 'flowers\columbine.jpg'],
    'Connecticut':['Hartford', '3559054', 'Mountain Laurel', 'flowers\mountainlaurel.jpg'], 'Delaware':['Dover', '982049', 'Peach Blossom', 'flowers\peachblossom.jpg'],
    'Florida':['Tallahassee', '21711157', 'Coreopsis', 'flowers\coreopsis.jpg'], 'Georgia':['Atlanta', '10723715', 'Cherokee Rose', 'flowers\cherokeerose.jpg'],
    'Hawaii':['Honolulu', '1411151', 'Hibiscus', 'flowers\hibiscus.jpg'], 'Idaho':['Boise', '1823594', 'Syringa', 'flowers\syringa.jpg'],
    'Illinois': ['Springfield', '12620571', 'Purple Violet', 'flowers\illinoisviolet.jpg'], 'Indiana':['Indianapolis', '6768941', 'Peony', 'flowers\peony.jpg'],
    'Iowa': ['Des Moines', '3161522', 'Wild Prairie Rose', 'flowers\wildprairierose.jpg'], 'Kansas':['Topeka', '2915269', 'Sunflower', 'flowers\sunflower.jpg'],
    'Kentucky':['Frankfort', '4474193', 'Goldenrod', 'flowers\kygoldenrod.jpg'], 'Louisiana':['Baton Rouge', '4637898', 'Magnolia', 'flowers\magnolia.jpg'],
    'Maine':['Augusta', '1349367', 'White Pine Cone and Tassel', 'flowers\whitepinecone.jpg'], 'Maryland':['Annapolis', '6055558', 'Black-Eyed Susan', 'flowers\\blackeyedsusan.jpg'],
    'Massachusetts':['Boston', '6902371', 'Mayflower', 'flowers\mayflower.jpg'], 'Michigan':['Lansing', '9989642', 'Apple Blossom', 'flowers\miappleblossom.jpg'],
    'Minnesota':['Saint Paul', '5673015', 'Pink and White Lady Slipper', 'flowers\pinkwhiteladysslipper.jpg'], 'Mississippi':['Jackson', '2971278', 'Magnolia', 'flowers\magnolia.jpg'],
    'Missouri':['Jefferson City', '6153233', 'White Hawthorn Blossom', 'flowers\hawthornblossom.jpg'], 'Montana':['Helena', '1076891', 'Bitterroot', 'flowers\\bitterroot.jpg'],
    'Nebraska':['Lincoln', '1943202', 'Goldenrod', 'flowers\\negoldenrod.jpg'], 'Nevada':['Carson City', '3132971', 'Sagebrush', 'flowers\sagebrush.jpg'],
    'New Hampshire':['Concord', '1365957', 'Purple Lilac', 'flowers\purplelilac.jpg'], 'New Jersey':['Trenton', '8878355', 'Violet', 'flowers\\njviolet.jpg'],
    'New Mexico':['Santa Fe', '2100917', 'Yucca Flower', 'flowers\yucca.jpg'], 'New York':['ALbany', '19376771', 'Rose', 'flowers\\rose.jpg'],
    'North Carolina':['Raleigh', '10594553', 'Dogwood', 'flowers\dogwood.jpg'], 'Ohio':['Columbus', '11701859', 'Scarlet Carnation', 'flowers\\redcarnation.jpg'],
    'Oklahoma':['Oklahoma City', '3973707', 'Oklahoma Rose', 'flowers\oklahomarose.jpg'], 'Oregon':['Salem', '4253588', 'Oregon Grape', 'flowers\oregongrape.jpg'],
    'Pennsylvania':['Harrisburg', '12803056', 'Mountain Laurel', 'flowers\pamountainlaurel.jpg'], 'Rhode Island':['Providence', '1060435', 'Violet', 'flowers\\riviolet.jpg'],
    'South Carolina':['Columbia', '5213272', 'Yellow Jessamine', 'flowers\yellowjessamine.jpg'], 'North Dakota':['Bismark', '766044', 'Wild Prairie Rose', 'flowers\wildprairierose.jpg'],
    'South Dakota':['Pierre', '890620', 'Pasque Flower', 'flowers\pasque.jpg'], 'Tennessee':['Nashville', '6886717','Iris', 'flowers\\tniris.jpg'],
    'Texas':['Austin', '29363096', 'Bluebonnet', 'flowers\\bluebonnet.jpg'], 'Utah':['Salt Lake City', '3258366', 'Sego Lily', 'flowers\segolily.jpg'],
    'Vermont':['Montpelier', '623620','Red Clover', 'flowers\\redclover.jpg'], 'Virginia':['Richmond', '8569752', 'Dogwood', 'flowers\\vadogwood.jpg'],
    'Washington':['Olympia', '7705917', 'Pink Rhododendron', 'flowers\pinkrhododendron.jpg'], 'West Virginia':['Charleston', '1780003', 'Rhododendron', 'flowers\\rhododendron.jpg'],
    'Wisconsin':['Madison', '5837462', 'Wood Violet', 'flowers\woodviolet.jpg'], 'Wyoming':['Cheyenne', '579917', 'Indian Paintbrush', 'flowers\indianpaintbrush.jpg']
    
}

main()
