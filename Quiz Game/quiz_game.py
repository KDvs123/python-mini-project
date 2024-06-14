print("Welcome to my computer quiz!")

playing=input("Do you want to play? ")

if playing.lower() != "yes":
    quit() #immediatly terminate the program

print("Okay! Let's play! :) ")
score=0

answer= input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct! :D")
    score += 1
else:
    print("Sorry, that's incorrect. ")


answer= input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct! :D")
    score+=1
else:
    print("Sorry, that's incorrect. ")


answer= input("What does RAM stand for? ").lower()


if answer == "random access memory":
    print("Correct! :D")
    score+=1
else:
    print("Sorry, that's incorrect. ")


answer= input("What does PSU stand for? ").lower()

 
if answer == "power supply":
    print("Correct! :D")
    score+=1
else:
    print("Sorry, that's incorrect. ")


print("You got "+str(score)+" questions correct ")
print("You got "+str(score/4 * 100)+" %")
    

    
