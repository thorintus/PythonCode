'''
Created on Dec 18, 2015

@author: m105822
'''

import json, sys

class Room(object):
    def __init__(self, name):
        self.object = name
        description = ""
        coins = ""
        directions = {}
        puzzle = {}
        loots = []
    
    def add_coins(self):
        pass
    
    def add_loots(self):
        pass
    
       
class Person():
    def __init__(self):
        moves = 0
        coins = 0
        room_coins = []
        loots = []
            
    def coin_counter(self):
        total_coins = sum(self.coins)
        if total_coins == 0:
            print("You haven't collected any coins.")
        elif total_coins < 2:
            print("You have collected one coin.") 
        else:
            print("You have collected %d coins." % total_coins)

    def move_counter(self):
        if self.moves == 0:
            print("You haven't gone anywhere!")
        elif self.moves == 1:
            print("You have moved once.")
        else:
            print("You have moved %d times." % self.moves)
    
    def stuck(self):
        print("You have stumbled around here so long")
        print("you have forgotten why you're here.")
        print("It has become so pleasant you decide to stay.\n")
        self.move_counter()
        self.coin_counter()
        exit(0)
        
class Engine:
    def __init__(self, engine):
        self.engine = engine
    
    
class Map:
    def __init__(self):
        pass
        
    def create_rooms(self):
        room_source = open("json_rooms.json")
        room_info = json.load(room_source)
        room_names = room_info.get('rooms')
        for k in room_names:
            print(k)
            k = Room(k)   
            
game = Map()
player = Person()
game.create_rooms()
        