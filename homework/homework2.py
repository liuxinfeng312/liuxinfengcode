import requests
from bs4 import BeautifulSoup
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url='https://hr.tencent.com/position.php?keywords=python'
response=requests.get(url,headers=headers)
print(response.content.decode())
