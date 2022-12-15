
import curses 
from curses import wrapper

import time

import random


def start_screen(stdscr=None):
    stdscr.clear()
    stdscr.addstr("Welcome to speed typing test")
    stdscr.addstr("\nSelect a level: press 1 for easy, 2 for medieum and 3 for hard")
    stdscr.refresh()
    key = stdscr.getkey()
        # If the user pressed 1, 2, or 3, set the filename to the appropriate file
    if key == "1":
        filename = "easy_text.txt"
    elif key == "2":
        filename = "medium_text.txt"
    elif key == "3":
        filename = "hard_text.txt"
    else:
        # If the user pressed any other key, set the filename to the default file
        filename = "easy_text.txt"
    return filename

def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

def load_text(stdscr):
    filename = start_screen(stdscr)
    with open(filename, "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()

def wpm_test(stdscr):
    target_text = load_text(stdscr)
    current_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)

    stdscr.addstr(2, 0, "You completed the text! Press any key to continue...")
    key = stdscr.getkey()


def view_results(stdscr):
    # Clear the screen and display a message
    stdscr.clear()
    stdscr.addstr("Your previous test results:")

    # Load the user's previous results from a file (or database, etc.)
    # and display them on the screen
    with open("results.txt", "r") as f:
        results = f.readlines()
        for result in results:
            stdscr.addstr(result)

    # Wait for the user to press a key before returning to the main menu
    stdscr.addstr("\n\nPress any key to return to the main menu...")
    key = stdscr.getkey()




def main(stdscr): 

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK) 
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    while True:
    # Display a main menu with options for the user to choose from
        stdscr.clear()
        stdscr.addstr("Welcome to the typing speed test", curses.color_pair(1))
        stdscr.addstr("\n\n1. Start a new test")
        stdscr.addstr("\n2. View previous results")
        stdscr.addstr("\n3. Quit")
        stdscr.refresh()

    # Wait for the user to press a key and act on their selection
        key = stdscr.getkey()

        if key == "1":
            wpm_test(stdscr)

        elif key == "2":
            view_results(stdscr)

        elif key == "3":
            break

wrapper(main)

