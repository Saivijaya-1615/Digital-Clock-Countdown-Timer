import time
import sys

def digital_clock():
    """Displays a digital clock for a specified duration."""
    n = int(input("Enter the duration (in seconds) for the digital clock to run: "))
    i = 0  # Initialize the counter
    print("Digital Clock started!")
    while i < n:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        sys.stdout.write("\rDigital Clock: " + current_time)
        sys.stdout.flush()
        time.sleep(1)
        i += 1
    print("\nDigital Clock stopped!")

def countdown_timer(seconds):
    """Counts down from a given number of seconds."""
    print("Countdown Timer started!")
    while seconds > 0:
        sys.stdout.write("\rTime remaining: " + str(seconds) + " seconds")
        sys.stdout.flush()
        time.sleep(1)
        seconds -= 1
    print("\nTime's up!")

# Main program loop
while True:
    print("\nChoose an option:")
    print("0: Exit")
    print("1: Digital Clock")
    print("2: Countdown Timer")
    choice = input("Enter your choice: ")
    
    if choice == '0':
        print("Exiting the program. Goodbye!")
        break
    elif choice == "1":
        digital_clock()
    elif choice == "2":
        try:
            seconds = int(input("Enter the number of seconds to countdown: "))
            if seconds < 0:
                print("Please enter a non-negative number!")
            else:
                countdown_timer(seconds)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    else:
        print("Invalid choice! Please select a valid option.")
