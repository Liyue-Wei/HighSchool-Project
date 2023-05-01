import os 

def path():
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = file_path.replace("\\", "/")
    return (file_path)

def path_function():
    file_path = path()
    file_path = "".join(file_path)
    return(file_path)

path_function()