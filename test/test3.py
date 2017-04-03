##特定のサイトの全HTMLコードを出力
#urllib.urlopen(url[, data[, proxies[, context]]])
from urllib.request import urlopen
html = urlopen("http://aiacademy.jp")
data = html.read()
##
print("---------------")
decoded_data = data.decode('utf-8') # decodeがうまく機能しない場合はこの行を削除
print(decoded_data)
##
print("---------------")
decoded_data = data
print(decoded_data)