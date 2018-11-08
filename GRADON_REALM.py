import random
import time

def displayIntro():
    print ('''You are in a land full of dragons. In front of you,
 you see two caves. In one cave, the dragon is friendly
 and will share his treasure with you. The other dragon
 is greedy and hungry, and will eat you on sight.''')
print()

def chooseCave():
     cave = ''
     while cave != '1' and cave != '2':
         print('Which cave will yougo intro? 1 or 2')
         cave = input()

     return cave

def checkCave(SelectNumber):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A lage dragon jamp out in front of you! He open his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = 1

    if SelectNumber == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Gobbles you down in one bite!') 

playAgain='yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)

    print('Do you want to play again? (yes or no)')
    playAgain=input()
