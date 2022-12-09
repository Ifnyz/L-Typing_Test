# Type as fast as you can

import curses # Need to be install on windows --> pip install windows-curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test") # if no coordinati will be (0, 0, '') per default
    stdscr.addstr("\npress any key to start") # tyhe backlash n bring the curssor down
    stdscr.refresh()
    stdscr.getkey()


def main(stdscr): # Allow you to use CMD as a screen to writye stuff on it for the modul above

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) # this init the color 1 is the number on the 'list'
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    '''
    stdscr.clear() # As soon as i do anthing clear the screen
    stdscr.addstr("hello word", curses.color_pair(1)) # this is a reference to the color pair 1
    stdscr.addstr(2, 0, "welcome") # This give coordinate or where to print the texte on screen first is y then x (vertical then horizontal)
    stdscr.refresh() # As soon as i do anthing clear the screen
    key = stdscr.getkey()
    print(key)
    '''
    start_screen(stdscr) # i call the fonction inside the other fonction

wrapper(main)

# this need to be launch in a terminal like CMD,
# go to folder where python is located and enter cmd in the path link and type enter, will open CMD with the right directory then just type : python file_name.py
# inside cmd use 'cd ..' to go to previous directoru and 'cd name_of_the_folder_you_need_to_go_in'

# cd desktop\sam
# python type_test.py
