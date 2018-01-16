#!/usr/bin/env python 3
#specifying which version of python i'm using

import random

#will generate random number
number = random.randint(1, 10)
tries = 1

#Asks user to enter username
uname = input("Hello, What is your username?")

# prints Hello + chosen username
print ("Hello", uname + ".", )

#Asks user question choosing yes will go to next question
question = input ("Would you like to play a game? [Y/N]" )
if question == "n":
    print("oh..okay")

#Conditions based on user guessing a value that will be higher or lower than the correct value until correct answer is chosen
if question == "y":
    print ("I'm thinking of a number between 1 & 10")
    guess = int(input("Have a guess: "))

if guess > number:
       print("Guess lower...")
if guess < number:
    print("Guess higher...")

while guess != number:  #guess is not equal to != the number
    tries += 1   #will give user 1 more try
    guess = int(input("Try again:"))
    if guess < number:
        print ("Guess higher")

if guess == number: #guess is equal to the number prints statement!
   print("You're right! you win! The number was", number,\
         "and it only took", tries, "tries!")

