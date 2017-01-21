import os
import sys

paths = sys.path
direct = paths[4]
direct += "\scripts\pip3.5"

def install(module, direct):
    command = direct + " install " + module
    os.system(command)

def remove(module, direct):
    command = direct + " uninstall " + module + " -y"
    os.system(command)

while True:
    mode = input("Install, update, or remove? ")
    mode = mode.lower()
    
    if mode == "install" or mode == "remove":
        module = input("Whats the module called? ")
        if mode == "install":
            install(module, direct)
            
        elif mode == "remove":
            remove(module, direct)
        else:
            print("something went wrong")
            
    elif mode == "update":
        os.system(direct + " install --upgrade pip")
        os.system(direct + " freeze > requirements.txt")
        os.system(direct + " install -r requirements.txt --upgrade")
        
    else:
        print("That isnt a known mode, try again")
    
