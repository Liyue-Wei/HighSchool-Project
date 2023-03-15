import os

modules = ["markdown"]

for i in range(0, len(modules)):
    os.system("pip install "+modules[i])