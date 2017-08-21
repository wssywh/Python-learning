from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get(
    "https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228")
time.sleep(3)
print(driver.page_source)
# print(driver.page_source.encode('gbk', 'ignore'))
  # 这个函数获取页面的html
driver.get_screenshot_as_file("2.jpg")  # 获取页面截图
print("Success To Create the screenshot & gather html")


driver.close()
