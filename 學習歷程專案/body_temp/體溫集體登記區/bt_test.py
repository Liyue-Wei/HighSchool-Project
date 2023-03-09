from selenium import webdriver
import random
import pyautogui
import time
import email.message
import smtplib

msg = email.message.EmailMessage()
driver = webdriver.Chrome()

global ID, url, ID_list, times, count, error_list
url = "https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx"
ID_list = []
error_list = []
count = len(ID_list)  
print(count)

def email_send(times):
    msg["From"] = "cwc-auto@mail.ru"
    # msg["Subject"] = "Автоматически заполнять температуру тела"
    msg["Subject"] = "體溫填報完成"
    msg["To"] = email[times]
    
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content("體溫 "+ str(rand_1)+ "."+ str(rand_2)+ "°C 已於 "+ msg_time+ " 完成填報")
    
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login("eric20050107@gmail.com", "DEWsso44")
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
    server.send_message(msg)
    server.close()

def email_ERROR_send(times):
    msg["From"] = "cwc-auto@mail.ru"
    msg["Subject"] = "體溫填報失敗"
    msg["To"] = email[times]
    
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content("體溫填報錯誤，請洽詢管理員 "+msg_time)
    
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login("gmail", "password")
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
    server.send_message(msg)
    server.close()
  
def error_list_send():
    error_list_str = " ".join(map(str, error_list))
    print(error_list_str)
    
    msg["From"] = "cwc-auto@mail.ru"
    msg["Subject"] = "Error List"
    msg["To"] = "kshs090400@gmail.com"

    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content(msg_time+"錯誤列表: "+error_list_str)
    
    # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server.login("gmail", "password")
    server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
    server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
    server.send_message(msg)
    server.close() 

def switch_screen():
    pyautogui.hotkey("ctrl", "t")        
    driver.switch_to.window(driver.window_handles[times+1])

for times in range (0, count):
    ID = ID_list[times]
    
    class rand_temp:
        driver.get(url)
        global rand_1, rand_2
        rand_1 = random.randint(35, 36)
        rand_2 = random.randint(0, 9)

    class Program:
        try:
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
                email_send(times)
                msg.clear()
            
            class part_4:
                print(times)
                pyautogui.hotkey("enter")
                time.sleep(1)
                switch_screen()
        
        except:
            print(times, "Error")
            error_list.append(times)
            switch_screen()
            email_ERROR_send(times)
            msg.clear()

if(len(error_list))!=0:
    error_list_send()
    
driver.quit()

# if(len(error_list))!=0:
#     error_list_str = " ".join(map(str, error_list))
#     print(error_list_str)
#     
#     msg["From"] = "cwc-auto@mail.ru"
#     msg["Subject"] = "Error List"
#     msg["To"] = "kshs090400@gmail.com"
#     msg.set_content(error_list_str)
#     
#     # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     # server.login("gmail", "password")
#     server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
#     server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
#     server.send_message(msg)
#     server.close() 
#    
# driver.quit()

# from selenium import webdriver
# import random
# import pyautogui
# import time
# import email.message
# import smtplib
# 
# msg = email.message.EmailMessage()
# driver = webdriver.Chrome()
# 
# global ID, url, ID_list, times, count
# url = "https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx"
# ID_list = ["E125489922", "E126318600", "E125738206", "E126101392", "S125815012", "S125461863", "E125723910", "X120638072", "E126251128", "E126251860", "E126032678", "E126136500"]
# email = ["wiwi805008@gmail.com", "durant931126@gmail.com", "a0911880586@gmail.com", "eric20050107@gmail.com", "JJason940519@gmail.com", "gan940724@gmail.com", "hongjieliu473@gmail.com", "yyenryan20041229@gmail.com", "moujinwei97@gmail.com", "bob931010@gmail.com", "happyyen8077616@gmail.com", "larry940106@gmail.com"]
# count = len(ID_list)  
# print(count)
# 
# def email_send(times):
#     msg["From"] = "cwc-auto@mail.ru"
#     # msg["Subject"] = "體溫填報完成"
#     msg["Subject"] = "體溫填報作業完成"
#     msg["To"] = email[times]
#     
#     msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
#     msg.set_content("體溫 "+ str(rand_1)+ "."+ str(rand_2)+ "°C 已於 "+ msg_time+ " 完成填報")
#     
#     # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     # server.login("gmail", "password")
#     server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
#     server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
#     server.send_message(msg)
#     server.close()
# 
# def email_ERROR_send(times):
#     msg["From"] = "cwc-auto@mail.ru"
#     msg["Subject"] = "體溫填報失敗"
#     msg["To"] = email[times]
#     
#     msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
#     msg.set_content("體溫填報錯誤，請洽詢管理員 "+msg_time)
#     
#     # server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
#     # server.login("gmail", "password")
#     server = smtplib.SMTP_SSL("smtp.mail.ru", 465)
#     server.login("cwc-auto@mail.ru", "G29fUtcjVWaDmsrpfNHP")
#     server.send_message(msg)
#     server.close()
#     
# for times in range (0, count):
#     ID = ID_list[times]
#     
#     class rand_temp:
#         driver.get(url)
#         global rand_1, rand_2
#         rand_1 = random.randint(35, 36)
#         rand_2 = random.randint(0, 9)
# 
#     class Program:
#         class stage_1:
#             global programming 
#             
#             class part_1:
#                 element_input = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]").send_keys(ID)
#                 element_button = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]").click()
#             
#             try:
#                 element_selector_1 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/span[2]/input[2]").click()
#                 programming = True
# 
#             except:
#                 programming = False
#        
#         class stage_2:
#             if programming == True:
#                 class part_2:
#                     element_selector_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[1]").send_keys(rand_1)
#                     element_selector_3 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[2]").send_keys(rand_2)
#                     element_selector_4 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[3]").send_keys("正常")
#                     element_button_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/input").click()
# 
#                 class part_3:
#                     email_send(times)
#                     msg.clear()
# 
#                 class part_4:
#                     print(times)
#                     pyautogui.hotkey("enter")
#                     time.sleep(1)
#                     pyautogui.hotkey("ctrl", "t")        
#                     driver.switch_to.window(driver.window_handles[times+1])
# 
#             elif programming == False:
#                 print(times+" ERROR")
#                 email_ERROR_send(times)
#                 pyautogui.hotkey("enter")
#                 time.sleep(1)
#                 pyautogui.hotkey("ctrl", "t")        
#                 driver.switch_to.window(driver.window_handles[times+1])
#    
# driver.quit()