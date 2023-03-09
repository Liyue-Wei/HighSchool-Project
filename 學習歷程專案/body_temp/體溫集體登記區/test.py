import time

class ID_list:
    global ID 
    ID_input = ["E126233657", "E126108588", "E125478018", "E126136591", "E126136911", "E125489922", "E126318600", "E125738206", "E126101392", "S125461863", "E125723910", "E126251128", "E126251860"]
    count = len(ID_input)    
    for times in range (0, count):
        ID = ID_input[times]
        print(ID)
        print(times)
        time.sleep(0.2)