#!/usr/bin/python3

import urllib.request
import json 

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"

head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299' 


while True:
		content=input("chinese: ")
		
		data={}
		data['action']="FY_BY_REALTIME"
		data['client']="fanyideskweb"
		data['doctype'] ="json"
		data['from']="AUTO"
		data['keyfrom']="fanyi.web"
		data['salt']= "1527077804473"
    	data['sign'] ="262add68ec9d4cf6e002c6d008541a97"
    	data['smartresult']= "dict"
    	data['to']= "AUTO"
    	data['typoResult']="false"
    	data['version']="2.1"



		data=urllib.parse.urlencode(data).encode('utf-8')
		response = urllib.request.urlopen(url,data);
		
#response.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')

		html = response.read().decode("utf-8")
#print(html);
		target = json.loads(html);
		print("result %s" % (target['translateResult'][0][0]['tgt']) )
