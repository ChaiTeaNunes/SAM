import os, webbrowser

info = "SAM is currently version 0.3 and is written by Chaiyawat Nunes\n\
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
browser/website: Opens web browser to given URL.\n\
close/exit: Exits SAM's console.\n\
create: creates a specific file or folder.\n\
google: Uses the Google Search Engine to look up the specific phrase.\n\
help: Displays the list of commands.\n\
kill: Kills the specified program.\n\
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
            response = input("Say what?\n")
            print(response)
        else:
            print(response[4:])
    # Open Command
    elif response.lower()[:4] == "open":
        if response.lower() == "open":
            reponse = input("Open what directory?\n")
            if response[(response.len - 1):response.len] == '/':
                os.system(r"explorer " + response)
            else:
                os.system(r"explorer " + response + '/')
        else:
            os.system(r"explorer " + response[5:])
            
    # Remove Command
    elif response.lower()[:6] == "remove":
        if response.lower() == "remove":
            response = ("Remove what file/directory?\n")
            os.remove(response)
        else:
            os.remove(response[7:])
    # Task Command
    elif response.lower()[:4] == "task":
        os.system("taskmgr")
    # Close/Exit command
    elif response.lower() == "close" or response.lower() == "exit":
        exit()
    # Programs command
    elif response.lower() == "programs":
        os.system("control appwiz.cpl")
    # Browser/Website
    elif response.lower()[:7] == "browser" or response.lower()[:7] == "website":
        if response.lower() == "browser" or response.lower() == "website":
            response = input("What site?\n")
            webbrowser.open_new_tab("https://" + response)
        else:
            webbrowser.open_new_tab("https://" + response[8:])
    # Google command
    elif response.lower()[:6] == "google":
        if response.lower() == "google":
            response = input("What should I search?\n")
            webbrowser.open_new_tab("https://www.google.com/search?q=" + response)
        else:
            webbrowser.open_new_tab("https://www.google.com/search?q=" + response[7:])
    # Kill command
    elif response.lower()[:4] == "kill":
        if response.lower() == "kill":
            response = input("Kill what program?\n")
            os.system("taskkill /f /im " + response)
        else:
            os.system("taskkill /f /im " + response[5:])
    # Create command
    elif response.lower()[:6] == "create":
        if response.lower() == "create":
            response = input("What directory is the folder/file in?\n")
            fof = input("File or Folder?\n")
            if fof.lower() == "folder":
                temp = input("What is the folder name?\n")
                os.makedirs(os.path.join(response, temp), 'wb')
                os.system(r"explorer " + response + '/')
                del temp
            elif fof.lower() == "file":
                temp = input("What is the file name?\n")
                open(os.path.join(response, temp), 'wb')
                del temp
            del fof
    # Command end
    print("\n<" + name + '>')

while 1:
    run()
