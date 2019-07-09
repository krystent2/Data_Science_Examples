#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 08:44:47 2018

@author: krystent
"""

"""
In this game, a player will go through a fun house. Each room will
have surprises and the player will need to make prompted decisions
about what happens and the actions they take. The house can decide
to eject the player if the player is not having enough fun. The
object of the game is to get through all rooms of the house having
fun.
"""

import textwrap

import sys

import os

class Player:
    """This class defines the player and allows the player to do things such as
       choose which tool they will use, make decisions about whether they want to 
       keep playing the game, and respond when the Fun House asks them if they 
       are having fun."""
    
    def __init__(self):
        self.name = input('What is your name? ') 
    
    def choice(self):
        self.choice = input('Which letter do you choose? ')
        
    def __str__(self):
        return self.name
        return self.choice
    
    def __repr__(self):
        return self.name
        return self.choice    

    def player_fun(p):
        
        while True:
            p = str(input('Are you having fun? Enter "Y" for yes or "N" for no: '))
            fun = []
            fun.append(p)
            print()

            try:
                if p == 'N':
                    print('The Fun House has kicked you out because '
                         'you\'re not having fun. Bye.'
                         )
                    raise SystemExit

                elif p == 'Y':
                    print('Yay!')
                    break

            except Exception as other:
                continue
        

class Room():
    """This class is the main class for all the rooms in the Fun House. Individual 
       rooms are subclasses off this main class. The Room class initializes the room
       name, description of the room, and an image.""" 


    def __init__(self, name):
        self.name = name
        self.descrip = None
                 
    def display_image(self):
        if self.image_path is not None:
            display(Image(filename=self.image_path))
    
    def describe(self):
        if self.descrip is not None:
            print(self.descrip)
        
class Mirror(Room):
    """The Mirror Room class is a sub-class of Room class. The init function  
       instantiates the room and the self.descrip describes the room for the user.
       The results method prompts the user for a choice on which tool the player
       will use to escape the room."""


    def __init__(self, name):
        Room.__init__(self, name)
        self.descrip = (
	"""You are in the Mirror Room. The walls, ceiling, and
        floor are mirrors. You can see yourself hundreds of times.
        It\'s very confusing. One of the mirrors is a secret door.
        What tool will you use to find the secret door?"""
                       )

       
    def results(a):  
        a = input('Type the capital letter for the tool you will use: ')
        answer = []
        answer.append(a)    
        print()
        
        for x in answer:
            if x == 'C':
                print('You did it! Congratulations. You\'ve escaped the mirror room.')
            elif x == 'A':
                b = input('Silly string won\'t work. Try again. Enter a different letter: ')
                answer.append(b)
            elif x == 'B':
                c = input('A squirt gun won\'t work on mirrors. Try again. Choice: ')
                answer.append(c)
            elif x == 'D':
                print('The Fun House has kicked you out because you\'re not having fun. Bye!') 
                raise SystemExit
            else:
                a = input('You can only enter "A", "B", "C", or "D": ')
                answer.append(a)

    def __str__(self):
        return self.descrip
    
    def __repr__(self):
        return self.descrip        
                     
                  
class Trampoline(Room):
    """The Trampoline Room class is a sub-class of Room class. The init function
       instantiates the room and the self.descrip describes the room for the user. 
       The results method prompts the user for a choice on which tool the player 
       will use to escape the room."""    
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.descrip = (
        """You\'ve now entered the trampoline room. The floor
        and walls are trampolines. You can bounce off the
        walls and do flips in the air."""
                       )

    def results(a):  
        a = input('Type the capital letter for the tool you will use: ')
        answer = []
        answer.append(a)  
        print()
        
        for x in answer:
            if x == 'A':
                print('''You just escaped the Trampoline Room like spider man,\nexcept you used silly string instead of a web.'''
                     )
            elif x == 'B':
                b = input('Squirt guns won\'t work this time. '
                          'Choose a different letter: ')
                answer.append(b)
            elif x == 'C':
                c = input('Water balloons don\'t work on trampolines. '
                          'Enter a different letter: ')
                answer.append(c)
            elif x == 'D':
                print('The Fun House has kicked you out '
                      'because you\'re not having fun. Bye!') 
                raise SystemExit
            else:
                a = input('The letter must be "A", "B", "C", or "D": ')
                answer.append(a)

class Balloon(Room):
    """The Balloon Room class is a sub-class of Room class. The init function  
       instantiates the room and the self.descrip describes the room for the user.
       The results method prompts the user for a choice on which tool the player
       will use to escape the room."""
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.descrip = (
        """You\'re in the Balloon Room. The entire room is filled\nwith balloons. You are stuck in the middle of the room.\nHow will you escape?"""
                        )

    def results(a):  
        a = input('Type the capital letter for the tool you will use: ')
        answer = []
        answer.append(a)  
        print()
        print()   

        for x in answer:
            if x == 'B':
                print('You did it! Congratulations. You\'ve escaped the '
                      'Balloon Room.')
                print()
                print('And you\'ve escaped the Fun House. You are now '
                      'riding down a tornado slide to the exit. '
                      'We hope you had fun.'
                     )
            elif x == 'A':
                b = input('Silly string won\'t work. Choose a different letter: ')
                answer.append(b)
            elif x == 'C':
                c = input('Water balloons don\'t work on air filled balloons. Enter a different letter: ')
                answer.append(c)
            elif x == 'D':
                print('The Fun House has kicked you out because you\'re not having fun. Bye!') 
                raise SystemExit
            else:
                a = input('The letter must be "A", "B", "C", or "D": ')
                answer.append(a)
        
#Create an instance of each room to use when calling methods in sub-classes
r1 = Mirror('Mirror Room')
r2 = Balloon('Balloon Room')
r3 = Trampoline('Trampoline Room')


class Tools():
    '''This class creates the tools the player can choose from to escape each
       room while going through the Fun House. Only one tool will work in each 
       room.'''
    
    def __init__(self, name, letter, choice):
        self.name = name   #Room name
        self.action = None  
        self.letter = letter
        self.choice = choice
 
    
    def letr(self):
        if self.letter is not None:
            return self.letter
    
    def choices(self):
        if self.choice is not None:
            return self.choice
       
class SillyString(Tools):
    """Silly String is a sub-class of the Tool class. It is initialized by using 
       attributes assigned in the main class Tools. self.letter assigns a letter
       choice to the tool (for the player) and self.choice names the tool. Both
       are called when the program runs."""
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.letter = 'A'
        self.choice = 'Silly string'

    def __str__(self):
        return '{}: {}'.format(self.letter, self.choice)
    
    def __repr__(self):
        return '{}: {}'.format(self.letter, self.choice)

class SquirtGun(Tools):
    """Squirt gun is a sub-class of the Tool class. It is initialized by using 
       attributes assigned in the main class Tools. self.letter assigns a letter
       choice to the tool (for the player) and self.choice names the tool. Both
       are called when the program runs."""
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.letter = 'B'
        self.choice = 'Squirt gun'
 
    def __str__(self):
        return '{}: {}'.format(self.letter, self.choice)
    
    def __repr__(self):
        return '{}: {}'.format(self.letter, self.choice)

    
class WaterBalloons(Tools):
    """Water balloon is a sub-class of the Tool class. It is initialized by using 
       attributes assigned in the main class Tools. self.letter assigns a letter
       choice to the tool (for the player) and self.choice names the tool. Both
       are called when the program runs."""    
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.letter = 'C'
        self.choice = 'Water balloons'

    def __str__(self):
        return '{}: {}'.format(self.letter, self.choice)
    
    def __repr__(self):
        return '{}: {}'.format(self.letter, self.choice)

class NoFun(Tools):
    """The No Fun class is a sub-class of the Tool class. This option provides
       player with an 'out' if the player is not having fun and wants to exit
       the program early. No Fun is initialized by using attributes assigned in the main
       class Tools. self.letter assigns a letter choice to the tool (for the player) and
       self.choice names the tool. Both are called when the program runs."""    
    
    def __init__(self, name):
        Room.__init__(self, name)
        self.letter = 'D'
        self.choice = 'I\'m not having fun.'

    def __str__(self):
        return '{}: {}'.format(self.letter, self.choice)
    
    def __repr__(self):
        return '{}: {}'.format(self.letter, self.choice)

#Create instances for each tool
t1 = SillyString('Silly String')
t2 = SquirtGun('Squirt Gun')
t3 = WaterBalloons('Water Balloons')
t4 = NoFun('I\'m not having fun')

def begin(): 
    """This function defines a secret code to enter the Fun House. The function is
       called after the player sees an introduction to the game."""

    start = ('''You are standing in front of the Fun House. To get inside,
	     you must type a secret code. The code is one number between
             1 and 5.'''
            )
    print(textwrap.fill(start, width=70))
    print()
    code1 = '3'
    
    while True:
        player_code_choice = str(input('Enter one number between 1 and 5:  '))
        if player_code_choice == '3':
            print()
            print('Congratulations! You\'ve entered the fun house.')
            break
        elif player_code_choice != '3':
            print()
            print('Enter just one number between 1 and 5.')


#################### Start of Program  ##########################

game_active = True  #starts loop to allow player to re-play game at end

while game_active == True:
    
    print()
    intro = ('''Welcome to the Fun House game. The goal is to navigate through a 
            series of rooms that are full of surprises. You will be armed with
            tools such as water balloons, squirt guns, and silly string. Your
            job is to have FUN! If the Fun House thinks you are not having fun,
            the house may kick you out. If you are kicked out, you will have the
            chance to play again.'''
            )
    print(textwrap.fill(intro, width=70))
    print()
    p1 = Player()   #Asks player for their name; creates instance of player
    print()  # All print() lines serve purpose of adding empty line for cleaner UX
 
    print('Ready? Let\'s go...')
    print()
    p1            
    begin()

    #Player is now inside Fun House in Mirror Room

    print()
    r1.describe()   
    print()
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print()
    print(p1)
    r1.results()
    print()
    print()
    r3.describe()   
    print()
    #insert player fun question here
    p1.player_fun()
    print()
    print()        
    transition = (
    '''You have spent hours in the trampoline room.\nNow you want to leave. What tool will you use to escape the Trampoline Room?'''
                 )
    print(textwrap.fill(transition, width=70))            
    print()
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print()
    print(p1)
    r3.results()
    print()
    print()
    print('You have made it to the third and final room of the Fun House.')
    print()
    r2.describe()  #this should print description of balloon room        
    print()
    print(t1)
    print(t2)
    print(t3)
    print(t4)
    print()
    print(p1)
    r2.results()
    print()
    print()
    z = str(input('Would you like to keep playing? "Y" for yes, "N" for no:  '))
    zlist = []
    zlist.append(z)
    print()
    if z == 'N':
        print('Bye.')
        break
    elif z == 'Y':
        print('Awesome!')
    else:
        print('You need to type "Y" or "N": ')
        z = str(input('Type "Y" for yes or "N" for no: '))
        zlist.append(z)
    print()
    








































































































 
        
        
        









































































































 
        
        
        