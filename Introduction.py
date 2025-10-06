# This program is an introductory program for this repository

name = input("Hello! What is your name? ")
#print("Your name is:", name)

#collaboration JC for assignment 405/505
# Make sure the user typed something
if name.strip() == "":
    print("You didn't enter a name.")
else:
    print("Nice to meet you,", name + "!")
