import os
modules = ["ttkbootstrap", "pyautogui", "selenium", "openpyxl", "opencv-python", "numpy", "markdown", "matplotlib", "pytube", "requests", "pillow", "pygame", "pandas", "sympy", "openai", "tensorflow"]
for i in range(0, len(modules)):
    os.system("pip install "+modules[i])