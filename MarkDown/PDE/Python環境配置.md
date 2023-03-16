# Python環境配置

###### tags: `Python` 

## 開始前的Python知識
Python是一種 "[**直譯式**](https://zh.m.wikipedia.org/zh-tw/%E7%9B%B4%E8%AD%AF%E8%AA%9E%E8%A8%80)"、"[**高級程式語言**](https://zh.m.wikipedia.org/zh-tw/%E9%AB%98%E7%BA%A7%E8%AF%AD%E8%A8%80)"，在1991年，由工程師[吉多·范羅蘇姆](https://gvanrossum.github.io/)所開發，現由[Python軟體基金會](https://www.python.org/psf/)管理。

由於其程式語法的易讀性及編程快速的優點，現多被用於資料科學以及人工智慧的程式開發，也是很多程式初學者的優先選擇。

更多詳細資訊，請參考[Python Docs - Beginner's Guide to Python](https://wiki.python.org/moin/BeginnersGuide)。

## 系統選擇
Python可以在[Windows](https://www.microsoft.com/zh-tw/windows)、[Mac OS](https://www.apple.com/tw/macos/monterey/)或者[Linux](https://www.linux.org/)等多個平台上執行及編譯。
### Mac OS
Mac OS上有很多的Python編譯器可以選擇，像是[Visual Studio Cdoe](https://code.visualstudio.com/)、[Spyder](https://www.spyder-ide.org/)等，但是建議初學者，使用像是[<font color="#12AD2B">Anaconda</font>](https://www.anaconda.com/products/distribution)或[Xcode](https://developer.apple.com/xcode/)這類的整合式開發環境(IDE)會比較方便。

更多詳細資訊，請參考[Python Docs - 在 Mac 系統使用 Python](https://docs.python.org/zh-tw/3/using/mac.html)。
**~註：Mac~ ~OS其實有是原生內建Pyhton的，只是版本可能比較舊，建議如果要使用Mac~ ~OS來寫Python程式的話，在開始的配置還是去官網下載一下for~  ~mac的安裝檔更新會比較好~**

### Windows
Windows上的Python就相對開放許多(至少就很多奇怪的插件都不會被阻擋)，在這個方面而言，Window也許更符合您需求。

Windows上也有很多IDE可供選擇，例如[Visual Studio](https://visualstudio.microsoft.com/zh-hant/)、[PyCharm](https://www.jetbrains.com/pycharm/)或[Atom](https://atom.io/)。前面Mac OS提過的Anaconda這個整合式開發環境也有，種類繁多。

更多詳細資訊，請參考[Windows Docs - 開始在 Windows 上使用適用於初學者的 Python](https://docs.microsoft.com/zh-tw/windows/python/beginners)。
**~註：從Python~** **~3.9開始，官方便不支援在Windows~** **~7及以下版本中安裝和執行，建議優先選擇Windows~** **~10以上的版本。~**

## <font color="#357EC7"> P</font><font color="#FFD700">y</font><font color="0000">thon</font>環境配置
這邊以Windows 11以及Visual Stidio Code做安裝示範：

### 1. 安裝Python
1. 前往 [Python <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width=20px alt="python">](https://www.python.org/downloads/)，選擇 "**Download Python 3.10**" 
**~註：小數點為例行性更新，直接下載即可~**

2. 安裝Python，選擇 "**Install Now**"
       
    ![](https://i.imgur.com/XuSitDx.png)
**~註：Add~ ~Python~ ~3.10~ ~to~ ~PATH~ <font color=#f0000>~記得要勾上~</font>**


### 2. 安裝Visual Studio Code
1. 前往[VS Code <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width=20px alt="vscode">](https://code.visualstudio.com/)，選擇 "**Download for Windows**"
2. 安裝VS Code，全部選同意；有其它選項的，照以下圖片操作：

    ![](https://i.imgur.com/drVlqJr.png)
    **~這邊不建議去改變安裝位置，避免出現奇奇怪怪的Bug~**

    ![](https://i.imgur.com/BMfgghK.png)
    **~這邊選下一步即可~**

    ![](https://i.imgur.com/kSALLt4.png)
    **~建議全部選上，方便後續操作，接著重新開機~**

### 3. 設置Visual Studio Code
1. 完成安裝之後開啟Visual Studio Code，應該會出現以下畫面，游標滑到左半邊，點選下面的 "**Mark Done**" 即可；右邊是換主題用的，稍後做示範

    ![](https://i.imgur.com/W4zTz7T.png)

2. 安裝繁體中文插件，點擊右邊的四個框框，輸入 "**traditional**"，選擇第一個，點擊 "**Install**"

    ![](https://i.imgur.com/QcNT2IZ.png)
    **~安裝完成會需要重新啟動VS~** **~Code，右下角會跳出提示框，點"立即重新啟動"即可~**

3. 安裝Python插件，輸入 "**Python**"，選擇第一個，點擊 "**安裝**"
    
    ![](https://i.imgur.com/PpvsNNg.png)

4. 安裝完Python，可能會跳出要配置[**Jupyter Notebooks**](https://jupyter.org/)的視窗，一樣滑到下面點擊"**標記完成**"即可

    ![](https://i.imgur.com/C0W4Eu4.png)



## [<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" width=30px alt="vscode">](https://code.visualstudio.com/) Visual Studio Code使用教學
### 1. 開啟資料夾及新增Python檔案
1. 找一個地方建立一個專門用來放程式的資料夾，像是在桌面建立一個"**Python_files**"資料夾
    **~資料夾的命名，如需連接兩個字，建議用~<font color=#f0000>**~下引號~~"~ ~_~ ~"~**</font> ~進行連接~**
2. 在資料夾上**點擊右鍵**，選擇 "**顯示其他選項**"，選擇 "**以Code開啟**" 

    ![](https://i.imgur.com/OyFOG45.png)

3. 勾選 "**信任父資料夾 '資料夾位置' 中所有檔案的作者**"，點擊 "**是，我信任作者 信任資料夾並啟用所有功能**"
    **~註：資料夾位置取決於您於哪個地方建立此資料夾，例如桌面就是'Desktop'~**
    
    ![](https://i.imgur.com/XpLV2Du.png)
    **~此操作僅須在新建資料夾後，第一次開啟時執行~**

### 2. 第一支Python程式
1. 移至最左邊的第一個文件選項，點擊 "**新增檔案**"
2. 新增一個檔案，副檔名為 "**.py**" 

    ![](https://i.imgur.com/V0A74RF.png)

    **~新增檔案按紐，在滑鼠游標靠近時會自動出現~**

    ![](https://i.imgur.com/xJoXBDW.png)
3. 在右邊編輯區塊輸入
```python=1
print("hello world")
```
4. 點擊右上角三角形執行鈕執行，查看Terminal返回值

    ![](https://i.imgur.com/dYFXvrQ.png)
  
    如果出現圖片所顯示的Terminal返回值，恭喜您，已經完成了第一隻Python程式的編譯
    
5. 儲存檔案
    1. VS Code上，未儲存的檔案，會在檔案名稱旁邊顯示一個點
    按 "**Ctrl**"+"**S**" 儲存
        
        ![](https://i.imgur.com/KuNeMrb.png)
        
    2. 每次離開VS Code前都記得要儲存
    **~雖然VS~ ~Code在每次執行時，都會自行存檔(Mac好像需要設定才會)，還是建議離開前按一下~ ~"~<font color=#f0000>~Ctrl~</font>~"~ ~+~ ~"~<font color=#f0000>~S~</font>~"~**
    
    3. 儲存完檔案，在資料夾裡面會多出一個長這樣的Python文件(下圖)，此Python已經可以直接執行，也可以 "**以Code開啟**" 來編輯
        
        ![](https://i.imgur.com/bdj0xdv.png)
        
        **~註：檔案開啟之後，出現一個黑框框然後馬上跳出，是正常的，因為指令執行完之後，程序就會自動退出，除非有特別去寫要暫停幾秒~**

### 3. 使用pip安裝模組 (module)
pip是一個專門設計給Python使用的軟件包管理系統，其中最常用的pip功能有 "**install**"、"**uninstall**" 及 "**list**"；而pip的用方法非常簡單，就是 "**pip**" + "**功能**"
#### 1. 以selenium為例，安裝模組
1. 點擊左上角的"**終端機**"，選擇"**新增終端**"

2. 在Terminal(終端機)中輸入 "**pip install**" + module name 
**~註：記得空格~**
```
pip install selenium
```
3. 等待Terminal返回 "Successfully installed"
    
    ![](https://i.imgur.com/h8DsjIB.png)
    
4. 按 "**F1**"，輸入 "**reload window**"，按**Enter**重新啟動頁面，完成安裝

    ![](https://i.imgur.com/S928wSy.png)


#### 2. 檢查已安裝的module
1. 在終端機輸入以下指令即可檢查已安裝模組
```
pip list
```
2. 如須清除terminal，則輸入cls即可
```
cls
```

#### 3. 以selenium為例，解除安裝module
1. 如需解除安裝module，在終端機輸入 "**pip uninstall**" + module name
**~註：記得空格~**
```
pip uninstall selenium
```
2. 然後終端機會返回要使用者確認的指示，輸入 "**Y**" 再按**Enter**即可

    ![](https://i.imgur.com/GERXuNr.png)

#### 4. 以selenium為例，更新module
Python的module資料庫相當龐大，常常會有新的更新出現，故更新module也因此成為了學習Python必修的技能之一
**~註：但除非有重大的功能性更新或是Bug修復，不然還是不要太常更新，容易導致程式碼出錯；因為新的module可能會換語法，而使用者尚未了解~**

1.  在Terminal(終端機)中輸入 "**pip install --update**"+module name 
**~註：記得空格~**
```
pip install --update selenium
```

### 4. 新增系統變數 (PATH)
PATH 是一個系統變數，可讓您的作業系統從指令行或終端機視窗中尋找所需的可執行檔。
[~JAVA~ ~-~ ~我要如何設定或變更~ ~PATH~ ~系統變數？~](https://www.java.com/zh-TW/download/help/path_zh-tw.html)

1. 將解壓縮完的資料夾移動到指定資料夾 
**~如果沒有特殊需求，建議將需要設定為PATH的資料夾拖放到C夾，這樣在設定PATH及日後更新會更方便~**

2. 按 **Windows鍵**，輸入 "**編輯系統環境變數**"

    ![](https://i.imgur.com/S3PUzA4.png)

4. 選擇 "**環境變數**"

    ![](https://i.imgur.com/UlhjKWP.png)

5. 選擇<font color=#f0000>**上面的**</font> "**Path**"，選擇 "**編輯**"

    ![](https://i.imgur.com/8Z2Wqdb.png)

7. 選擇 "**新增**"，選擇 "**瀏覽**"，找到剛才存放資料夾的位置；或是直接輸入存放資料夾的位置

    ![](https://i.imgur.com/PEDAC8R.png)
    **~如果按照上的說明操作，位置為：C:\chromedriver_win32~**

4. 按確定，接著重新啟動，完成PATH的設定

### 5. 變更主題及字型大小
Visual Studio Code的主題可以變更為預設的 "深色" 或是 "淺色"，也可以變更為其他開發者開發的主題，而其形式便是以**插件**的型態供使用者安裝及使用
#### 1. 變更字型大小
1. 點擊左下角的齒輪圖標，選擇設定

    ![](https://i.imgur.com/eqEe3kg.png)

3. 輸入 "**font size**"

    ![](https://i.imgur.com/jWsGC4a.png)


5. 變更第三個 "**Editor：Font Size**" 的數值，即可改變編譯器字型大小

    ![](https://i.imgur.com/YXiRogm.png)
    
#### 2. 變更內建主題
1. 點擊左下角的齒輪圖標，選擇 "**色彩佈景主題**"

    ![](https://i.imgur.com/JKbmQsV.png)

2. 上方會出現選項供使用者更改

    ![](https://i.imgur.com/Dqp4EGq.png)

#### 3. 變更為使用者自訂主題
前面提過，第三方的主題包，以插件的形式供使用者安裝，故安裝方式與前面安裝Python插件大同小異
1. 點擊右邊的四個框框，輸入想要的主題 (例如：Pink)

2. 選擇目標主題包，安裝，套用即可

    ![](https://i.imgur.com/nmppPR5.png)



### 6. 錯誤排查 (Debug)
寫程式的過程，免不了Debug的過程；而程式出錯的原因，大致上可以分成三種；Visual Studio Code其實會提示出錯的原因和建議的修正方式，只通常只適用於預設的語法錯誤，如果是因為module的語法或是引用出現錯誤，就只會提示 "**Index Error**"

#### 1. 出現錯誤後，Visual Studio Code會怎麼提示 (僅限語法錯誤)
1. 程式的名稱會變成黃色 
**~註：右邊的黑點代表尚未儲存~**
    
    ![](https://i.imgur.com/j5H36xJ.png)

    
    正常的程式碼名稱會是黑色的
    
    ![](https://i.imgur.com/TJNrTDx.png)

2. 出現錯誤的程式碼片段底下，會出現黃色波浪線

    ![](https://i.imgur.com/fbH8McP.png)

    
4. 下面終端機，最左邊的 "**問題**" 旁邊會出現數字
**~註：數字代表已發現的錯誤數量~**

    ![](https://i.imgur.com/lVeFBXb.png)

#### 2. 怎麼判斷是哪裡出錯
如前面所述，錯誤可以大致分成三種，此三種分別是 "**邏輯錯誤**"、"**語法錯誤**" 或者很令人難以理解的 "**當機**"
##### 1. 邏輯錯誤
邏輯錯誤，常見的表現是：當你寫完一段程式碼，並且順利執行了，可是回傳的值卻不是你所預期的，並且沒有語法或是執行次序上的錯誤

##### 2. 語法錯誤
語法錯誤，例如print打成prinf，這個語法錯誤會在VS Code上面直接顯示出來，通常terminal也會提示出建議的修正方法
    
```python=1
prinf("hello world")
```
此時terminal會提示 "**Did you mean: 'print'?**"，然後**問題**會顯示 "**'prinf' is not defined**"
##### 3. 當機
這種錯誤都出現的很突然，並且難以復現；但是檢查以下幾個重點：
- [x] 語法沒有錯誤
- [x] 一直報錯 "**Index Error**"
- [x] 已經安裝完的module，在import時，問題一直出現"**模組名稱 is not defined**"
- [x] [CSDN](https://www.csdn.net/)或是[Stack Overflow](https://stackoverflow.com/)找不到解答，Google上所有的方法都試過一遍，還是沒解決

都符合的話，那恭喜你，一定是當機了

#### 3. 怎麼修正錯誤

##### 1. 針對邏輯錯誤
舉例：求三角形面積，假設底邊長8cm，高4cm，兩邊長分別為5cm及根號41cm，答案應該是16平方公分；而答案卻返回了20平方公分
```python=1
from cmath import sqrt

height = 4
botton_len = 8
side_1 = 5
side_2 = sqrt(41)

area = (botton_len*side_1)/2

print(area)
```
**~terminal回傳值：20~**

這便是典型的邏輯錯誤，因為三角形間應該是"(底x高)/2"，而不是"(底x邊/2)"

所以應該改成
```python=8
area = (botton_len*height)/2
```
**~terminal回傳值：16~**

這樣程式的修正便完成了
##### 2. 針對語法錯誤
以前面舉例的prinf為例，VS Code已經給出了建議 "**print**"，那通常照建議去修改就沒問題了；若是提示**Index Error**，那可以把報錯的那行複製起來去Google，通常都會是因為沒有按照module的語法編寫或是打錯字
##### 3. 針對當機
造成當機的原因有很多種，可能是過熱、太久沒關機或者是記憶體滿了；而這種當機最煩的就是 "不是卡死" 也不是 "藍屏"，很多時候都是查來查去都找不出來，到最後重新開機就解決了，所以面對當機，只有下兩種解決辦法
1. 先儲存資料，然後按 "**F1**"，然後輸入 "**reload window**"，按**Enter**重新啟動VS Code

    ![](https://i.imgur.com/aWCRVuf.png)
    
2. 如果重新啟動VS Code還沒辦法解決問題的話，那就趕快儲存資料，然後重新開機

___
[<img src="https://i.imgur.com/OgS1fhr.gif" width="75px" alt="logo">](https://hackmd.io/@KSHS-PyClub)<font size="5" font face="微軟正黑體">**K3S12 <font color="#357EC7">P</font><font color="#FFD700">y</font><font color="0000">thon</font>** **Studio**</font> 
