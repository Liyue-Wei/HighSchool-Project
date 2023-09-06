# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/2048px-Octicons-mark-github.svg.png" width="38px" alt="github"> GitHub入門指南
###### tags: `GitHub`

## GitHub與Git
Git是一種分散式版本控制系統，它可以讓多人協同開發軟體；而GitHub則是原始碼的代管平台，使用Git來管理儲存庫（Repository）。

可以簡單的理解為：Git是一種工具，而GitHub則是一個使用Git操作的平台。

GitHub還有提供GitHub Pages的靜態網頁代管服務，可以參見[GitHub Pages使用教學](https://hackmd.io/@K3S12-Python-Studio/GH_Page)。

## GitHub Repository
GitHub Repository（GitHub repo）就是GitHub上面的專案資料夾。
### 建立GitHub repo
1. 註冊GitHub帳號，並登入個人介面（Your profile）
2. 點擊「Repository」，再點擊「New」
3. 輸入「Repository name」以及「Description」（非必要）
4. 勾選「Add a README file」選項（往後執行git push會比較方便）
5. 若不需要新增「.gitignore」或「license」，點擊「create repository」即可完成repo的建立

更多詳細資訊，請參考[GitHub Docs - Create a repo](https://docs.github.com/en/get-started/quickstart/create-a-repo)。

## GutHub Desktop
GitHub Desktop是一個由GitHub官方開發的桌面端應用程式，能夠很方便地以圖形化介面來創建GitHub repo，或是操作Git Clone以及Git Push，可以大幅縮短學習時間。
### 安裝GitHub Desktop
GutHub Desktop的安裝步驟非常簡單。
1. 前往[GutHub Desktop](https://desktop.github.com/)，選擇"**Download for Windows**" 
**~註：Mac~ ~OS或許會是Download~ ~for~ ~Mac~ ~OS~**
2. 安裝GitHub Desktop，全部都選下一步即可

## Git
Git Clone、Git Push是Git最常使用到的功能，其主要目的分別為「將Github上的版本下載至本機」以及「將新的版本推送到GitHub上」。
### 安装Git
1. 前往[Git](https://git-scm.com/downloads)，依作業系統下載，Windows直接選擇"**Download for Windows**"
2. 安裝Git，同樣全部都選下一步，不建議修改預設安裝的選項
### git clone
1. 開啟git bush
2. 輸入「cd」+目標位置，例如「cd desktop」
**~註：目標位置就是clone下來的檔案要存放的位置~**
3. 找到GitHub上面的Clone URL
4. 輸入「git clone」+「Clone URL」
~例如：「git~ ~clone~ ~"https://github.com/GitHub-UserName/GitHub.git"」~
**~註：上述URL為範例，沒辦法實際執行Clone~**
5. 等Git Bush執行完成，目標位置會存在一個GitHub專案名稱的資料夾
**~註：若Git~** **~Bush回報「remote:~** **~Repository~** **~not~** **~found.」，請檢察Clone~** **~URL是否正確~**

### git push
1. 新增檔案至GitHub專案資料夾
2. 開啟git bush
**~註：也可以在資料夾上點擊右鍵，選擇「git~** **~bush~** **~here」，省略第三步驟~**
3. 輸入「cd」+資料夾位置
~例如：「cd~ ~"C:\Users\Admin\Desktop\GitHub"」~
4. 輸入「git add」+「新增的資料夾(或檔案，記得加副檔名)」
~例如：git~ ~add~ ~"GitHub"~
5. 輸入「git commit -m」 + 「新增的資料夾(或檔案，記得加副檔名)」
6. 輸入：「git push」
**~註：若git~** **~bush回報「Everything~** **~up-to-date」，重新執行第四、五步驟~**
7. 等Git Bush執行完成，GitHub Repositories裡面可以找到新增的檔案
___
### Authored by [**Liyue-Wei**](https://github.com/Liyue-Wei) on GitHub
