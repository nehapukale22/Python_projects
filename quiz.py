#Quiz_game
print("Welcome to my Computer quiz")
# ask the do u wanna play my game
playing=input("Do you want to play? ")
print(playing)
#if yes in capital letters then quiz not start so will use .lower()
if playing.lower()!="yes":
    quit()
print("Okay! Let's play :)")
score=0

answer=input("What does CPU stand for? ").lower()
if answer=="central processing unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input("what is GPU stands for? ")
if answer.lower()=="graphics processing unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input("What does RAM stands for? ").lower()
if answer=="random access memory":
    print('Correct!')
    score+=1
else:
    print('Incorrect')

answer=input("what does PSU stands for? ").lower()
if answer=="power supply unit":
    print('Correct!')
    score+=1
else:
    print('Incorrect')

print("You got"+str(score)+"questions correct1")
#u can't add int to string therefore we are converting score to string
print("You got"+str((score/4)*100)+"%")





