import random # import random module

#using randint (-5,11) 11 also generate 

top_of_range=input("Type a number: ")

if top_of_range.isdigit(): #isDigit() method makes sure that  the user enter a digit number 
                           #it returns true if it is a number
    top_of_range=int(top_of_range)

    if top_of_range <=0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()





random_number=(random.randint(0,top_of_range)) #generate numbers between -5 to 11(excluding 11)
guesses=0

while True:
    guesses+=1
    user_guess=input("Guess the number: ")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time. ")
        continue

    if(user_guess==random_number):
        print("You got it right")
        break
   
    elif(user_guess>random_number):
         print("You were above the number")
    else:
        print("You were below the number")
        


print("You got it in ",guesses," guesses")




