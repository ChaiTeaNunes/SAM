import os, webbrowser

info = "SAM is currently version 0.2 and is written by Chaiyawat Nunes\n\
    (chaiteanunes@gmail.com, chaiteanunes.github.io).\n\
SAM stands for Simple Assistant Machine.\n\
SAM is a machine, therefore has no gender or sexual preference.\n\
SAM is not even a neural network."
response = ""

name = input("Hello. I am SAM - Simple Assistant Machine. What is your name?\n")
print("Hello " + name + ", type \"help\" for a list of commands.")
print("\n<" + name + '>')

def run():
    response = input()
    # Help Command
    if response.lower() == "help":
        print("\
about/sam: Displays information about SAM.\n\
browser/web: Opens web browser to given URL.\n\
close/exit: Clears SAM's console.\n\
google: Using the Google Search Engine to look up the specific phrase.\n\
help: Display the list of commands.\n\
open: Opens a directory.\n\
programs: Opens programs and features.\n\
remove: Removes a directory or file.\n\
say: SAM says the specified phrase.\n\
task: Opens the task manager.")
    # About/Sam command
    if response.lower() == "sam" or response.lower() == "about":
        print(info)
    # Say Command
    elif response.lower()[:3] == "say":
        if response.lower() == "say":
            print("Say what?")
            response = input()
            print(response)
        else:
            print(response[4:])
    # Open Command
    elif response.lower()[:4] == "open":
        if response.lower() == "open":
            reponse = ("Open what directory?")
            os.system(r"explorer " + response)
        else:
            os.system(r"explorer " + response[5:])
    # Remove Command
    elif response.lower()[:6] == "remove":
        if response.lower() == "remove":
            response = ("Remove what file/directory?")
            os.remove(response)
        else:
            os.remove(response[7:])
    # Task Command
    elif response.lower()[:4] == "task":
        os.system("taskmgr")
        os.system("taskkill /f /im cmd.exe")
    # Close/Exit command
    elif response.lower() == "close" or response.lower() == "exit":
        exit()
    # Programs command
    elif response.lower() == "programs":
        os.system("appwiz.cpl")
        os.system("taskkill /f /im cmd.exe")
    elif response.lower()[:7] == "browser" or response.lower()[:3] == "web":
        if response.lower() == "browser":
            response = input("What site?")
            webbrowser.open_new_tab("https://" + response)
        else:
            webbrowser.open_new_tab("https://" + response[4:]
    elif response.lower()[:6] == "google":
        if response.lower() == "google":
            response = input("What should I search?")
            webbrowser.open_new_tab("https://www.google.com/search?q=" + response)
        else:
            webbrowser.open_new_tab("https://www.google.com/search?q=" + response[7:]
    print("\n<" + name + '>')

while 1:
    run()
