import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=opt)
driver.get("https://act.hoyolab.com/bbs/event/signin/hkrpg/index.html?act_id=e202303301540311&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&utm_campaign=checkin&utm_id=6&lang=zh-tw&bbs_theme=light&bbs_theme_device=1")
