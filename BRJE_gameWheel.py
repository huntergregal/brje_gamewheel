#!/usr/bin/env python3
import json
import random
from time import sleep
#__import__("IPython").embed()

'''
Itch.io "Bundle for Racial Justice and Equality" game selector
Author: Hunter Gregal
'''

def GetRandomGame():
    with open('games.json', 'r') as f:
        blob = f.read()
    games = json.loads(blob)['games']
    ngames = len(games)
    choice = random.randrange(0, ngames)
    return games[choice]

colors = ['Red', 'Green', 'Yellow', 'LightPurple', 'Purple', 'Cyan',
                'LightGray']
def Red(skk): return "\033[91m{}\033[00m" .format(skk) 
def Green(skk): return "\033[92m{}\033[00m" .format(skk)
def Yellow(skk): return "\033[93m{}\033[00m" .format(skk)
def LightPurple(skk): return "\033[94m{}\033[00m" .format(skk)
def Purple(skk): return "\033[95m{}\033[00m" .format(skk)
def Cyan(skk): return "\033[96m{}\033[00m" .format(skk)
def LightGray(skk): return "\033[97m{}\033[00m" .format(skk)

def Rainbow(word, space=False):
    cLetters = []
    if space:
        fmt = '{} '* len(word)
    else:
        fmt = '{}'* len(word)
    i = 0
    for c in word:
        cLetters.append(globals()[colors[i]](c))
        i += 1
        i %= len(colors)
    return fmt.format(*cLetters)
    
def PrettyPrintGame(game):
    for key, val in game.items():
        if key in ['id', 'cover_color']:
            continue
        print(f"\033[93m {key}\033[00m: {val}")

def Spin():
    for i in range(0, 3):
        color = colors[random.randrange(0, len(colors))]
        space = ' ' * random.randrange(0,10)
        sleep(1)
        print(globals()[color]("{}... SpInNinG ...\n".format(space)))
        sleep(1)

if __name__ == '__main__':
    print(Rainbow('-------------------------------'*2))
    print(Rainbow('~~~WELCOME TO THE GAME WHEEL~~~', True))
    print(Rainbow('-------------------------------'*2))
    print("Special thanks to itch.io and the {}".format(Rainbow('Bundle for Racial Justice and Equality')))
    Spin()
    game = GetRandomGame()
    PrettyPrintGame(game)
