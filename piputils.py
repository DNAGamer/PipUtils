import os
import sys

def getdir():
    paths = sys.path
    direct = paths[4]
    direct += "\scripts\pip3.5"
    return direct

def install(module, direct):
    command = direct + " install " + module
    os.system(command)

def remove(module, direct):
    command = direct + " uninstall " + module + " -y"
    os.system(command)
    
def update(direct):
    os.system(direct + " install --upgrade pip")
    os.system(direct + " freeze > requirements.txt")
    os.system(direct + " install -r requirements.txt --upgrade")
    try:
        os.remove("requirements.txt")
    except:
        print("I couldnt clean up after myself :(")

    
direct = getdir()
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
        update(direct)
        
    else:
        print("That isnt a known mode, try again")
    
