# -*- coding: utf-8 -*-
import re
import urllib.request
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='https://www.qiushibaike.com/text/page/1/'
req=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(req)
content=response.read().decode()
# print(content)
text='<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number'
coms=re.compile(text,re.S)
strs=coms.findall(content)
# print(strs[0])


# 匹配名字
for item in strs:
    # print(item)
    # 匹配评论
    contentments='<span>(.*?)</span>'
    contentment=re.compile(contentments,re.S)
    con=contentment.findall(item)[0]

    # 匹配名字
    name='<h2>(.*?)</h2>'
    names=re.compile(name,re.S)
    str1=names.findall(item)[0]

    strall=str1.rstrip()+'说:'+con.strip()
    # strall1=strall.decode(type['encoding'])
    print(strall)
    with open('homework1.txt','a+',encoding='utf-8') as fp:
        fp.write(strall)





# str1.strip('')

