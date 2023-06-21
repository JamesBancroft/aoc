from func import below, above, ask, below_or_above

bounds = [0, 100]
guess = 50
tries = 0
response = 2

number = int(input("Please chose a number between 0 and 100 "))

# The last task to complete: check if the guess is equal to the chosen number 
while tries < 11 and response == 2:

    response = ask(guess)

    if response == 2:
        pinpoint = below_or_above(guess)
    
    if pinpoint == 1:
        guess = below(guess, bounds)

    elif pinpoint == 2:
        guess = above(guess, bounds)

    tries += 1 

if tries < 11:
    print("I guessed your number! I win. ")

else: 
    print("I was unable to guess your number, You win. ")
