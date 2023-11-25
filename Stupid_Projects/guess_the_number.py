#!./env/bin/python3
""" Write a program that generates a random number and asks the user to guess it. Provide hints like "too high" or "too low" until the user guesses correctly."""
import random
import time
# Generate a random number.
number = random.randint(1, 10)

# Ask the user to guess the number.
print("A random number has been generated, the range is between 1 to 10")





# Compare the user's prediction to the generated number.

def main():
    correct = number
    keep_going = True
    tries = 0

    while keep_going:
        tries = tries + 1

        guess = int(input("Guess what the number is?: "))
        print("Comparing Your Prediction To The Random Number")
        time.sleep(1)
        if guess > correct:
            print('Too High!... Try Again.\n')
            
        elif guess < correct:
            print('Too Low!... Try Again.\n')
            
        elif guess == correct:
            print("Correct!!!... Great Job!\n")
            keep_going = False
        
        if tries >= 3 and guess != correct:
            print("Better Luck Next Time!")
            keep_going = False

if __name__ == "__main__":
    main()