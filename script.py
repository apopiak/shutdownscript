'''
Thanks to Jay for the initial version of the script!
'''

from datetime import datetime
from time import sleep
from os import system
import sys

def gui_input():
    try:
        import easygui as gui

        while True:
            msg = 'Enter when your system should shut down'
            Lines = ['month', 'day', 'hour', 'minute']
            userinput = gui.multenterbox(msg, "Alex little helper v1.3", Lines)
            for i, val in enumerate(userinput):
                if len(val) == 1:
                    userinput[i] = '0' + userinput[i]
            if gui.ynbox('Do you want me to shut down\non the %s.%s. around %s:%s?' % tuple(userinput)):
                return userinput
    except:
        return None

def terminal_input():
    userinput = []
    while len(userinput) < 4:
        if len(userinput) == 0:
            userinput.append(input('Enter the time of the desired shutdown:\n Month: '))
        elif len(userinput) == 1:
            userinput.append(input(' Day: '))
        elif len(userinput) == 2:
            userinput.append(input(' Hour: '))
        elif len(userinput) == 3:
            userinput.append(input(' Minute: '))
    return userinput

def wait_for_shutdown(userinput, polling_interval=200):
    int_input = [int(string) for string in userinput]
    shutdown_time = datetime(2015, *int_input)
    delta = (shutdown_time - datetime.now()).total_seconds()
    while delta > 0:
        print('System shutting down in ', delta, ' seconds')
        sleep(polling_interval)
        delta = (shutdown_time - datetime.now()).total_seconds()
    if sys.platform == 'linux2':
        system('shutdown -s') #  = 'shutdown now' in linux
    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        system('shutdown /s') #  = 'shutdown now' in windows
    exit()

userinput = gui_input()
if userinput is None:
    userinput = terminal_input()
wait_for_shutdown(userinput)
