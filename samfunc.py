# Copyright Chai Nunes. MIT Liscense.
import webbrowser, os, platform, stat

class SAM:
    opsys = platform.system().lower()
    inp = ''

    def input(phrase=''):
        SAM.say(phrase)
        SAM.inp = input()
        return SAM.inp

    def help():
        helpFile = open('help.txt', 'r+').read()
        SAM.say(helpFile)

    def info():
        infoFile = open('info.txt', 'r+').read()
        SAM.say(infoFile)

    def say(phrase=''):
        print(phrase)
        if SAM.opsys == 'darwin':
            os.system('say ' + phrase)

    def open(path='', isFile=False):
        if os.access(path, os.F_OK) and os.access(path, os.R_OK):
            if SAM.opsys == 'darwin':
                os.system('open ' + path)
                SAM.say('I successfully opened ' + path)
            elif SAM.opsys == 'windows':
                if isFile:
                    os.system('start ' + path)
                else:
                    os.system(r'explorer ' + path)
                SAM.say('I successfully opened ' + path)
            else:
                SAM.say('I\'m sorry, your operating system is not compatable with this command.')
        else:
            SAM.say('I\'m sorry, the specified path does not exist or I do not have the permissions to read this file or open this folder.')

    def create(path='', name='', isFile=False):
        if os.access(path, os.F_OK) and os.access(path, os.W_OK):
            if isFile:
                open(os.path.join(path, name), 'a+')
                SAM.open(os.path.join(path, name))
            else:
                os.makedirs(os.path.join(path, name))
                SAM.open(os.path.join(path, name))
        else:
            SAM.say('I\'m sorry, the specified path does not exist or I do not have the permissions to create this file or folder.')            

    def delete(path=''):
        if os.access(path, os.F_OK):
            success = True
            try:
                os.remove(path)
            except IOError as e:
                success = False
                pass
            if success:
                SAM.say('I successfully removed ' + path)
            else:
                SAM.say('I do not have the permissions to delete this file or folder.')
        else:
            SAM.say('I\'m sorry, the specified path does not exist')

    def clear():
        if SAM.opsys == 'windows':
            os.system('cls')
        elif SAM.opsys == 'darwin':
            os.system('clear')
