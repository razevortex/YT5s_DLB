import copy
from random import randint as rng
from selenium.webdriver import Edge
from selenium.webdriver.edge.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from os import listdir, rename, remove, path, getcwd, getppid, getpid
import time
import sys


class YT5(object):
    def __init__(self):

        self.driver = webdriver.Edge('A:\Raze VorteX\Workspace\YT5s_DLB\Packages\webdriver\msedgedriver.exe')
        self.download_path = r'C:/Users/Raze Vortex/Downloads'
        self.yt5_url = f'https://yt5s.com/en101/youtube-to-*/'
        self.quality = ''
        self.downloading_link = ''
        self.still_downloading = False

    def load_link(self, line):
        url = copy.copy(self.yt5_url)
        url = url.replace('*', line[0])
        url += '?q=' + line[2]
        self.downloading_link = line[2]
        self.quality = line[1]
        print(url)
        self.driver.get(url)

    def pick_res(self):
        el = self.driver.find_element(By.ID, 'formatSelect')
        for option in el.find_elements(By.TAG_NAME, 'option'):
            if self.quality in option.text:
                option.click()  # select() in earlier versions of webdriver
                return True

    def click_continue(self):
        el = self.driver.find_element(By.ID, 'btn-action')
        el.click()

    def download_element(self):
        el = self.driver.find_element(By.ID, 'asuccess')
        self.driver.get(el.get_attribute('href'))

    def check_download_folder(self, post=False):
        wait = True
        time.sleep(3)
        while wait:
            file_loading = [f for f in listdir(self.download_path) if 'yt5s.com-' in f or 'yt5s.com - ' in f]
            print(file_loading)
            if file_loading == []:
                wait = False
            else:
                for file_name in file_loading:
                    if '.crdownload' in file_name:
                        print(f"{file_name.replace('.crdownload', '')} is still loading")
                    else:
                        new_name = file_name.replace('yt5s.com-', '')
                        new_name = new_name.replace('yt5s.com - ' , '')
                        files = [file for file in listdir(f'{self.download_path}/') if new_name in file]
                        print(files)
                        if len(files) <= 1:
                            rename(f'{self.download_path}/{file_name}', f'{self.download_path}/{new_name}')
                            print(f'{self.download_path}/{new_name}' + ' downloaded and renamed')
                            if post is not True:
                                remove_link(self.downloading_link)
                        else:
                            remove(f'{self.download_path}/{file_name}')
                            if post is not True:
                                remove_link(self.downloading_link)
                            print('file already existed')
            time.sleep(5)


def next_line():
    with open('A:\Raze VorteX\Workspace\YT5s_DLB\Packages\Links\links.txt', 'r') as linklist:
        for line in linklist.readlines():
            line = line.strip()
            return line.split(',')


def remove_link(link):
    t_arr = []
    with open('A:\Raze VorteX\Workspace\YT5s_DLB\Packages\Links\links.txt', 'r') as linklist:
        for line in linklist.readlines():
            if link not in line:
                t_arr.append(line)
    with open('A:\Raze VorteX\Workspace\YT5s_DLB\Packages\Links\links.txt', 'w') as linklist:
        linklist.writelines(t_arr)


def walk_link_list():
    yt_loader = YT5()
    yt_loader.check_download_folder()
    while True:
        if not next_line():
            time.sleep(10)
        else:
            yt_loader.load_link(next_line())
            time.sleep(2)
            yt_loader.pick_res()
            time.sleep(0.2)
            yt_loader.click_continue()
            time.sleep(1.5)
            yt_loader.download_element()
            time.sleep(2)
            yt_loader.check_download_folder()

'''if __name__ == '__main__':
    walk_link_list()'''