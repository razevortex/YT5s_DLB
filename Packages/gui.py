import PySimpleGUI as sg
import copy
from random import randint as rng
from os import listdir, rename, system, path, getcwd,  getppid, getpid
import time
import sys


class MainMenu(object):
    def __init__(self):
        self.MainWindowPos = (0, 0)
        self.MainWindow = self.window_builder()

    def window_builder(self):
        layout = [[sg.Text('Enter Link:'), sg.InputText(key='link', do_not_clear=False), sg.Button('Add', key='Add', bind_return_key=True)],
                  [sg.Combo(
                      values=['mp4/720', 'mp4/480', 'mp4/360', 'mp4/240', 'mp4/144', 'mp3/128'],
                      default_value='mp4/360', key='convert')],
                  [sg.Button('Close', key='Close')]]
        return sg.Window(
            'YT5 - Downloader', layout,
            location=self.MainWindowPos,
            grab_anywhere=True,
            no_titlebar=False)


def add_to_list(file_type, quality, link):
    string = f'{file_type},{quality},{link}\n'
    with open('A:\Raze VorteX\Workspace\YT5s_DLB\Packages\Links\links.txt', 'a') as linklist:
        linklist.write(string)


def gui_proc():
    gui = MainMenu()
    active = True
    while active:
        event, value = gui.MainWindow.read()
        if event == 'Close' or event == sg.WIN_CLOSED:
            gui.MainWindow.close()
            sys.exit()
        if event == 'Add':
            format = value['convert'].split('/')
            link = value['link']
            add_to_list(format[0], format[1], link)
