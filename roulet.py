#!/usr/bin/env python3
# Created by Dylan Mutabazi
# Date : April 2025
# in this program you play a game of russian roulette

import random
import constant


def main():

    # Initial greeting
    print(
        "Hello mate. in this game we play a very popular game called russian roulette."
    )
    print(
        "but first you must decode this phrase 'OB' into an integer, you have 3 guess. Good luck and have fun"
    )

    # Sets number of tries for passcode to 3
    lives = 3

    # Passcode loop
    while True:
        print("")
        user_passcode = input("What is the passcode: ")

        # Tries to convert user_input into int
        try:
            user_passcode_int = int(user_passcode)

            if user_passcode_int == constant.PASSCODE:
                print("good job, now you can start playing russian roulette")
                # Creates a variable chambers with a list/arrays of zeros and ones. 0 represent empty chambers, 1 represent bullet
                chambers = [0, 1, 0, 0, 0, 0]

                # Shuffles the arrays
                random.shuffle(chambers)

                # loops 6 times
                for i in range(6):
                    print("")
                    print(input("Press enter to fire "))

                    # If the array in chamber was 1 then your dead
                    if chambers[i] == 1:
                        print("")
                        print("BANG !!! ... you died")
                        break

                    # Else it must be 0 
                    else:
                        print("")
                        print("good job you survived.")
                        print("")
                        again = input("Do you wanna go again (y/n)?")

                        # If they go again then it loops backs to shooting
                        if (
                            again == "y"
                            or again == "Y"
                            or again == "Yes"
                            or again == "YES"
                            or again == "yes"
                        ):
                            print("")
                        
                        # If the answer is no then it stops the for loop 
                        elif (
                            again == "n"
                            or again == "N"
                            or again == "No"
                            or again == "NO"
                            or again == "no"
                        ):
                            print("")
                            print("Sad to see you go. By BY")
                            break

                        # Any other input shall be seen as saying no and break the loop 
                        else:
                            print("")
                            print("I'm going to guess thats a no so see ya")
                            break
                
                # Makes sure to break the loop in both for and while loop 
                break

            # If the passcode is not 152 then it removes 1 from lives until its0 
            elif user_passcode_int != constant.PASSCODE:
                lives = lives - 1
                print(
                    f"{user_passcode_int} is not the right code. you have {lives} chances left."
                )

                # Once it reaches 0 then it stops the loop
                if lives <= 0:
                    print("")
                    print("Your guesses are done")
                    break

        # Catches the exceptions/ error while trying to convert to int 
        except ValueError:
            print(f"{user_passcode} is not an integer")
            break


if __name__ == "__main__":
    main()
