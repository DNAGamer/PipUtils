import os
import sys

def installPip():
    import requests
    print("Downloading pip...")
    requests.get("https://bootstrap.pypa.io/get-pip.py")
    os.system("cls")
    print("Running installer...")
    paths = sys.path
    if os.system("{}\python3.5 get-pip.py") != 0:
        print("Error")
        exit()
    print("Adding pip to environment variables...")
    paths = sys.path
    direct = paths[4]
    direct += "\scripts"
    if os.system('setx PATH "%PATH%;{}\Scripts'.format(direct)) != 0:
        print("Error adding")
        exit()
    print("Completed installation...")
    print("Cleaning up ^-^")
    os.unlink("get-pip.py")
    print("Terminating instance")
    exit()

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
    mode = str(input("1. Install a module\n2. Remove a module\n3. Update modules\n4. Install pip properly"))
    mode = mode.lower()
    
    if mode == "1" or mode == "2":
        module = input("Whats the module called? ")
        if mode == "1":
            install(module, direct)
        elif mode == "2":
            remove(module, direct)
        else:
            print("something went wrong")
    elif mode == "3":
        update(direct)
    elif mode == "4":
        installPip()
    else:
        print("That isnt a known mode, try again")
    
