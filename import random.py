import random
#random.randrange(5,11) = 11 not included but in randrange it is included

#will ask user how large number they wanna generate
top_of_range = input("Type a number: ")
#if user give u integer value we want to convert it into int by default it's a string

if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print('Please type a number larger than 0 next time')
        quit()
else:
    print('Please type a number next time')
    quit()
random_number =random.randint(0,top_of_range)

#let's take a number to guess
guesses=0
while True:
    guesses+=1
    user_guess=input("Make a guess")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print('Please type a number next time.')
        continue
    if user_guess==random_number:
        print('You got it!')#it will continue after completion as well so will use break
        break 
    else:
        #print('You got it wrong!') will give hint to user
        if user_guess>random_number:
            print("You were above the number")
        else:
            print("You were below the number")


#print("You got it in",guesses,"guesses")#how many guesses we require to find a number
#both are same
print("Congratulations!!!!!!!!!!!!!!!!!!!!")
print("You got it in"+ str(guesses) +"guesses")