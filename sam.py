# Copyright Chai Nunes. MIT Liscense.
from samfunc import SAM

isCommand = False

name = SAM.input('Hello, user. I am SAM - Simple Assistant Machine. What is your name?')
def EOI():
    print('\n<' + name + '>\n')
EOI()

commands = open('C:\\Python34\\Lib\\SAM\\commands.txt', 'r+')

commandList = [x.strip('\n') for x in commands.readlines()]

uinput = SAM.input('Welcome, ' + str(name) + ', type "help" for the list of commands.')

while 1:
    for i in range(len(commandList)):
        if uinput == commandList[i]:
            isCommand = True

    if isCommand:
        if str(uinput) == commandList[0]:
            SAM.help()
        elif str(uinput) == commandList[1]:
            SAM.info()
        elif str(uinput) == commandList[2]:
            phrase = SAM.input('What should I say?')
            SAM.say(str(phrase))
        elif str(uinput) == commandList[3]:
            path = SAM.input('What is the path of the file or folder I should open?')
            isFile = SAM.input('Am I opening a file or a folder?')
            bFile = False
            if isFile == 'yes':
                bFile = True
            SAM.open(str(path), bFile)
        elif str(uinput) == commandList[4]:
            path = SAM.input('What is the path of the file or folder I should delete?')
            SAM.delete(str(path))
        elif str(uinput) == commandList[5]:
            SAM.clear()
        uinput = ''
        EOI()
        isCommand = False
