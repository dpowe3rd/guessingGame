import random  # Random Module


def guess(number):  # Function that takes a random number as a parameter
    count = 1  # Sets count equal to 0, as we haven't attempted to guess yet
    while number < 21:  # This is essentially a while True loop because number will never be greater than 20
        spam = int(input())  # Asks the user to guess the number and input a number

        if spam < 1 or spam > 20:
            print('That is not an answer, please choose a number from 1 - 20.')
            continue

        elif int(spam) > int(number):  # Compares user input to random number
            print('You guessed too high, Please try again.')  # The user input is higher than the random number
            count = count + 1  # Adds 1 to the count for our first attempt
            continue  # Restarts the loop

        elif int(spam) < int(number):  # Compares user input to random number
            print('You guess too low, Please try again.')  # The user input is lower than the random number
            count = count + 1  # Adds 1 to the count for our first attempt
            continue  # Restarts the loop

        elif int(spam) == int(number) and count == 1:
            # The line above compares user input to random number and if the number of times the loop was restarted
            print('You guessed my number correctly, in only ' + str(count) + ' try! Good job!')
            break  # Stops the loop

        elif int(spam) == int(number) and count > 1:
            # The line above compares user input to random number and if the number of times the loop was restarted
            print('You guessed my number correctly, in only ' + str(count) + ' tries! Good job!')
            break  # Stops the loop


r = random.randint(1, 20)  # Generates a number from 1 - 20

print('I am thinking of a number, 1-20 can you guess what it is?')  # Asks the user to play.
print(guess(r))  # Calls the function 'guess'
