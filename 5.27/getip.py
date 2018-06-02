'''
import urllib.request

url1 = "https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query="

url2="&co=&resource_id=6006"

ip = input("please input the ip: \n")

url = url1 + ip + url2

response = urllib.request.urlopen(url).read().decode("gbk")

import json

result = json.loads(response)["data"][0]["location"]

print(result);
'''

headers ={
"Accept":"text/html, application/xhtml+xml, image/jxr, */*",
"Accept-Language": "zh-CN",
"Cache-Control": "no-cache",
"Connection":"Keep-Alive",
"Content-Length": "219",
"Content-Type": "application/x-www-form-urlencoded",
"Host": "u.mumayi.com",
"Referer": "http://u.mumayi.com/oauth/?m=Oauth&a=authorize&client_id=100004&response_type=code&display=&error_line=3&error_info=%E9%AA%8C%E8%AF%81%E7%A0%81%E5%A1%AB%E5%86%99%E9%94%99%E8%AF%AF%EF%BC%81"
}

post_data={
"accept":"Yep",
"client_id": "100004",
"mycode": "0991",
"passwd": "123456a",
"redirect_uri":"http%3A%2F%2Fpay.mumayi.com%2F%3Fa%3Dcallback",
"response_type":"code",
"scopelist%5B%5D":"basicinfo",
"scopelist%5B%5D": "bbsinfo",
"usernm":"service@52exe.cn"
}

url = "http://u.mumayi.com/oauth/?m=Oauth&a=authorize"

import urllib.request

encode_data = urllib.parse.urlencode(post_data).encode("utf-8")
print("encode_data")
req = urllib.request.Request(url=url,data=encode_data,headers=headers)

print("req")		
response = urllib.request.urlopen(req).read().decode("gbk")

print(response)		
