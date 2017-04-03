from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ja">
<title>testTitle</title>
<body>
    <h1>AI Academyとは？（エーアイ アカデミーとは？）</h1>
    <p>人工知能プログラミングに特化したマンツーマン オンラインプログラミングスクールです。</p>
    <p>プログラミング言語Pythonを使いながら、機械学習や深層学習などを学習します。</p>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

title = soup.find("title")
body = soup.find("body")

##titleやbodyがが存在しないとエラーになる
print("title: " + title.string)
print("body: " + body.text)