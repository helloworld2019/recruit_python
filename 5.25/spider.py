import urllib.request
import os
from selenium import webdriver
import time 


def open_url(url):
	headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
	req = urllib.request.Request(url,None,headers)

#	req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')	
	response = urllib.request.urlopen(req)
	html = response.read()	
	return html

def find_page(html):
	a = html.find("img src")
	img_addrs = []
	while a != -1 :
		a = a+ 9 
		b = html.find('.jpg',a)
		if b == -1 :
			break
		b = b + 4
		img_addrs.append(html[a:b])	
		a = html.find("img src",b)
	
	return img_addrs

def next_page(html):
	a = html.find("Older Comments") 
	b = html.find("page-",a)+5
	c = html.find("#",b);
	
	return html[b:c] 


def save_pic(pic_list):
		for each in pic_list:
			filename = each.split('/')[-1]
			with open(filename,'wb') as f:
					img = open_url(each)
					f.write(img)

		return 

def download_mm(folder = "mm" , pages=100):
	if os.path.exists(folder):
		os.chdir(folder)
	else:
		os.mkdir(folder)


	driver = webdriver.Firefox();
	
	url = "https://jandan.net/ooxx/"
	
	page_url = url
	page = 1
	for each in range(pages):
		print("page:")
		print(page)
		page +=1
		print("the page is")
		print(page_url)
		driver.get(page_url)
		html = driver.page_source
		pic = find_page(html)	
		save_pic(pic)
		page_url = url + "page-"+ str(next_page(html))+"#comments"
		print("next page is")
		print(page_url)
	return 




if __name__ == '__main__' :
	download_mm();
