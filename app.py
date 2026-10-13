import msvcrt 
import os
import time
import random

def clear_keyboard_buffer(): 
    """Remove any pending keystrokes from the keyboard buffer.""" 
    while msvcrt.kbhit(): 
        msvcrt.getwch() 

def clear_screen():
    """Clears the screen"""
    os.system('cls' if os.name == 'nt' else 'clear')



def generate_string(level):
    """Generates, presents, and returns a random string based off of the level"""
    code = ""
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(level+4):
        code += letters[random.randint(0,25)]
    print(f"Level {level+1}\n\nCode: {code}\n\n")
    for i in range(5):
        print(".",end = "", flush = True)
        time.sleep(1)
    clear_screen()
    return code

def good_job():
    """Says 'Good Job' for 3 seconds"""
    clear_screen()
    print("Good Job\n\n")
    for i in range(3):
        print(".",end = "", flush = True)
        time.sleep(1)
    clear_screen()

def ask_play_again():
    """Asks user if they would like to replay, and returns 'y' or 'n'"""
    while True:
        choice = input("Enter 'y' to play again or 'n' to quit: ")
        if "yn".find(choice.strip().lower()) > -1: #checks if choice is (y or n) or not
            break
        print("Invalid")
    return choice.strip().lower()

def print_score(level, guess, code):
    """Prints the score of the user when they lose"""
    clear_screen()
    print(f"""Incorrect.

Correct String: {code}
Your Answer: {guess}

You made it through Level {level}.

""")
    if level <3:
        print("Wow, did you understand the game?")
    elif level <7:
        print("Not bad, keep working at it.")
    else:
        print("Nice Jo! You're a memory master!")

clear_screen()
level = 0
start = input("Type 'q' to quit, or other to play: ").strip().lower()
while not start == "q":
    clear_screen()
    code = generate_string(level)
    clear_keyboard_buffer()
    guess = input("Enter the code(case insensitive): ").strip().upper()
    if guess == code:
        level += 1
        good_job()
    else:
        print_score(level, guess, code)
        play_again = ask_play_again()
        if play_again == "n":
            break
        level = 0
print("Have a good day.")