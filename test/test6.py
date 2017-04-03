from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ja">
<title>testTitle</title>
<body>
    <h1>AI Academyとは？（エーアイ アカデミーとは？）</h1>
    <p>人工知能プログラミングに特化したマンツーマン オンラインプログラミングスクールです。</p>
    <p>プログラミング言語Pythonを使いながら、機械学習や深層学習などを学習します。</p>
    <ul>
        <ol><a href="http://aiacademy.jp">AI Academy1</a></ol>
        <ol><a href="http://aiacademy.jp">AI Academy2</a></ol>
        <ol><a href="http://aiacademy.jp">AI Academy3</a></ol>
    </ul>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

links = soup.find_all("a")

for a in links:
    href = a.attrs['href']  # attrs = attributes = 属性
    text = a.string
    print(text, href)


print("done")