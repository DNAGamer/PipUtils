import os
import sys
import urllib.request
import time

def installPip():
    download = True
    try:
        print("Downloading pip...")
        urllib.request.urlretrieve("https://bootstrap.pypa.io/get-pip.py", "get-pip.py")
        os.system("cls")
        print("Running installer...")
        paths = sys.path
        if os.system("python get-pip.py") != 0:
            print("Error using python, attempting to repair fault")
            if os.system('setx PATH "%PATH%;{}'.format(direct)) != 0:
                print("Unable to mount python to environment variables\nRecomended action: Reinstall python")
                exit()
            else:
                print("Added python to environment variables. Re-running commands")
                os.system("cls")
                print("Running installer...")
                paths = sys.path
                if os.system("python get-pip.py") != 0:
                    print("Error... Terminating")
                    exit()

    except:
        download = False
    os.system("cls")
    print("Adding pip to environment variables...")
    paths = sys.path
    direct = paths[4]
    direct += "\scripts"
    if os.system('setx PATH "%PATH%;{}\Scripts'.format(direct)) != 0:
        print("Error performing OS command, terminating")
        exit()
    os.system("cls")
    print("Completed installation...")
    time.sleep(2)
    os.system("cls")
    print("Cleaning up ^-^")
    if download:
        os.unlink("get-pip.py")
    print("Completed task...")
    time.sleep(2)
    return

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
    os.system("cls")
    mode = str(input("1. Install a module\n2. Remove a module\n3. Update modules\n4. Install pip properly\n"))
    mode = mode.lower()
    os.system("cls")

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
    time.sleep(1)
    
