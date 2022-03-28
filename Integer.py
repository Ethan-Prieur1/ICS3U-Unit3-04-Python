#!/usr/bin/env python3

# Created by Ethan Prieur
# Created on March 2022
# This is a program that calculates if a number is positive, negative or zero


def main():
    # This function is the main program

    # input
    Number = int(input("Enter a positive or negative number: "))

    # process & output
    if Number > 0:
        print("Your Number Was Positive :)")
    elif Number < 0:
        print("Your Number Was Negative :(")
    elif Number == 0:
        print("That's Zero! Wow Nice Job entering Zero!")
    else:
        print("I have no idea what this could be")
    print("\nDone.")


if __name__ == "__main__":
    main()
