###RPG GAME (HARD--WAY)
from sys import exit
def gold_room():
    print('This room is full of gold , How much you take.?')
    choice=input('> ')
    if 0 in choice or 1 in choice:
        how_much=int(choice)
    else:
        dead('man , learn to type of number.')
    if how_much<50:
        print('nice, you are not greedy, you won')
        exit(0)
    else:
        dead('your greedy bad.')
def bear_room():
    print('there is a bear here')
    print('the bear has a bunch of honey')
    print('the fat bear is in from  of another door')
    print('how are you going to move the bear ?')
    bear_moved=False
    while True:
        choice=input('> ')
        if choice=='take honey':
            dead('the bear look at you then slaps your face off.')
        elif choice=='taunt bear' and not bear_moved:
            print('bear has moved from the door.')
            print('you can go trough it now.')
            print('you can go through the door')
            bear_moved=True
        elif choice=='taunt bear' and bear_moved:
            dead('the bear gets pissed off and chew your  legs off')
        elif choice=='open door':
            gold_room()
def dark_room():
    print('here you see the great evil dark')
    print('he,it,whatever stares at you and you can go insane')
    print('do you flee for your life or eat your head?')
    choice=input('> ')
    if 'flee' in choice:
        start()
    elif 'head' in choice:
        dead('well that was tasty')
    else :
        dark_room()
def start():
    print('You are in dark room.')
    print('there is a door to your right and left')
    print('whice one you take?')
    choice=input('> ')
    if choice=='left':
        bear_room()
    elif choice=='right':
        dark_room()
    else :
        dead('you stamble around the room untile you strave')
def dead(msg):
    print(msg+'thank you..')
start()
