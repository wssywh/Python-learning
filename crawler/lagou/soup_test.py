#coding:utf-8
from bs4 import BeautifulSoup
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print(tag)
print(tag.attrs)
print(tag['class'])
print()