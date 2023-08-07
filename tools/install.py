import os

modules = ["ttkbootstrap", "pyautogui", "selenium", "openpyxl", "opencv-python", "numpy", "markdown", "matplotlib", "pytube", "requests", "pillow", "pygame", "pandas", "opencv-contrib-python"]
for i in range(0, len(modules)):
    os.system("pip install "+modules[i])

try:
    os.system('nvidia-smi.exe')
    os.system("pip install "+"cupy-cuda12x")    #根据Cuda版本变更cupy安装版本

except:
    print("Cuda environment not avaliable")
    os.system('pause')