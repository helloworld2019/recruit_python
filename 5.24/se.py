
from selenium import webdriver
import time 
driver = webdriver.Firefox();
url = "http://www.jandan.net/ooxx"
driver.get(url);
time.sleep(5)
html = driver.page_source
print(html)
