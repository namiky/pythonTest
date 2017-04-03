from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html lang="ja">
<title>title1</title>
<body>
<div id="main">
  <h1>AI Academyの特徴</h1>
    <ul class="items">
      <li><a href="http://aiacademy.jp">AI Academy1</a></li>
      <li><a href="http://aiacademy.jp">AI Academy2</a></li>
      <li><a href="http://aiacademy.jp">AI Academy3</a></li>
    </ul>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.select_one("div#main > h1").string
print("h1: ",h1)

li_list = soup.select("div#main > ul.items > li")
for li in li_list:
    print("li: ", li.string)