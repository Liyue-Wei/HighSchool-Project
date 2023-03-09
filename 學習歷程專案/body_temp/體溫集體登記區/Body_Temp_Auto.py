from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import pyautogui
import time
import email.message
import smtplib

msg = email.message.EmailMessage()
driver = webdriver.Chrome()

global ID, url, ID_list, times, count, error_list
url = "https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx"
ID_list = ["E126233657", "E126108588", "E125478018", "E126136591", "E126136911", "E125489922", "E126318600", "E125738206", "E126101392", "S125815012", "S125461863", "E125723910", "X120638072", "E126251128", "E126032678", "E126136500", "E126227613", "E126251860"]
email = ["danielwqq@gmail.com", "brianwang72@gmail.com", "hang65989@gmail.com", "zack40091647@gmail.com", "chenray2005221@gmail.com", "wiwi805008@gmail.com", "durant931126@gmail.com", "a0911880586@gmail.com", "eric20050107@gmail.com", "JJason940519@gmail.com", "gan940724@gmail.com", "hongjieliu473@gmail.com", "yyenryan20041229@gmail.com", "moujinwei97@gmail.com", "happyyen8077616@gmail.com", "larry940106@gmail.com", "kevin159264@gmail.com", "bob931010@gmail.com"]
error_list = []
count = len(ID_list)  
print(count)

def email_send(times):
    msg["Subject"] = "體溫填報完成"
    msg["To"] = email[times]    
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content("體溫 "+ str(rand_1)+ "."+ str(rand_2)+ "°C 已於 "+ msg_time+ " 完成填報")
    server_service(msg)

def email_ERROR_send(times):
    msg["Subject"] = "體溫填報失敗"
    msg["To"] = email[times]    
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content("體溫填報錯誤，請洽詢管理員 "+msg_time)
    server_service(msg)
  
def error_list_send():
    error_list_str = " ".join(map(str, error_list))
    print(error_list_str)    
    msg["Subject"] = "體溫填報失敗"
    msg["To"] = "kshs090400@gmail.com"
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content(msg_time+"錯誤列表: "+error_list_str)
    server_service(msg)

def server_service(msg):
    msg["From"] = "eric20050107@gmail.com"
    server = smtplib.SMTP_SSL("smtp.gmail.com", "465")
    server.login("eric20050107@gmail.com", "esvrdvprpxrexvif")
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
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]").send_keys(ID)
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]").click()
       
            class part_2:
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[2]/td/span[2]/input[2]").click()
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[1]").send_keys(rand_1)
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[2]").send_keys(rand_2)
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[3]").send_keys("正常")
                driver.find_element(By.XPATH, "/html/body/form/div[3]/table[2]/tbody/tr[2]/td/input").click()
            
            class part_3:
                email_send(times)
                msg.clear()
                pyautogui.hotkey("enter")
                time.sleep(0.5)
                pyautogui.hotkey("ctrl", "t")        
                driver.switch_to.window(driver.window_handles[times+1])
        
        except:
            print(times, "Error")
            error_list.append(times)
            switch_screen()
            email_ERROR_send(times)
            msg.clear()

if(len(error_list))!=0:
    error_list_send()
    
driver.quit()