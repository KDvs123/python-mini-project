# asking for the master password
master_pwd=input("What is the master password? ")


# added a function- executable reusable block of code

def view():
     #pass keywords literary does nothing .but keep that to avoid indentation errors
          # while the actuall code
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():# take the file , read all the lines and get all the lines
            print(line.rstrip())
            # rstrip()  strip of the carraige return from our line

            # figure out the user from the password
            data = line.rstrip()
            user,passw=data.split("|") # split does it it looks for the character and split items based on that character
            # split example




def add():
    name = input("Accout Name: ")
    pwd= input("Password: ")

    with open('passwords.txt','a') as f: # using with will close the file once the operations are done
        f.write(name+" | "+pwd+"\n") # character break at the end of the line

    # 'w' -write create a new file or override if the file already exist
    # 'a' - append to the file
    # 'r' - read the file
    # 'r+' - read and write to the file
    # 'w+' - write and read to the file


        

#using while loop to add or view new password
while True:
    mode= input("Would you like to add a new password or view existing one (view,add), press q to quit: ?").lower()
    if mode == "q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()

    else:
        print("Invalid mode. Please try again")
        continue

