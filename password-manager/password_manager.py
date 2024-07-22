# asking for the master password
pwd=input("What is the master password? ")


# added a function- executable reusable block of code

def view():
    pass #pass keywords literary does nothing .but keep that to avoid indentation errors
          # while the actuall code implements

def add():
    pass

#using while loop to add or view new password
while True:
    mode= input("Would you like to add a new password or view existing one (view,add), press q to quit?").lower()
    if mode == "q":
        break
    if mode=="view":
        pass
    elif mode=="add":
        pass

    else:
        print("Invalid mode. Please try again")
        continue

