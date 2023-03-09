from selenium import webdriver  #從selenium函式庫，引入網頁自動化操作驅動
import random   #引入random函式庫

driver = webdriver.Chrome() #調用Chrome驅動
driver.get('https://webap1.kshs.kh.edu.tw/kshsSSO/publicWebAP/bodyTemp/index.aspx') #前往"網址" //此網址為高雄中學體溫填報網站

class rand_temp:    #建立"rand_temp"類別 //用來亂數生成體溫數據
    global rand_1, rand_2   #將變數宣告為全域變數
    rand_1 = random.randint(35, 36) #變數"and_1"由"random"函式庫生成，範圍界在(35,36)之間
    rand_2 = random.randint(0, 9)   #變數"and_2"由"random"函式庫生成，範圍界在(0,9)之間

class Program:  #建立"Program"類別 //用來執行網頁自動化操作
    class part_1:   #建立"part_1"類別 //用來進入網站並填入身分證
        element_input = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[1]") #由xpath找到元件 //此為身分證填入區
        element_input.send_keys("****") #對元件輸入"****" //雙引號之間要填身分證
        element_button = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[1]/td/input[2]")    #由xpath找到元件 //此為確認框
        element_button.click()  #點擊元件

    class part_2:   #建立"part_2"類別 //用來操作體溫填報區
        element_selector_1 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/span[2]/input[2]")    ##由xpath找到元件 //此為
        element_selector_1.click()  #點擊元件
        element_selector_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[1]")   ##由xpath找到元件 //此為
        element_selector_2.send_keys(rand_1)    #對元件輸入"****" //雙引號間為體溫
        element_selector_3 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[2]")   ##由xpath找到元件 //此為
        element_selector_3.send_keys(rand_2)    #對元件輸入"****" //雙引號間為體溫(小數點)
        element_selector_4 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/select[3]")   ##由xpath找到元件 //此為
        element_selector_4.send_keys("正常")    #對元件輸入"正常" 
        element_button_2 = driver.find_element_by_xpath("/html/body/form/div[3]/table[2]/tbody/tr[2]/td/input") ##由xpath找到元件 //此為
        element_button_2.click()    #點擊元件
        
    class part_3:   #建立"part_3"類別 //完成操作後用來退出瀏覽器
        driver.quit()   #退出瀏覽器