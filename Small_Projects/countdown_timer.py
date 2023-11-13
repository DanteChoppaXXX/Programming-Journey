#!./env/bin/python3
import time

# Prompt the user or the countdown duration
duration = int(input("How many minutes countdown?: "))



def main():
    # Convert minutes to seconds
    countdown_point = duration * 60
    # Begin the countdown
    while countdown_point > 0:
        # Reduce the value of countdown_point by 1 each passing second
        countdown_point -= 1
        # Delay for 1 second
        time.sleep(1)
        # Display the current value
        print(countdown_point, end='\r')
        if countdown_point == 0:
            print("COUNTDOWN COMPLETE!")

if __name__ == "__main__":
    main()