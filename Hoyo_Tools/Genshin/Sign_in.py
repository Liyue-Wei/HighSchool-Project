import os
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

os.popen('start chrome --remote-debugging-port=9527 --user-data-dir="C:\chromedriver_win32"')
opt = Options()
opt.add_experimental_option("debuggerAddress", "127.0.0.1:9527")
driver = webdriver.Chrome(options=opt)
driver.get("https://act.hoyolab.com/ys/event/signin-sea-v3/index.html?act_id=e202102251931481&hyl_auth_required=true&hyl_presentation_style=fullscreen&utm_source=hoyolab&utm_medium=tools&lang=zh-tw&bbs_theme=light&bbs_theme_device=1")
