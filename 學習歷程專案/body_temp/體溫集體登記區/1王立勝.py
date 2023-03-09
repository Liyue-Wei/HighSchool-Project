from selenium import webdriver
import random
driver = webdriver.Chrome()
driver.get('https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx')

class rand_temp:

    global rand_1, rand_2
    rand_1 = random.randint(35, 36)
    rand_2 = random.randint(0, 9)

class Program:

    class part_1:

        element_input = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]")
        element_input.send_keys("E126233657")
        element_button = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]")
        element_button.click()

    class part_2:

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
        
    class part_3:

        driver.quit()

