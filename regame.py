from sys import exit

class Room(object):
    
    def __init__(self):
        self.room_coins = []
          
    def enter(self):
        print("This room is not complete yet. Give it an enter()")
        exit(0)
        
class Player(object):
    
    def __init__(self):
        self.coin = []
        self.moves = 0
        self.room_coins = []
        
    def coin_counter(self):
        total_coins = sum(self.coin)
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

class Engine(object):
        
    def __init__(self, engine):
        self.engine = engine
            
    def navigate(self):
        current_room = self.engine.start_room()
        last_room = self.engine.next_room('win')
        
        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.engine.next_room(next_room_name)
        
        current_room.enter()
    
class EntryWay(Room):
    
    def enter(self):
        print("You are standing in the entry to the demiplane")
        print("of elements. There is little light, a little wind, and")
        print("a lot of noise. Ahead of you, to the north, the light grows")
        print("stronger.")
        print("What are you going to do?")

        while True:
            choice = input("> ")
                        
            if "north" in choice:
                player1.moves += 1
                return 'sand_storm'
            elif "look" in choice:
                print("There really isn't enough light to see anything.")
            elif "feel" in choice:
                print("You feel around. You actually find a hole! What now?")
            elif "hole" in choice or "enter" in choice:
                player1.moves += 1
                return 'gold'
            elif "coins" in choice:
                player1.coin_counter()
            elif "moves" in choice:
                player1.move_counter()
            elif "give up" in choice or "stuck" in choice:
                print("Well that's too bad.")
                player1.stuck()
            else:
                print("Try something else, that didn't help.")   
   
class Volcano(Room):
    
    def enter(self):
        print("""Volcano""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "north" in choice:
                player1.moves += 1
                return 'fire'
            elif "south" in choice:
                player1.moves += 1
                return 'earth'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Sand_storm(Room):
    
    def enter(self):
        if "sun_coin" in player1.room_coins:
            print("A dust devil suddenly picks you up and you are deposited")
            print("back in the middle of the sandstorm at the pedestal.")
            print("Blast it all!")
            print("You can still see the wind tunnels through the storm to the")
            print("east and west and the demiplane entry to the south.")
            print("What now?")
            while True:
                choice = input("> ")
                if "east" in choice:
                    player1.moves += 1
                    return 'wind'
                elif "west" in choice:
                    player1.moves += 1
                    return 'earth'
                elif "south" in choice:
                    player1.moves += 1
                    return 'entry_way'
                elif "coins" in choice:
                    player1.coin_counter()
                elif "moves" in choice:
                    player1.move_counter()
                elif "stuck" in choice or "give up" in choice:
                    player1.stuck()
                else:
                    print("The sandstorm continues and you are still here. Ya gotta do something here.")
        else:
            print("As you walk towards the light, wind starts to buffet you. You can see")
            print("the ground you're walking on is a hard black sand. As you continue the wind gets")
            print("stronger and is picking up sand. You try to shield your face but to no avail.") 
            print("Eventually you come to a small pedestal that reads:\n")
            print("-" * 10)
            print("I am the beginning of the end, the end of every place. I am the beginning of eternity,")
            print(" the end of time and space. Say my name.")
            print("-" * 10)
            print("You can see the entry to the demiplane to the south. All you see in any other ")
            print("directions is sand.")
            print("What do you do?")
            
            sun_coin = 0
            while True:
                choice = input("> ")
                
                if "e" in choice and ("say" in choice or "speak" in choice) and sun_coin != 1:
                    print("'E' is the right answer! After saying the letter the riddle disappears and ")
                    print("a hole opens in the pedestal. Inside you see a coin.")
                    print("Do you take the coin?")
                    
                    while sun_coin < 1:
                        take_coin = input("> ")
                        if "yes" in take_coin:
                            print("You grab the coin. After you remove the coin the wind picks up. You almost")
                            print("Can't stand up it's so strong. After a moment wind tunnels appear to the")
                            print("east and the west.")
                            player1.coin.append(1)
                            sun_coin = 1
                            player1.room_coins.append("sun_coin")
                        else:
                            print("Why wouldn't you take the coin? Say yes to the coin! (really, type 'yes')")                    
                elif "east" in choice and sun_coin == 1:
                    player1.moves += 1
                    return 'wind'
                elif "west" in choice and sun_coin == 1:
                    player1.moves += 1
                    return 'earth'
                elif "south" in choice:
                    player1.moves += 1
                    return 'entry_way'
                elif "coins" in choice:
                    player1.coin_counter()
                elif "moves" in choice:
                    player1.move_counter()
                elif "stuck" in choice or "give up" in choice:
                    player1.stuck()
                else:
                    print("The sandstorm continues and you are still here. Ya gotta do something here.")    

class Fire(Room):
    
    def enter(self):
        print("""Fire""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "east" in choice:
                player1.moves += 1
                return 'geyser'
            elif "south" in choice:
                player1.moves +=1 
                return 'volcano'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Earth(Room):
    
    def enter(self):
        if "earth_coin" in player1.room_coins:
            print("""You        """)
        else:
            print("Earth")
            
            while True:
                choice = input("> ")
                
                if "hello world" in choice:        
                    print("Hello World")
                elif "east" in choice:
                    player1.moves += 1
                    return 'sand_storm'
                elif "north" in choice:
                    player1.moves += 1
                    return 'volcano'
                elif "stuck" in choice or "give up" in choice:
                    player1.stuck()
                elif "moves" in choice:
                    player1.move_counter()
                elif "coins" in choice:
                    player1.coin_counter()
                else:
                    print("Try something else.")

class Water(Room):
    
    def enter(self):
        print("""Water""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "west" in choice:
                player1.moves += 1
                return 'geyser'
            elif "south" in choice:
                player1.moves += 1
                return 'hurricaine'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try again")

class Wind(Room):
    
    def enter(self):
        print("""Wind""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            if "west" in choice:
                player1.moves += 1
                return 'sand_storm'
            if "north" in choice:
                player1.moves += 1
                return 'hurricaine'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Hurricaine(Room):
    
    def enter(self):
        print("""Hurricaine""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "north" in choice:
                player1.moves += 1
                return 'water'
            elif "south" in choice:
                player1.moves += 1
                return 'wind'
            elif "west" in choice:
                player1.moves +=1
                return 'prismatic'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Prismatic(Room):
    
    def enter(self):
        print("""Prismatic""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "east" in choice:
                player1.moves += 1
                return 'hurricaine'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Gold(Room):
    
    def enter(self):
        if "gold_coin" in player1.room_coins:
            print("The room is the same as when you left it.")
            print("It is very gold and contains a very empty wooden box.")
        else:
            print("You exit the hole and find yourself")
            print("in a room so yellow you feel a little sick.")
            print("Everything is covered in gold. In the middle")
            print("of the room is a simple wooden box.")
        
            gold_coin = 0
            while True:
                choice = input("> ")
                
                if "box" in choice and "open" in choice:
                    print("You open the box and find 5 coins. Now what?")
                    while gold_coin == 0:
                        take_coin = input("> ")
                        if "take" in take_coin:
                            print("You grab the coins. Now what?")
                            player1.coin.append(5)
                            gold_coin = 5
                            player1.room_coins.append("gold_coin")
                        else:
                            print("Why wouldn't you take the coins? Take them? (type 'take')")
                elif "stuck" in choice or "give up" in choice:
                    player1.stuck()
                elif "return" in choice or "back" in choice or "hole" in choice:
                    player1.moves += 1
                    return 'entry_way'
                elif "coins" in choice:
                    player1.coin_counter()
                elif "moves" in choice:
                    player1.move_counter()
                else:
                    print("That didn't help at all. Maybe try another action.")

class Geyser(Room):
    
    def enter(self):
        print("""Geyser""")
        
        while True:
            choice = input("> ")
            
            if "stuck" in choice or "give up" in choice:
                player1.stuck()
            elif "east" in choice:
                player1.moves += 1
                return 'water'
            elif "west" in choice:
                player1.moves += 1
                return 'fire'
            elif "moves" in choice:
                player1.move_counter()
            elif "coins" in choice:
                player1.coin_counter()
            else:
                print("Try something else.")

class Win(Room):
    
    def enter(self):
        pass
 
# How to manage the rooms in the game 
class Map(object):
    
    rooms = {
        'volcano': Volcano(),
        'earth': Earth(),
        'sand_storm': Sand_storm(),
        'water': Water(),
        'fire': Fire(),
        'geyser': Geyser(),
        'hurricaine': Hurricaine(),
        'prismatic': Prismatic(),
        'wind': Wind(),
        'gold': Gold(),
        'entry_way': EntryWay(),
        'win': Win()
    }
            
    def __init__(self, first_room):
        self.first_room = first_room
       
    def next_room(self, room_name):
        next_room = Map.rooms.get(room_name)
        return next_room
        
    def start_room(self):
        return self.next_room(self.first_room)
        

# Start up the game        
room_start = Map('entry_way')
my_game = Engine(room_start)
player1 = Player()
my_game.navigate()