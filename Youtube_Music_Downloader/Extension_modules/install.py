import os

def program():  
    modules = ["pytube", "ttkbootstrap"]  
    for i in range(0, len(modules)):
        os.system("pip install "+modules[i])

os.system('pause')