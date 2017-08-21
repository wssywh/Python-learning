#coding:utf-8
# 引入selenium中的webdriver
from selenium import webdriver
import time

# webdriver中的PhantomJS方法可以打开一个我们下载的静默浏览器。
# 输入executable_path为当前文件夹下的phantomjs.exe以启动浏览器
driver = webdriver.PhantomJS(executable_path="/home/gao/PycharmProjects/python3/crawler/freebuf/phantomjs-2.1.1-linux-i686/bin/phantomjs")

# 使用浏览器请求页面
# driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
driver.get("https://www.lagou.com/zhaopin/Python/")
# 加载3秒，等待所有数据加载完毕
time.sleep(3)
# 通过id来定位元素，
# .text获取元素的文本数据
# print(driver.find_element_by_id('content').text)
data = driver.page_source
print(data)

# 关闭浏览器
driver.close()
