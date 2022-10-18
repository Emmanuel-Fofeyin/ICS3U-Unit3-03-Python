#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Oct 2022
# This program is a number guessing game using an else statement

import random

def main():

    # input
    random_number = random.randint(0,9)
    guessed_number = int(input("Guess a number from 0 - 9:"))

    # process and output
    if guessed_number == random_number:
        print("\nYou guessed right.")
    else:
         print("\nIncorrect, the number was {}.".format(random_number))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
