import os

def download():
    dir_path = os.path.dirname(__file__)
    path_list = dir_path.split("\\")
    del path_list[3:len(path_list)]
    path_list.append("Downloads")
    path_list = "/".join(path_list)
    return(path_list)