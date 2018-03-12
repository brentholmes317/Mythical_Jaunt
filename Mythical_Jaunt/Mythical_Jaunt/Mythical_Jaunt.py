from birth1 import Birth
from doorway import Doorway
from grove import Grove
from metropolis import Metropolis
from death import Death
from forest import Forest
from plains import Plains
from elfkingdom import ElfKingdom

"""
This is a game that uses a map and an engine to navigate between various scenes in
the game.  The game has various items that can be collected and the scenese interact
differently with the player based on the player's progress in the game.
"""


class Engine():

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        #the following dictionary keeps track of what items we have and where we have
        #visited.  this affects how the creatures of this world will interact with us
        inv =  {'clothes' : 0, 'smelly_key' : 0, 'ornate_key' : 0, 'fused_key' : 0,
         'birth_visited' : 0, 'grove_visited' : 0, 'plains_visited' : 0,
         'elf_blessing' :0, 'yoogalie_blessing' : 0}

        current_scene = self.scene_map.opening_scene()
        #the player must win, die or command code to exit the game.  The game
        #has no set length so we use this loop to let it run until such a conclusion
        while 1 == 1:
            temp = current_scene.enter(inv)
            next_scene_name = temp[0]
            #we update the inventory.
            inv = temp[1]
            current_scene = self.scene_map.next_scene(next_scene_name)

class Map():

    #translates the strings we receive as returns to which function to call next
    scenes = {
        'birth' : Birth(),
        'grove' : Grove(),
        'metropolis' : Metropolis(),
        'death' : Death(),
        'doorway' : Doorway(),
        'forest' : Forest(),
        'plains' : Plains(),
        'elfkingdom' : ElfKingdom()
        }

    #we provide a place to start
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    #plays the first scene in the game
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('birth')
a_game = Engine(a_map)
a_game.play()
