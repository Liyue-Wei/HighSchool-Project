from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://192.168.137.171:8080/shot.jpg")

while True:
    time.sleep(0.04)
    driver.refresh()