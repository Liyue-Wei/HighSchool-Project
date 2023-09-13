import os 

def path():
    file_path = os.path.abspath(os.path.dirname(__file__))
    file_path = file_path.replace("\\", "/")
    length = len(file_path)
    file_path_2 = []
    for i in range(0, length):          
        file_path_2.append(file_path[i])

    return (file_path_2)

def path_function(direct_path):
    file_path = path()
    file_path.append(direct_path)
    file_path = "".join(file_path)
    return(file_path)
