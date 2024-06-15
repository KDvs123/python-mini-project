user_name=input("Type your name: ")
print(f"Welcome {user_name} to this adventure ")

answer=input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go? ")

if answer.lower()=="left":
    answer=input("You come to a river, you can walk around it or swim acros Type walk to walk around or swim to swim accrss: ")
    if answer=="swim":
        print("You swim accrosee were eaten by an alligator")
    elif answer=="walk":
        print("You walked for many miles, ran out of water and you lost the game")
    else:
        print("Not a valid option You Lose")

elif answer.lower()=="right":
    answer=input("You come to a bridge.it looks wobbly , do you want to cross it or head back (cross /back)")
    if answer=="back":
        print("You go back and lose ")
    elif answer=="cross":
        answer=input("You cross the bridge and meet a stranger.Do you talk to them(yes/no)? ")
        if answer=="yes":
            print("You talk to the stanger and they give you gold.You WIN!")
        elif answer=="no":
            print("You ignore the stranger and they ar offended and you LOSE! ")
        else:
            print("Not a valid option You Lose")

    else:
        print("Not a valid option You Lose")


else:
    print("Invalid input. You lose")

print("Thank you for playing")