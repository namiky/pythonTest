##特定サイトの画像を取得して、pythonファイルの直下にfileを生成
#retrive = 検索、回収する
#urllib.urlretrieve(url[, filename[, reporthook[, data]]])
import urllib.request
imgname = "py.png"
url = "http://aiacademy.jp/img/"+imgname
urllib.request.urlretrieve(url, imgname) # fileを取得して、直下に生成
print("done.")





