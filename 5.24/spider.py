#!/usr/bin/python3

import urllib.request
import os


def open_url(url):
	headers={'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'}
	req = urllib.request.Request(url,None,headers)

#	req.add_header('User-Agent','Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0')	
	response = urllib.request.urlopen(req)
	html = response.read()	
	return html

def find_page(html):
	a = html.find("img src")+9
	img_addrs = []
	print("i am in the find\n")
	while a!=-1:
		b = html.find('.jpg',a)-1
	    
		if c!=-1:
			img_addrs.append(html[a:b])	
			a = html.find("img src",b)

	print("finish\n")

	for each in img_addrs:
		print(each)
	
	return img_addrs

def next_page(html):
	a = html.find("Older Comments") 
	b = html.find("page-",a)+5
	c = html.find("#",b)-1;
	print(html[b:c])
	
	return html[b:c] 


def save_pic(pic_list):
		for each in pic_list:
			filename = each.split('/')[-1]
			with open(filename) as f:
					img = open_url(each)
					f.write(img)

		return 

def download_mm(folder = "mm" , pages=10):
	if os.path.exists(folder):
		os.chdir(folder)
	else:
		os.mkdir(folder)


	url = "https://jandan.net/ooxx/"
	
	page_url = url

#	for each in range(pages):
	html = open_url(page_url).decode("utf-8")
	pic = find_page(html)	
#			save_pic(pic)
#			page_url = url + "page-"+ str(next_page(html))

	return 




if __name__ == '__main__' :
	download_mm();
