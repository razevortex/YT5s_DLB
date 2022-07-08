from multiprocessing import Process
import sys
from gui import *
from bot import *

if __name__ == '__main__':
    gui_process = Process(target=gui_proc)
    gui_process.start()
    bot_process = Process(target=walk_link_list)
    bot_process.start()

