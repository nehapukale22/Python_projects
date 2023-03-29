#Password_manager
from http.client import NETWORK_AUTHENTICATION_REQUIRED


pwd=input("What is the master password")

def view():
    #pass#it does nothing just reduces our indentation error
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data=line.rstrip()
            #it splits by searching the pipe into list
            #like="hello|neha"        ["hello","neha"] we can access it by index and assign it names
            user,passw=data.split("|")
            #i want to split the username and password
            print("User:",user," , Password:",passw)

"""What does Lstrip and Rstrip do in Python?
rstrip(): returns a new string with trailing whitespace removed. 
It's easier to remember as removing white spaces from “right” side of the string.
 lstrip(): returns a new string with leading whitespace removed,
  or removing whitespaces from the “left” side of the string."""
   
def add():
    name=input('Account Name:')
    pwd=input("Password: ")
    #with open it automatically closes the file
    with open('passwords.txt','a') as f:
        f.write(name+"|"+pwd+"\n")
        
        


while True:
    mode=input("Would you like to add a new password or view existing ones(view,add),press q to quit?").lower()
    if mode=="q":
        break
    if mode=="view":
        view()
    elif mode=="add":
        add()
    else:
        print("Invalid mode")
        continue