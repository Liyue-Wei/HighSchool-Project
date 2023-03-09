import tkinter as tk
from selenium import webdriver
import random
import time

win = tk.Tk()
win.title("高雄中學體溫自動填報系統")

driver = webdriver.Chrome()
driver.get('https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx')

class rand_temp:
    global rand_1, rand_2
    rand_1 = random.randint(35, 36)
    rand_2 = random.randint(0, 9)

def program():   
    ID_in = ID.get()
    element_input = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]")
    element_input.send_keys(ID_in)
    element_button = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]")
    element_button.click()
    time.sleep(1)

    element_selector_1 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/span[2]/input[2]")
    element_selector_1.click()
    element_selector_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[1]")
    element_selector_2.send_keys(rand_1)
    element_selector_3 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[2]")
    element_selector_3.send_keys(rand_2)
    element_selector_4 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[3]")
    element_selector_4.send_keys("正常")
    element_button_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/input")
    element_button_2.click()
    time.sleep(1)

    driver.quit()
    request = ("填報完成")

class GUI_interface:
    global ID
    ID = tk.StringVar()
    label1 = tk.Label(win, text="高雄中學體溫自動填報系統", fg="black", font=("微軟正黑體", 20))
    label1.pack(padx=5, pady=5)
    label2 = tk.Label(win, text="填入身分證字號", fg="gray", font=("微軟正黑體", 18))
    label2.pack(padx=5, pady=5)
    input_ID = tk.Entry(win, font=("微軟正黑體", 20), bg="white", width="12", textvariable=ID)
    input_ID.pack(padx=5, pady=5)
    button = tk.Button(win, text="輸入", fg="white", bg="gray", font=("微軟正黑體", 15), command=program)
    button.pack(padx=5, pady=5)

    global request
    request = tk.StringVar()
    request_IO = tk.Label(win, fg="gray", font=("微軟正黑體", 18), textvariable=request)
    request_IO.pack(padx=5, pady=5)

win.mainloop()