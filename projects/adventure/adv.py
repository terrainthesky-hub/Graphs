from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


from util import Queue
from util import Graph
import random

class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

#a dictionary stores a key value pair, and the value can be a set of values. Maybe
#I want a nested dictionary

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
#map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

print(player.current_room.get_exits())
print(player.current_room.id)
player.travel('n')
print(player.current_room.get_exits())
print(player.current_room.id)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']

traversal_path = []


#U
##Can move n, s, w, e unless restricted in one or more directions. There's a get exits with a method which gives you
##an array called exits with 'n','s','w','e', if not none. I want to create a dictionary to store the rooms, and have a
##nested? dictionary that stores '?' if it isn't known if a room can be traversed. 
# Room has get room in direction
##may need to mark rooms as untraversable with get_exits() 
##`player.current_room.id`, `player.current_room.get_exits()` and `player.travel(direction)` are useful commands to write
#Need to back up at dead ends.

#P

##move the player (player.travel()), out of a random choice of n,s,w,e strings in an array. 
## get the room and create a dictionary with values assigned to n,s,w,e--if
## untraversed put a '?' there in the dictionary. When you move N, the next room's
## S is the previous room id, and the previous room's N is the current room id.
## Do the same with E and W, S and N, W and E, check if not a '?' if it is not '?',
## don't fill in the value 
## Begin a DFT, get neighbor
## algorithim for dead ends should be an array that takes in the movement pattern
## at the last non-dead end (you can only move one direction and it's visited)
## populate the array per step, once at a dead end, reverse the directions in the array
## with a dictionary that and swaps and maps the values.
## Once not at dead end, get neighbor again with a random traversal in a not
## known direction.

## once 500 rooms are filled in the dictionary
## do a BFS of the best path to traverse every node
## BFS? possible w/ robot limitations?


def first_traversal(self):


    room_id = player.current_room.id
    current_room_exits = player.current_room.get_exits()
    previous_room = player.current_room.id

    all_rooms = {}
    backtrack = []
    q = Stack()
    q.push(room_id)
    random_direction = str(random.choice(current_room_exits)
    while len(all_rooms) < 499:

        v = q.pop()
        if all_rooms[room_id]['n'] == '?' and all_rooms[room_id]['s'] == '?' and all_rooms[room_id]['w'] == '?', all_rooms[room_id]['e'] == '?':
            robot_choice = (random_direction)
            previous_room = player.current_room.id


            movement = player.travel(robot_choice)
            backtrack.append(movement)
            current_room = player.current_room.id


        if v not in all_rooms:
                
            if robot_choice == 'n':
                all_rooms[room_id] = {'n': '?', 's': previous_room, 'w': '?', 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('n')

            if robot_choice == 's':
                all_rooms[room_id] = {'n': previous_room, 's': '?', 'w': '?', 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('s')
            if robot_choice == 'w':
                all_rooms[room_id] = {'n': '?', 's': '?', 'w': '?', 'e':previous_room}
                q.push(player.current_room.id)
                backtrack.append('w')
            if robot_choice == 'e':
                all_rooms[room_id] = {'n': '?', 's': '?', 'w': previous_room, 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('e')
        if v in all_rooms:
            
            if len(player.current_room.get_exits()) == 1:
                btmap = {'n':'s', 'w':'e', 's':'n', 'e', 'w'}
                btmap.map(backtrack)
                for movement in backtrack:
                    player.travel(movement)


            if robot_choice == 'n':
                all_rooms[room_id] = {'n': '?', 's': previous_room, 'w': '?', 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('n')
            if robot_choice == 's':
                all_rooms[room_id] = {'n': previous_room, 's': '?', 'w': '?', 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('s')
            if robot_choice == 'w':
                all_rooms[room_id] = {'n': '?', 's': '?', 'w': '?', 'e':previous_room}
                q.push(player.current_room.id)
                backtrack.append('w')
            if robot_choice == 'e':
                all_rooms[room_id] = {'n': '?', 's': '?', 'w': previous_room, 'e':'?'}
                q.push(player.current_room.id)
                backtrack.append('e')
                


        q.push(current_room)





# # TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
