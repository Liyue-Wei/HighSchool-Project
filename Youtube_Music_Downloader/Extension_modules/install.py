import os

def program():  
    modules = ["pytube", "ttkbootstrap"]  
    for i in range(0, len(modules)):
        os.system("pip install "+modules[i])

def program_2():  
    modules = ["pywin32"]  
    for i in range(0, len(modules)):
        os.system("pip install "+modules[i])
