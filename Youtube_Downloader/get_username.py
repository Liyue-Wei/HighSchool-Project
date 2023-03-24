import os 

def username():
    dir_path = os.path.dirname(__file__)
    path_list = dir_path.split("\\")
    return(path_list[2])