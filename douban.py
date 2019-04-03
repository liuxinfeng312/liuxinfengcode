import json
import os
import urllib.request

from urllib import request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=1'
req=urllib.request.Request(url,headers=headers)
response=urllib.request.urlopen(req)
context=response.read().decode()
image_list=json.loads(context)
print(image_list[0]['cover_url'])
print(image_list[0])
print(image_list)

# for i in range(1, 3):
#     url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
#     i ) + "&limit=20"
#     req=urllib.request.Request(url,headers=headers)
#     response=urllib.request.urlopen(req)
#     context=response.read().decode()
#     print(context)




for images in image_list:
    # print((images))
    # print(images['title'])
    name=images['title']+'.jpg'
    pathname='../dir/'+name
    # request.urlretrieve(images['cover_url'], pathname)
    # print(name)
    print('正在下载',name)



    (request.urlretrieve(images['cover_url'], images['title']+'.jpg'))


