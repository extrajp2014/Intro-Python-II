from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["sword", "shield"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["laptop"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["statue"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["calculator"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
if __name__ == "__main__":
    player = Player(room['outside'])
    assert player.current_room.name == "Outside Cave Entrance"

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(player)
    print(player.current_room)
    cmd = input(
        'What do you want to do? Possible options are move, take or q to quit the game > ').lower().strip()
    if cmd == 'q':
        break        
    elif cmd == 'move':
        move = input(
            'Where do you want to go? Possible options are north, south, east, west, or q to quit the game > ').lower().strip()
        if move == 'q':
            break
        elif player.current_room.name == room["outside"].name and move == 'north':
            player.current_room = room['outside'].n_to
        elif player.current_room.name == room["foyer"].name and move == 'north':
            player.current_room = room['foyer'].n_to
        elif player.current_room.name == room["foyer"].name and move == 'south':
            player.current_room = room['foyer'].s_to
        elif player.current_room.name == room["foyer"].name and move == 'east':
            player.current_room = room['foyer'].e_to
        elif player.current_room.name == room["overlook"].name and move == 'south':
            player.current_room = room['overlook'].s_to
        elif player.current_room.name == room["narrow"].name and move == 'north':
            player.current_room = room['narrow'].n_to
        elif player.current_room.name == room["narrow"].name and move == 'south':
            player.current_room = room['narrow'].s_to
        elif player.current_room.name == room["narrow"].name and move == 'west':
            player.current_room = room['narrow'].w_to
        else:
            print("Incorrect input or you cannot you go there.")
            continue
    elif cmd == 'take':
        item= input(
            f'What do you want to take? {player.current_room.items}> ').lower().strip()
        if item == 'q':
            break
        elif item in player.current_room.items:
            player.take(item)
        else:
            print("Incorrect input.")
            continue
    else:
        print("Incorrect input.")
        continue
