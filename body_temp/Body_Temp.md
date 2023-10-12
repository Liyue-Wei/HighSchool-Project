# 高雄中學體溫自動填報系統說明
###### tags: `Python` `Selenium` `BodyTemp`
## 系統要求
本系統由Python編寫而成，因為需要配合一些特殊的功能使用，所以建議在Windows系統環境下使用，以達到最初設計之功能最大化；當然，如果使用者在Mac OS或是Linux也有辦法將(特定)原功能復現的話，也是可以正常使用的。

因為該系統需使用到**Selenium**及**ChromeDriver**，而ChomeDriver僅支援Windows、Mac OS及Linux，所以儘管Python可以在很多系統上執行，但該系統只能(在功能可能受限的情況下)於上述三個作業系統執行。

更多關於系統環境配置的資訊，請參考[Python環境配置](https://hackmd.io/@K3S12-Python-Studio/PDE)

## 模組
本系統需要使用到以下模組

1. **Selenium**   
    **~需要下載對應版本webdriver~**
3. **PyAutoGUI**
5. **time**
6. **smtplib**及**email.message**
7. **random**

## 功能
此程式的設計用途為「定時自動填報體溫」，並且具有多人同時填報的功能、填報失敗提醒功能以及亂數填報溫度功能。

## 程式碼
請參見[Body Temp System by Liyue-Wei](https://github.com/Liyue-Wei/HighSchool-Project/blob/main/body_temp/bt_final_edition.py)。

## 程式原碼片段說明 
def email_send：定義信件內容及發送信件  
def email_ERROR_send：填報錯誤時，給使用者的郵件及發送功能  
def error_list_send：填報錯誤時，給管理員的郵件及發送功能  
def switch_screen：切換螢幕  
class rand_temp：產生亂數體溫數據  
class Program：基本操作功能

## 設定定時執行
需要使用到Windows功能 "工作排程器"
1. 按下 <img src="https://cdn.iconscout.com/icon/free/png-256/windows-221-1175066.png" width="25px" alt="win button">，輸入"工作排程器"

    ![](https://i.imgur.com/fnSQ0Bz.jpg)
    
2. 選擇"建立基本工具" --> 命名 --> 設定時間 --> 選擇"開啟程式" --> 完成

    ![](https://i.imgur.com/q1y0mA0.png)



## 使用說明
1. 安裝ChromeDriver
2. 更改變數：
    - [ ] 身分證字號  
    **~格式請用~** **~["身分證字號1",~** **~"身分證字號2"]~** **~以此類推~**
    - [ ] 主機email帳號
    - [ ] 使用者email帳號
    - [ ] 主機email帳號
    - [ ] 密碼
    - [ ] SMTP伺服器  
    **~SMTP伺服器推薦使用"smtp.gmail.com"~**
    - [ ] TCP埠  
    **~gmail的TCP埠為"465"~**
3. 設定定時執行
---
### Authored by [**Liyue-Wei**](https://github.com/Liyue-Wei) on GitHub