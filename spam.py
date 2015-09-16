import os

commands = ["say", "open", "remove", "task"];
response = ""

name = input("Hello. I am SPAM - Simple Personal Assistant Machine. What is your name?\n")
print("Hello " + name + ", type \"help\" for a list of commands.")
print("\n<" + name + '>')

def run():
    response = input()
    # Say Command
    if response.lower()[:3] == commands[0]:
        if response.lower() == response.lower()[:3]:
            print("Say what?")
            response = input()
            print(response)
        else:
            print(response[4:])
    # Open Command
    if response.lower()[:4] == commands[1]:
        
        os.system(r"explorer " + response[5:])
    # Remove Command
    if response.lower()[:6] == commands[2]:
        os.remove(response[7:])
    # Task Command
    if response.lower()[:4] == commands[3]:
        os.system("taskmgr")
        os.wait()
        os.system("taskkill /f /im cmd.exe")
    print("\n<" + name + '>')

while 1:
    run()
