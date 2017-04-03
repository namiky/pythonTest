import urllib.request
from bs4 import BeautifulSoup
import time
import os

# 画像ダウンロード
def download_image(url,name):
    path = "./scrape_image/"    # 保存場所
    imagename = str(name) + ".jpg"  #保存ファイル名

    if not os.path.exists(path):
        os.makedirs(path)

    print("download...", url)
    print(path)
    urllib.request.urlretrieve(url, path+imagename)
    time.sleep(1) # 1秒スリープ

##
pictureNumber=10    # 取得枚数
url = "https://api.photozou.jp/rest/search_public.xml?keyword=%E7%8C%AB&limit="+str(pictureNumber) #フォト蔵のAPI
response = urllib.request.urlopen(url)
rss = response.read().decode("utf-8")

soup = BeautifulSoup(rss, "xml")

name = 0
for s in soup.find_all("photo"):
    url = s.find_all("image_url")[0].string
    name+=1
    download_image(url,name)