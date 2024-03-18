def install():
    import os 
    os.system("pip install pywin32")

start = False
while(start==False):
    try:
        from win32 import win32gui, win32print
        from win32.lib import win32con
        from win32.win32api import GetSystemMetrics 
        start = True

    except:
        install()
        break

def resolution():
    HDC = win32gui.GetDC(0)
    width = win32print.GetDeviceCaps(HDC, win32con.DESKTOPHORZRES)
    height = win32print.GetDeviceCaps(HDC, win32con.DESKTOPVERTRES)
    return(width, height)

def metrics():
    (width, height) = (GetSystemMetrics(0), GetSystemMetrics(1))
    return (width, height)

def magnification():
    res = resolution()
    met = metrics()
    return(round(res[0]/met[0], 2))
