# -*- coding: utf-8 -*


import webbrowser as web
import time
import os

urllist = [
    'https://blog.csdn.net/ViatorSun/article/details/84554874',
    'https://blog.csdn.net/ViatorSun/article/details/82917094',
    'https://blog.csdn.net/ViatorSun/article/details/86560727',
    'https://blog.csdn.net/ViatorSun/article/details/84261266',
    'https://blog.csdn.net/ViatorSun/article/details/82934935',
    'https://blog.csdn.net/ViatorSun/article/details/89609586',
    'https://blog.csdn.net/ViatorSun/article/details/80192355',
    'https://blog.csdn.net/ViatorSun/article/details/82983401',
    'https://blog.csdn.net/ViatorSun/article/details/81363841',
    'https://blog.csdn.net/ViatorSun/article/details/80286649',
    'https://blog.csdn.net/ViatorSun/article/details/96430089',
    'https://blog.csdn.net/ViatorSun/article/details/86577653',
    'https://blog.csdn.net/ViatorSun/article/details/88787089',
    'https://blog.csdn.net/ViatorSun/article/details/82914713',
    'https://blog.csdn.net/ViatorSun/article/details/82831582',
    'https://blog.csdn.net/ViatorSun/article/details/82052193',
    'https://blog.csdn.net/ViatorSun/article/details/82350107',
    'https://blog.csdn.net/ViatorSun/article/details/81350342',
    'https://blog.csdn.net/ViatorSun/article/details/86819765',
    'https://blog.csdn.net/ViatorSun/article/details/82418578',
    'https://blog.csdn.net/ViatorSun/article/details/86546993',
    'https://blog.csdn.net/ViatorSun/article/details/89717118',
    'https://blog.csdn.net/ViatorSun/article/details/82696475',
    'https://blog.csdn.net/ViatorSun/article/details/81880679',
    'https://blog.csdn.net/ViatorSun/article/details/83892683',
    'https://blog.csdn.net/ViatorSun/article/details/90704996',
    'https://blog.csdn.net/ViatorSun/article/details/82351222',
    'https://blog.csdn.net/ViatorSun/article/details/88884397',
    'https://blog.csdn.net/ViatorSun/article/details/81365244',
    'https://blog.csdn.net/ViatorSun/article/details/80993963',
    'https://blog.csdn.net/ViatorSun/article/details/84790462',
    'https://blog.csdn.net/ViatorSun/article/details/92840186',
    'https://blog.csdn.net/ViatorSun/article/details/80369520',
    'https://blog.csdn.net/ViatorSun/article/details/82934861',
    'https://blog.csdn.net/ViatorSun/article/details/81007380',
    'https://blog.csdn.net/ViatorSun/article/details/88963665',
    'https://blog.csdn.net/ViatorSun/article/details/88377300',
    'https://blog.csdn.net/ViatorSun/article/details/99675274',
    'https://blog.csdn.net/ViatorSun/article/details/82387854',
    'https://blog.csdn.net/ViatorSun/article/details/82751273',
    'https://blog.csdn.net/ViatorSun/article/details/82415345',
    'https://blog.csdn.net/ViatorSun/article/details/80285929',
    'https://blog.csdn.net/ViatorSun/article/details/81066134',
    'https://blog.csdn.net/ViatorSun/article/details/83037784',
    'https://blog.csdn.net/ViatorSun/article/details/88082626',
    'https://blog.csdn.net/ViatorSun/article/details/82826664',
    'https://blog.csdn.net/ViatorSun/article/details/80204628',
    'https://blog.csdn.net/ViatorSun/article/details/100703100',
    'https://blog.csdn.net/ViatorSun/article/details/101931633',
    'https://blog.csdn.net/ViatorSun/article/details/102713679',
    'https://blog.csdn.net/ViatorSun/article/details/102611431',
    'https://blog.csdn.net/ViatorSun/article/details/102828342',
    'https://blog.csdn.net/ChelsaCheng/article/details/102731006']

for j in range(0, 10):  # 设置循环的总次数
    i = 0
    while i < 1:  # 一次打开浏览器访问的循环次数
        for url in urllist:
            web.open(url )  # 访问网址地址，语法 .open(url,new=0,Autorasise=True),设置 new 的值不同有不同的效果0、1、2
            i = i + 1
            time.sleep(1)  # 设置每次打开新页面的等待时间
    else:
        time.sleep(5)  # 设置每次等待关闭浏览器的时间
        os.system('D:\Program Files (x86)\Tencent\QQBrowser\QQBrowser.exe')  # 你设置的默认使用浏览器，其他的更换下就行