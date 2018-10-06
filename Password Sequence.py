# - Password Sequence -
# The Goal of this was to create a some sort of base password
# funtion that'll grow into what I think would be a bassline
# for a website password gadget.
# This is my first code in Python, I copied it and modified it off of freeCodeCamp.org's
# Youtube Video. "Learn Python - Full Course for Beginners."
password = "XXX"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != password and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

print("You Lost Sucka")