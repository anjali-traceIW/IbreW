import curses
import curses.ascii
import os
import re
import sys
import time

from curses import wrapper

# TODO import logo (convert to cursed)
from state import State as state
from menuHandler import MenuHandler as menuHandler
from menuOptions import MenuOptions as menuOptions
from ui import UI as UI

def initializeScreen():
    screen = curses.initscr()
    return screen

def deinitializeScreen():
    curses.endwin()

def exitApp(screen):
    UI.clearScreen(screen)
    state.saveObjects(screen)
    curses.nocbreak()
    screen.keypad(False)
    curses.echo()
    deinitializeScreen()
    exit()

def main(screen):
    curses.curs_set(False)
    state.loadObjects(screen)
    currentChoice = 0
    while currentChoice != -1:
        currentChoice = menuHandler.handleMainMenu(
            screen,
            menuOptions.getMainMenuOptions(),
            currentChoice,
            state.getPeople(),
            state.getDrinks())
    exitApp(screen)

screen = initializeScreen()

if __name__ == "__main__":
    wrapper(main)
else:
    state.loadObjects(screen)

