#!/usr/bin/python3

import os

def clear_screen():
    """Clear the terminal screen."""
    os.system("clear")  # For Unix-like systems
    # os.system("cls")  # Uncomment this line and comment the above line if you are on Windows

def showInstructions():
    # Print the game instructions
    print('''
Amalfi Coast Adventure
========================
Commands:
  go [direction] - Move in the specified direction
  get [item] - Pick up the specified item
  use [item] - Use the specified item (if applicable)
  exit - Quit the game
''')

def showStatus():
    # Print the player's current status
    print('---------------------------')
    print(f'You are in the {currentRoom}.')
    if 'directions' in rooms[currentRoom]:
        print('You can go:', ', '.join(rooms[currentRoom]['directions']))
    print('Inventory: ' + str(inventory))
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    if 'husband' in rooms[currentRoom] and rooms[currentRoom]['husband']:
        print('BUSTED! Your husband has caught you and you can no longer go on a shopping spree!')
    if 'lookout' in rooms[currentRoom] and rooms[currentRoom]['lookout']:
        print('Your best friend is here as a lookout. They warn you that your husband is in the Living Room!')
    print("---------------------------")

# Player's inventory starts empty
inventory = []

# Counter for the number of moves made
move_count = 0

# Dictionary of rooms with directions, items, and special features
rooms = {
    'Master Bedroom': {
        'directions': ['north', 'east', 'south', 'west'],
        'north': 'Secret Passage',
        'east': 'Giant Walk-in Closet',
        'south': 'Gourmet Kitchen',
        'west': 'Elegant Dining Room',
        'item': 'bedside book'
    },
    'Giant Walk-in Closet': {
        'directions': ['west', 'east'],
        'west': 'Master Bedroom',
        'east': 'Elegant Garden',
        'item': 'designer sunglasses',
        'trapdoor': True
    },
    'Elegant Garden': {
        'directions': ['west', 'south', 'east', 'north'],
        'west': 'Giant Walk-in Closet',
        'south': 'Secret Passage',
        'east': 'Luxury Villa',
        'north': 'Elegant Dining Room',
        'item': 'maze key'
    },
    'Secret Passage': {
        'directions': ['north', 'south'],
        'north': 'Elegant Garden',
        'south': 'Master Bedroom',
        'item': 'stack of money'
    },
    'Luxury Villa': {
        'directions': ['west'],
        'west': 'Elegant Garden',
        'item': 'black card',
        'husband': False  # No husband here to catch the player
    },
    'Gourmet Kitchen': {
        'directions': ['north', 'east', 'west'],
        'north': 'Master Bedroom',
        'east': 'Opulent Living Room',
        'west': 'Massive Car Garage',
        'item': 'chef’s knife',
        'lookout': True  # Best friend is in the Kitchen as a lookout
    },
    'Massive Car Garage': {
        'directions': ['east'],
        'east': 'Gourmet Kitchen',
        'item': 'sports car key'
    },
    'Opulent Living Room': {
        'directions': ['west', 'east'],
        'west': 'Gourmet Kitchen',
        'east': 'Elegant Dining Room',
        'item': 'gold card',
        'husband': True  # Husband is in the Living Room
    },
    'Elegant Dining Room': {
        'directions': ['north', 'east', 'south', 'west'],
        'north': 'Gourmet Kitchen',
        'east': 'Giant Walk-in Closet',
        'south': 'Opulent Living Room',
        'west': 'Luxurious Gym',
        'item': 'vintage wine'
    },
    'Luxurious Gym': {
        'directions': ['east', 'south'],
        'east': 'Elegant Dining Room',
        'south': 'Massive Car Garage',
        'item': 'Apple AirPods Max'
    }
}

# Set the starting room to Master Bedroom
currentRoom = 'Master Bedroom'

# Show instructions at the start
showInstructions()

# Main game loop
while True:
    showStatus()  # Show the current status

    # Get the player's next command
    move = input('> ').strip().lower()

    # Split the command into action and item/direction
    command = move.split(" ", 1)

    # Check and process the command
    valid_command = False

    if command[0] == 'exit':
        print('Thank you for playing! Goodbye!')
        break

    elif command[0] == 'go':
        if len(command) > 1:
            direction = command[1]
            if direction in rooms[currentRoom]['directions']:
                nextRoom = rooms[currentRoom][direction]
                # Handle trapdoor
                if 'trapdoor' in rooms[currentRoom] and rooms[currentRoom]['trapdoor']:
                    if direction == 'east' and currentRoom == 'Giant Walk-in Closet':
                        print('The trapdoor prevents you from going back. You are now in the Elegant Garden.')
                        currentRoom = nextRoom
                    else:
                        currentRoom = nextRoom
                else:
                    currentRoom = nextRoom
                move_count += 1  # Increment move count
                valid_command = True
            else:
                print('You can\'t go that way!')

        else:
            print('Specify the direction to go!')

    elif command[0] == 'get':
        if len(command) > 1:
            item = command[1]
            if "item" in rooms[currentRoom] and item == rooms[currentRoom]['item']:
                # Special handling for the stack of money
                if item == 'stack of money':
                    print('You found a stack of money and put it in your purse!')
                inventory.append(item)  # Add item to inventory
                print(item + ' obtained!')
                del rooms[currentRoom]['item']  # Remove item from the room
                valid_command = True
            else:
                print('Can\'t get ' + item + '!')
        else:
            print('Specify the item to get!')

    elif command[0] == 'use':
        if len(command) > 1:
            item = command[1]
            if item == 'maze key' and 'maze key' in inventory and currentRoom == 'Elegant Garden':
                print('You use the maze key to find a hidden path to the Luxury Villa!')
                currentRoom = 'Luxury Villa'
                move_count += 1
                valid_command = True
            else:
                print('You can\'t use ' + item + ' here!')
        else:
            print('Specify the item to use.')

    else:
        print('Unknown command!')

    # Clear the screen only if the command was valid
    if valid_command:
        clear_screen()

    # Check if player has won
    if currentRoom == 'Luxury Villa' and 'black card' in inventory:
        print('You use the black card to enjoy a shopping spree on the Amalfi Coast. You win!')
        print(f'You made {move_count} moves.')
        break

    # Check if player has been caught
    if 'husband' in rooms[currentRoom] and rooms[currentRoom]['husband']:
        print('BUSTED! Your husband has caught you and you can no longer go on a shopping spree. GAME OVER!')
        print(f'You made {move_count} moves.')
        break

