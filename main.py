import random

print("Welcome to Guess a number program")
name = input("What is your name? ")
print("Your name is " + name )
number = random.randint(1, 10)
number_of_guesses = 0

while(True):
    guess = int(input("Make a guess? "))

    if(guess != number):
        print("The number is not correct!")
        number_of_guesses += 1
    else:
        print("The number is correct!")
        number_of_guesses += 1
        break
    
print("The number was " + str(number))
print("The number of guesses was: " + str(number_of_guesses))