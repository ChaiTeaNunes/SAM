import os

info = "SPAM is currently version 0.1 and is written by Chaiyawat Nunes\n\
    (chaiteanunes@gmail.com, chaiteanunes.github.io).\n\
SPAM stands for Simple Personal Assistant Machine.\n\
SPAM is a machine, therefor has no gender or preference.\n\
SPAM is not even a neural network."
response = ""

name = input("Hello. I am SPAM - Simple Personal Assistant Machine. What is your name?\n")
print("Hello " + name + ", type \"help\" for a list of commands.")
print("\n<" + name + '>')

def run():
    response = input()
    # Help Command
    if response.lower() == "help":
        print("\
about/spam: Displays information about SPAM.\n\
close/exit: Clears SPAM's console.\n\
help: Display the list of commands.\n\
open: Opens a directory.\n\
remove: Removes a directory or file.\n\
say: SPAM says the specified phrase.\n\
task: Opens the task manager.")
    # About/Spam command
    if response.lower() == "spam" or response.lower() == "about":
        print(info)
    # Say Command
    if response.lower()[:3] == "say":
        if response.lower() == response.lower()[:3]:
            print("Say what?")
            response = input()
            print(response)
        else:
            print(response[4:])
    # Open Command
    if response.lower()[:4] == "open":
        if response.lower() == response.lower()[:4]:
            reponse = ("Open what directory?")
            os.system(r"explorer " + response)
        else:
            os.system(r"explorer " + response[5:])
    # Remove Command
    if response.lower()[:6] == "remove":
        if response.lower() == response.lower()[:6]:
            response = ("Remove what file/directory?")
            os.remove(response)
        else:
            os.remove(response[7:])
    # Task Command
    if response.lower()[:4] == "task":
        os.system("taskmgr")
        os.wait()
        os.system("taskkill /f /im cmd.exe")
    # Close/Exit command
    if response.lower() == "close" or response.lower() == "exit":
        exit()
    print("\n<" + name + '>')

while 1:
    run()
