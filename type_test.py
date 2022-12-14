# Type as fast as you can

import curses # Need to be install on windows --> pip install windows-curses
from curses import wrapper

import time

import random


def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test") # if no coordinati will be (0, 0, '') per default
    stdscr.addstr("\npress any key to start") # tyhe backlash n bring the curssor down
    stdscr.refresh()
    stdscr.getkey()

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target) # if no coordinati will be (0, 0, '') per default
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color) # this print the color you choses from the above on the scren

def load_text():
    with open("v1_test.txt", "r") as f: # "r" is for read mode / the with will make sure the file will be closed after the file was used / we store in f
        lines = f.readlines()
        return random.choice(lines).strip() # '.strip()' remove the invisible '\n' at the end of every line in the txt file

def wpm_test(stdscr):
    target_text = load_text()
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5) # this give character per minute and not words per minutes but the last division by 5 give us wpm

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text: # "-".join(current_text) --> "H-e-l-l-o"
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27: # the ord of a key is the representation of any key on the keyboard with a number (unicode or ascit)
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop() # the .pop option remove the last caracter from a list
        elif len(current_text) < len(target_text):
            current_text.append(key) # In Python, the append() method is used to add an item to the end of a list. In the code you provided, current_text is a list, and key is the item being added to the end of the list.


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

    while True:
        wpm_test(stdscr)
        stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)

# this need to be launch in a terminal like CMD,
# go to folder where python is located and enter cmd in the path link and type enter, will open CMD with the right directory then just type : python file_name.py
# inside cmd use 'cd ..' to go to previous directoru and 'cd name_of_the_folder_you_need_to_go_in'

# cd desktop\sam
# python type_test.py
'''
cd desktop\sam & python type_test.py
'''
