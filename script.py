#!/usr/bin/python

'''
If you don't want to install easygui, quote line 11 and unquote lines 14 and 24.
You will have to enter your  desired shutdown time in line 23 (if you want to
shutdown on the 4th, 3:07pm line 23 has to be: "userinput = ['04','15','07']")
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

def wait_for_shutdown(userinput, polling_interval=200):
    int_input = [int(string) for string in userinput]
    shutdown_time = datetime(2015, *int_input)
    while (datetime.now() - shutdown_time).total_seconds() > 0:
        sleep(polling_interval)
    if sys.platform == 'linux2':
        system('shutdown -s') #  = 'shutdown now' in linux
    elif sys.platform == 'win32' or sys.platform == 'cygwin':
        system('shutdown /s') #  = 'shutdown now' in windows
    exit()

userinput = gui_input()
if userinput is None:
    userinput = tuple(['08', '14', '22', '20'])
wait_for_shutdown(userinput)
