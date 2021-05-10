#!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on May 10, 2021
# Guess the number game with randomly generated numbers

import random


# Function that runs Guess the number game
def main():
    # User input
    print("Welcome to Guess the number!\nPick a number from 0-9")
    user_input = (input("Your number is: "))
    # Process
    program_number = random.randint(0, 9)
    try: 
        user_number = int(user_input)
        
        if user_number == program_number:
        # Output
            print("You have guessed the correct number, nice!")
        else:
            print("You have guessed incorrectly.")
            print("The correct answer was: {}".format(program_number))
    except Exception:
            print("{} is not an integer".format(user_input))
    finally:
            print("Finished succssfully")


if __name__ == "__main__":
    main()