# Matthew hall
# December 11, 2024
# game
import random
import time

def display_intro():
    print("You're on a planet full of dragons. Two caves appear before you.")
    time.sleep(2)
    print("One dragons friendly, sharing its treasure.")
    time.sleep(2)
    print("The other's hungry, ready to devour you!")
    time.sleep(2)

def choose_cave():
    while True:
        try:
            cave = int(input("Which cave will you enter (1, 2, or 3)?: "))
            if 1 <= cave <= 3:
                return cave
            else:
                print("Invalid choice. Please enter 1, 2, or 3!")
        except ValueError:
            print("Invalid input. Please enter a number!")

def check_cave(cave_number):
    print("You approach the cave...")
    time.sleep(2)
    print("Darkness and shadows surround you...")
    time.sleep(2)
    print("A colossal shadow looms over you...")
    time.sleep(3)
    print("A fearsome dragon emerges! Its jaws open wide...")
    time.sleep(4)

    if cave_number == random.randint(1, 3):
        print("The dragon smiles, offering you its treasure!")
    else:
        print("The dragon lunges, devouring you in one gulp!")

while True:
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input("Dou you dare to play again? (yes/no): ").lower()
    if play_again not in ['yes', 'y']:
        break