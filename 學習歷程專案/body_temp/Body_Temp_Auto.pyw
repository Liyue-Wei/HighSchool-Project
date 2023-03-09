from selenium import webdriver
import random
import pyautogui

driver = webdriver.Chrome()

# class unencrtpt:
#     class variable:
#         global chr_bsc_M,  ascii_list_int, switch_num, delta_num
#         chr_bsc_M = 77
#         int_bsc_4 = 52
#         delta_num = 57
#     
#     class input_list:    
#         global unformatted_list, formatted_list, ascii_list, count, ID_input
#         ascii_list = []
#         formatted_list = []
#         unformatted_list = []
#         unformatted_list = input()
#         count = len(unformatted_list)
#     
#         for num in range(0, count, 1):
#             formatted_list.append(unformatted_list[num])
#     
#         for num in range(0, count, 1):
#             ascii_list.append(ord(formatted_list[num]))
#     
#     class unencrypt:
#         for num in range(0, count, 1):
#             ascii_list_int = int(ascii_list[num])
#     
#             if(90>=ascii_list_int and 64<=ascii_list_int):
#                 switch_num = chr_bsc_M+(1*(chr_bsc_M-ascii_list_int))
#                 if(switch_num == 64):
#                     switch_num = "Z"
#                 ascii_list[num] = chr(switch_num)
#                 
#             if(114>=ascii_list_int and 105<=ascii_list_int):
#                 ascii_list[num] = chr(ascii_list_int-delta_num)
#     
#         ID_input = []
#         ID_input = "".join(ascii_list)
#         
#         print(ID_input)

class ID_list:
    global ID, url, ID_input, times, count
    url = "https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx"
    ID_input = ["E126233657", "E126108588", "E125478018", "E126136591", "E126136911", "E125489922", "E126318600", "E125738206", "E126101392", "S125461863", "E125723910", "E126251128", "E126251860", "X120638072", "E126032678"]
    count = len(ID_input)    
    print(count)
    
    for times in range (0, count):
        ID = ID_input[times]
        
        class rand_temp:
            driver.get(url)
            global rand_1, rand_2
            rand_1 = random.randint(35, 36)
            rand_2 = random.randint(0, 9)

        class Program:
            class part_1:
                element_input = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]").send_keys(ID)
                element_button = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]").click()

            class part_2:
                element_selector_1 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/span[2]/input[2]").click()
                element_selector_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[1]").send_keys(rand_1)
                element_selector_3 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[2]").send_keys(rand_2)
                element_selector_4 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[3]").send_keys("正常")
                element_button_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/input").click()
            
            class part_3:
                print(times)
                pyautogui.hotkey("enter")
                pyautogui.hotkey("ctrl", "t")        
                driver.switch_to.window(driver.window_handles[times+1])
       
    driver.quit()