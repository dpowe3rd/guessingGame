import random  # Random Module
boo = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
# Above is a list of all possible inputs, no other inputs will work


def guess(number):  # Function that takes a random number as a parameter
    count = 1  # Sets count equal to 0, as we haven't attempted to guess yet
    while number < 21:  # This is essentially a while True loop because number will never be greater than 20
        spam = input()  # Asks the user to guess the number and input a number

        if spam not in boo:  # If the user input is not in the list boo, it will not be taken
            print('That is not an answer, please choose a number from 1 - 20.')
            continue

        if int(spam) > int(number):  # Compares user input to random number
            print('You guessed too high, Please try again.')  # The user input is higher than the random number
            count = count + 1  # Adds 1 to the count for our first attempt
            continue  # Restarts the loop

        if int(spam) < int(number):  # Compares user input to random number
            print('You guess too low, Please try again.')  # The user input is lower than the random number
            count = count + 1  # Adds 1 to the count for our first attempt
            continue  # Restarts the loop

        if int(spam) == int(number) and count == 1:
            # The line above compares user input to random number and if the number of times the loop was restarted
            print('You guessed my number correctly, in only ' + str(count) + ' time! Good job!')
            break  # Stops the loop

        if int(spam) == int(number) and count > 1:
            # The line above compares user input to random number and if the number of times the loop was restarted
            print('You guessed my number correctly, in only ' + str(count) + ' times! Good job!')
            break  # Stops the loop


r = random.randint(1, 20)  # Generates a number from 1 - 20

print('I am thinking of a number, 1-20 can you guess what it is?')  # Asks the user to play.
print(guess(r))  # Calls the function 'guess'