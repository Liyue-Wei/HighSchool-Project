from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import openpyxl
import pyautogui

driver = webdriver.Chrome()
# url_login = ""
url_meet = "https://meet.google.com/"
url_classroom = "https://classroom.google.com/"

driver.get(url_meet)
pyautogui.hotkey('win', 'up')

# driver.find_element(By.XPATH, "/html/body/header/div[1]/div/div[3]/div[1]/div/span[1]/a").click()
# driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("eric20050107@gmail.com")
# pyautogui.hotkey('enter')

# driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div[1]/div[2]/div/div[2]/input").send_keys("xah-jnjo-wio")
# driver.find_element(By.XPATH, "/html/body/main/section[1]/div/div[1]/div[2]/div/div[2]/a/button/span").click()