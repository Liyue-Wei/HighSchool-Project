import os

modules = ["ttkbootstrap", "pyautogui", "selenium", "openpyxl"]

for i in range(0, len(modules)):
    os.system("pip install "+modules[i])