import sys, time
from pynput.keyboard import Key, Listener

global ROOMS

ROOMS = {}

text = ''

item = ''

item_num = 0

option = ''

global speed

with Listener(on_press = on_press) as listener:
    listener.join()

def on_press(Key):
    pass

def say(text, spee):                             #print slowly
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(spee)

        if Key:
            spee = 0
        
        else:
            spee = speed
    
    spee = speed


def choice(num_1, num_2):
    global option
    global speed
    option = input()

    if option.isnumeric():
        option = int(option)
        
        if option in range(num_1, num_2 + 1):
            return option
        
        else:
            say('Please choose an option\n', speed)
            choice(num_1, num_2)

    else:
        say('Please choose an option\n', speed)
        choice(num_1, num_2)

#puzzles

def key_puzzle():
    say('There is a gun on the counter and two targets on the wall.\nAbove the targets is a sign that says "what was in the closet?"\nUnder the left target there is a sign that says "shelves"\nAnd under the right a sign that says "a cabinet"\n', speed)
    time.sleep(0.2)
    say('1.Shoot left target\n2.Shoot right target\n', speed)
    choice(1, 2)

    if option == 1:
        say('Correct\n', speed)
        ply.room.items.append('key')
        ply.room.puzzles = None

    elif option == 2:
        say('Wrong\n', speed)
        key_puzzle()
    
def statue_puzzle():
    say('There are two statues and a crown, there is a plaque on the floor that says "where am I?"\nOne statue has an arrow pointing down and to the right\nThe other has an arrow pointing up and to the right\n', speed)
    say('1.Put the crown on the down and to the right statue\n2.Put the crown on the up and to the right statue\n', speed)
    choice(1, 2)

    if option == 1:
        say('Correct\n', speed)
        ply.room.items.append('big key')
        ply.room.puzzles = None
    
    elif option == 2:
        say('Wrong\n', speed)
        statue_puzzle()

def math_puzzle():
    say('There is a sign that says 3 x 8 / 6 + 2\nAnd a number pad\n', speed)
    say('Answer\n', speed)
    choice(0, 100)

    if option == 6:
        say('Correct\n', speed)
        ply.room.items.append('big key')
        ply.room.puzzles = None

    elif option < 6:
        say('Wrong\n', speed)
        math_puzzle()
    
    elif option > 6:
        say('Wrong\n', speed)
        math_puzzle()
    
def simon_says_puzzle():
    say('There is a grid with a red square, a blue, square, a green square, and a blank square\n', speed)
    say('The blank square lights up blue\n', speed)
    say('1.Red\n2.Blue\n3.Green\n', speed)
    choice(1, 3)

    if option == 3:
        say('The blank square lights up green\n', speed)
        say('1.Red\n2.Blue\n3.Green\n', speed)
        choice(1, 3)

        if option == 1:
            say('The blank square lights up red\n', speed)
            say('1.Red\n2.Blue\n3.Green\n', speed)
            choice(1, 3)

            if option == 2:
                say('Correct', speed)
                ply.room.items.append('big key')
                ply.room.puzzles = None
            
            elif option == 1:
                simon_says_puzzle()
            
            elif option == 3:
                simon_says_puzzle()
        
        elif option == 2:
            simon_says_puzzle()
    
    elif option == 2:
        simon_says_puzzle()

def red_key_puzzle():
    say('The jukebox has 3 buttons, one is labled red, another is labled blue, and the last is labled green\n', speed)
    say('1.Red\n2.Blue\n3.Green\n', speed)
    choice(1, 2)

    if option == 1:
        say('Correct\n', speed)
        ply.room.items.append('red key')
        ply.room.items.append('key')
        ply.room.puzzles = None
    
    elif option == 2:
        say('Wrong\n', speed)
        red_key_puzzle()

def blue_key_puzzle():
    say('There is a clock that is moving backwards\nAnd two clocks moving forwards\n', speed)
    say('1.Stop one clock\n2.Make all move forwards\n3.Make all move backwwards\n', speed)
    choice(1, 3)

    if option == 1:
        say('Wrong\n', speed)
        blue_key_puzzle()
    
    elif option == 2:
        say('Correct\n', speed)
        ply.room.items.append('blue key')
        ply.room.items.append('key')
        ply.room.puzzles = None

    elif option == 3:
        say('Wrong\n', speed)
        blue_key_puzzle()

def green_key_puzzle():
    say('In the chemistry set there are three liquids, one is coloured red, another is coloured blue, and the last is coloured yellow\n', speed)
    say('1.Mix red and blue\n2.Mix red and yellow\n3.Mix blue and yellow\n', speed)
    choice(1, 3)

    if option <=2:
        say('Wrong\n', speed)
        green_key_puzzle()
    
    elif option == 3:
        say('Correct\n', speed)
        ply.room.items.append('green key')
        ply.room.items.append('key')
        ply.room.puzzles = None

def item_take():                #checks what the item is
    say(f'Take?\n', speed)
    print('')
    say('1.Yes\n2.No\n', speed)
    choice(1, 2)
    item_num = 0
    
    if option <= 1:

        if ply.room.items[item_num] == 'key':
            ply.key += 1

        elif ply.room.items[item_num] == 'big key':
            ply.big_key += 1

        elif ply.room.items[item_num] == 'red key':
            ply.red_key += 1

        elif ply.room.items[item_num] == 'blue key':
            ply.blue_key += 1

        elif ply.room.items[item_num] == 'green key':
            ply.green_key += 1
        
        del ply.room.items[item_num]
        
    elif option >= 2:
        item_num += 1

#win

def win():
    say('''
         ______________________________________________________
________|    _     _             __    _     _    ___    __   |_______
\       |   / '   / \   |\  |   / __  |_\   /_\    |    /__   |      /
 \      |   \_.   \-/   |  \|   \__/  | \  /   \   |    __/   |     /
 /      |_____________________________________________________|     \ 
/__________)                                              (__________\ 
    ''', 0.005)
    say('''
`8.`8888.      ,8'  ,o888888o.     8 8888      88           `8.`888b                 ,8'  8 8888 b.             8 
 `8.`8888.    ,8'. 8888     `88.   8 8888      88            `8.`888b               ,8'   8 8888 888o.          8 
  `8.`8888.  ,8',8 8888       `8b  8 8888      88             `8.`888b             ,8'    8 8888 Y88888o.       8 
   `8.`8888.,8' 88 8888        `8b 8 8888      88              `8.`888b     .b    ,8'     8 8888 .`Y888888o.    8 
    `8.`88888'  88 8888         88 8 8888      88               `8.`888b    88b  ,8'      8 8888 8o. `Y888888o. 8 
     `8. 8888   88 8888         88 8 8888      88                `8.`888b .`888b,8'       8 8888 8`Y8o. `Y88888o8 
      `8 8888   88 8888        ,8P 8 8888      88                 `8.`888b8.`8888'        8 8888 8   `Y8o. `Y8888 
       8 8888   `8 8888       ,8P  ` 8888     ,8P                  `8.`888`8.`88'         8 8888 8      `Y8o. `Y8 
       8 8888    ` 8888     ,88'     8888   ,d8P                    `8.`8' `8,`'          8 8888 8         `Y8o.` 
       8 8888       `8888888P'        `Y88888P'                      `8.`   `8'           8 8888 8            `Yo 
    ''', 0.005)
    say('''
       _____________________
      |       .--,--.       |
      |  .   /|~~|~~|\   .  |
      | :+:  ||.-o-.||  :+: |
      |  |   |/.-'-.\|   |  |
      |--,---------------.  |
      |  |:y:o:u:|Win Win|  |
      |  | ' . ' |)_Win_(|  |
      |  | y:o:u |  )_(  |  |
      :--+---'---|-------+--;
       : :Win Win|:y:o:u:; ;
        \ \_( )_(| '   '/ /
         \ `. Win|you ,' /
          `. `._(| ',' ,'
           _`. `.|,' ,'     _ _ _/ _
  \/)()(/_)   `. | ,'    /)/ (- /_)
                `+'     /
            _   _  _  _  _
          _) ()//)//)(-_)
    \n''', 0.005)
    say('1.Play again\n2.Quit', speed)
    choice(1, 2)

    if option <= 1:
        ply = Player(None, 0, 0, 0, 0, 0)
        ply.enter('Back Room')
        
    
    elif option >= 2:
        exit()

class Player:       #where the player is what keys they have

    def __init__(self, room, key, big_key, red_key, blue_key, green_key):
        self.room = room
        self.key = key
        self.big_key = big_key
        self.red_key = red_key
        self.blue_key = blue_key
        self.green_key = green_key

    global option

    def describe(self):
        say(f'You enter The {self.room.name}.', speed)
        print('')
        self.room.list_furniture()  #lists furniture

        global option
        
        #checks what the puzzle is

        if self.room.puzzles == 'key_puzzle()':
            key_puzzle()

        elif self.room.puzzles == 'statue_puzzle()':
            statue_puzzle()

        elif self.room.puzzles == 'simon_says_puzzle()':
            simon_says_puzzle()

        elif self.room.puzzles == 'math_puzzle':
            math_puzzle()

        elif self.room.puzzles == 'red_key_puzzle()':
            red_key_puzzle()

        elif self.room.puzzles == 'blue_key_puzzle()':
            blue_key_puzzle()
        
        elif self.room.puzzles == 'green_key_puzzle()':
            green_key_puzzle()

        elif self.room.puzzles == 'win()':
            win()

        self.room.list_items() #lists items            
        self.room.list_doors() #lists doors

        for choice_num, door_name in enumerate(self.room.doors, start = 1):
            say(f'{choice_num}.{door_name.capitalize()}', speed)
            print('')

        global choice

        choice(1, choice_num)

        self.enter(self.room.adjacent[option - 1])      #if you choose the first door in the list you will go to the first adjacent room in the list

    def enter(self, adjacent):

        if type(adjacent) != Room:
            adjacent = Room.get_room(adjacent)

            if adjacent == None or type(adjacent) != Room:
                raise Exception

        #if a door is locked with any kind of key this will tell you and ask if you want to use one

        if adjacent.locked:
            time.sleep(1)
            say('The door is locked and requires a key.\n', speed)
            time.sleep(0.2)
            
            if self.key > 0:
                say('Use a key?\n1.Yes\n2.No\n', speed)
                time.sleep(0.2)
                choice(1, 2)

                if option <= 1:
                    self.key = self.key - 1
                    say('You use a key.\n', speed)
                    adjacent.locked = False       
            
                elif option >= 2:
                    ply.enter(ply.room)
        
            else:
                ply.enter(ply.room)

        if adjacent.locked_big:
            time.sleep(1)
            say('The door is locked and requires a big key.\n', speed)
            time.sleep(0.2)

            if self.big_key > 0:
                say('Use a big key?\n1.Yes\n2.No\n', speed)
                time.sleep(0.2)
                choice(1, 2)

                if option <= 1:
                    self.big_key = self.big_key - 1
                    say('You use a big key.\n', speed)
                    adjacent.locked_big = False

                elif option >= 2:
                    ply.enter(ply.room)
                
            else:
                ply.enter(ply.room)

        if adjacent.locked_red:
            time.sleep(1)
            say('The door is locked and requires a red key.\n', speed)
            time.sleep(0.2)

            if self.red_key > 0:
                say('Use a red key?\n1.Yes\n2.No\n', speed)
                time.sleep(0.2)
                choice(1, 2)

                if option <= 1:
                    self.red_key = self.red_key - 1
                    say('You use a red key.\n', speed)
                    adjacent.locked_red = False

                elif option >= 2:
                    ply.enter(ply.room)
                
            else:
                ply.enter(ply.room)

        if adjacent.locked_blue:
            time.sleep(1)
            say('The door is locked and requires a blue key.\n', speed)
            time.sleep(0.2)

            if self.blue_key > 0:
                say('Use a blue key?\n1.Yes\n2.No\n', speed)
                time.sleep(0.2)
                choice(1, 2)

                if option <= 1:
                    self.blue_key = self.blue_key - 1
                    say('You use a blue key.\n', speed)
                    adjacent.locked_blue = False

                elif option >= 2:
                    ply.enter(ply.room)
                
            else:
                ply.enter(ply.room)

        if adjacent.locked_green:
            time.sleep(1)
            say('The door is locked and requires a green key.\n', speed)
            time.sleep(0.2)

            if self.green_key > 0:
                say('Use a green key?\n1.Yes\n2.No\n', speed)
                time.sleep(0.2)
                choice(1, 2)

                if option <= 1:
                    self.green_key = self.green_key - 1
                    say('You use a green key.\n', speed)
                    adjacent.locked_green = False

                elif option >= 2:
                    ply.enter(ply.room)
                
            else:
                ply.enter(ply.room)

        else:
            self.room = adjacent
            self.describe()

class Room:     #what the room name is, what its adjacent to, its furniture, its items, its doors, whether it is locked
    def __init__(self, name, adjacent, furniture, puzzles, items, doors, locked, locked_big, locked_red, locked_blue, locked_green):
        self.name = name
        self.adjacent = adjacent
        self.items = items
        self.furniture = furniture
        self.puzzles = puzzles
        self.doors = doors
        self.locked = locked
        self.locked_big = locked_big
        self.locked_red = locked_red
        self.locked_blue = locked_blue
        self.locked_green = locked_green
        ROOMS[self.name] = self

    global option

    @staticmethod
    def get_room(rooms):
        return ROOMS.get(rooms, None)

    def list_furniture(self):       #list furniture

        if type(self.furniture) == list:
            
            for item in self.furniture:

                if item == self.furniture[0]:
                    
                    if item == self.furniture[-1]:
                        say(f'There {item}.', speed)
                        print('')

                    else:
                        say(f'There {item}, ', speed)
                        sys.stdout.flush()

                else:
                    if item == self.furniture[-1]:
                        say(f'and there {item}.', speed)
                        print('')
                    
                    else:
                        say(f'There {item}, ', speed)
                        sys.stdout.flush()                


        time.sleep(0.2)
    
    def list_items(self):       #list items and ask if you want to take them

        if type(self.items) == list:

            for item in self.items:

                if item == self.items[0]:
                    
                    if item == self.items[-1]:
                        say(f'There is a {item}.\n', speed)
                        print('')
                        item_take()

                    else:
                        say(f'There is a {item}, ', speed)
                        sys.stdout.flush()
                        item_take()

                else:
                    if item == self.items[-1]:
                        say(f'and a {item}.\n', speed)
                        print('')
                        item_take()
                    
                    else:
                        say(f'There is a {item}, ', speed)
                        sys.stdout.flush()                
                        item_take()

        time.sleep(0.2)

    def list_doors(self):       #list doors

        for item in self.doors:

            if item == self.doors[0]:
                
                if item == self.doors[-1]:
                    say(f'There is a {item}.', speed)
                    print('')

                else:
                    say(f'There is a {item}, ', speed)
                    sys.stdout.flush()

            else:
                if item == self.doors[-1]:
                    say(f'and a {item}.', speed)
                    print('')
                
                else:
                    say(f'There is a {item}, ', speed)
                    sys.stdout.flush()                

        time.sleep(0.2)

#the player

ply = Player(None, 0, 0, 0, 0, 0)

#the rooms

back_room = Room('Back Room', ['Closet', 'House'], None, None, None, ['door ahead', 'door to the left'], False, False, False, False, False)

closet = Room('Closet', ['Back Room'], ['are shelves'], None, ['key'], ['door behind'], False, False, False, False, False)

house = Room('House', ['Gun Range', 'Statues Room', 'Math Room', 'Simon Says Room', 'End', 'Back Room'], None, None, None, ['downstairs door to the left', 'downstairs door to the right', 'upstairs door to the left', 'upstairs door to the right', 'front door', 'door behind'], True, False, False, False, False)

gun_range = Room('Gun Range', ['House'], ['is a counter'], 'key_puzzle()', [], ['door behind'], False, False, False, False, False)

statues = Room('Statues Room', ['Red Room', 'House'], [], 'statue_puzzle()', [], ['door ahead', 'door behind'], True, False, False, False, False)

math = Room('Math Room', ['Blue Room', 'House'], [], 'math_puzzle()', [], ['door ahead', 'door behind'], True, False, False, False, False)

simon_says = Room('Simon Says Room', ['Green Room', 'House'], [], 'simon_says_puzzle()', [], ['door ahead', 'door behind'], True, False, False, False, False)

red_room = Room('Red Room', ['Statues Room'], ['is a jukebox'], 'red_key_puzzle()', [], ['door beind'], False, True, False, False, False)

blue_room = Room('Blue Room', ['Math Room'], ['are clocks'], 'blue_key_puzzle()', [], ['door beind'], False, True, False, False, False)

green_room = Room('Green Room', ['Simon Says Room'], ['is a chemistry set'], 'green_key_puzzle()', [], ['door beind'], False, True, False, False, False)

end = Room('End', [], [], 'win()', [], [], False, False, True, True, True)


while True:

    #a start screen

    print('1.Play\n2.Quit\n')

    choice(1, 2)                  # input 1 or 2

    if option <= 1:
        time.sleep(0.2)                 # text will not play immediately after input

        speed = float(input('Speed of text in seconds '))

        ply.enter(back_room)

    elif option >= 2:
        exit()    