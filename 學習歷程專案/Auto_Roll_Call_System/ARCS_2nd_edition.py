import pygame as pg
import time
import openpyxl
import pyautogui
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

running = True
resolution = (WIDTH, HEIGHT) = pyautogui.size()
# resolution = pyautogui.size()
# WIDTH = resolution[0]/1
# HEIGHT = resolution[1]/1

global FPS, white
FPS = 60
white = (255, 255, 255)

pg.init()
pg.display.set_caption("ARCS_2nd_edition")
window = pg.display.set_mode(resolution)
clock = pg.time.Clock()

while running == True:
    clock.tick(FPS)
        
    for event in pg.event.get():
        key_pressed = pg.key.get_pressed()

        if key_pressed[pg.K_ESCAPE]:
            running = False

        if event.type == pg.QUIT:
            running = False

    window.fill(white)
    pg.display.update()

pg.quit

# def path():
#     file_path = os.path.abspath(os.path.dirname(__file__))
#     length = len(file_path)
#     file_path_2 = []
#     for i in range(0, length):       
#         if file_path[i] == "\\":
#             file_path_2.append("/")
# 
#         else :
#             file_path_2.append(file_path[i])
# 
#     return (file_path_2)
# 
# def path_function(direct_path):
#     file_path = path()
#     file_path.append(direct_path)
#     file_path = "".join(file_path)
#     return(file_path)
# 
# def Chromedriver(direct_path):
#     direct_path = ("/chromedriver_win32")
#     file_path = path_function(direct_path)
#     print(file_path)
# 
# print(Chromedriver)

# os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
# opt = Options()
# opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
# driver = webdriver.Chrome(options=opt)
