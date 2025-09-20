import random

top_number_range = input("Type the number : "  )

if top_number_range.isdigit():
    top_number_range = int(top_number_range)
    if top_number_range <=0 :
        print("Enter a number greater than 0")
        quit()
else:
    print("Enter a number next time")
    quit()

random_number = random.randint(0, top_number_range)

guesses = 0 
while True:
    guesses += 1
    user_guess = input("Make a guess :" )
    if user_guess.isdigit():
         user_guess = int(user_guess)
       
    else:
        print("enter a number next time")
        continue
    if user_guess == random_number :
        print("you got it correct")
        break 
    if user_guess > random_number :
        print("you were above the number")
    else:
        print("you were below the number ")

print("you got in " , guesses , " guesses")
        