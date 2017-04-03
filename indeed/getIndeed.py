from bs4 import BeautifulSoup
import urllib.request

##メンテするとき
##①urlの変数を手動で買える
##②getNumberメソッドのENとJPを手動で買える

print("-----------------")
## varidates
#url = "https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&l=japan"     #日本
url = "https://www.indeed.ca/jobs?q=python&l=canada"                           #canada
#url = "https://www.indeed.com/jobs?q=python&l=United+States"                   # usa
#url = "https://au.indeed.com/jobs?q=python&l=Australia"                        # australia

# Get Web page
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

## 掲載数
def getNumber():
    ## retried
    # number
    target = "searchCount"
    contextTag=soup.find(id=target)
    context=str(contextTag)
    print("総合求人数："+getNumberCount(context,"EN"))
    print("-----------------")

## 給与額面
def getSalary():
    target = "div#SALARY_rbo > ul > li > a"
    salaryList = soup.select(target)
    peopleSum=0
    for m in salaryList:
        a=getSalaryCont(m.get("title"))
        print("金額　：" + a[0]) #salaryVal
        print("求人数：" + a[1]) #peopleVal
        print("-----")


def getSalaryCont(a):
    salaryVal=""             # 給与金額を取得。空っぽで宣言
    peopleVal=""              # 求人数を取得。空っぽで宣言
    peopleSum=""            # 総求人数を取得。空っぽで宣言
    flg = True               # 数字⇒文字列⇒数字の切り替え用のフラグ
    for l in a:           # 1文字ずつ処理
        if l=="," or l=="$":              # カンマとドルがSkip
            pass
        elif l.isdigit():       # 数字なら
            if flg==True:       #文字に遭遇していないなら
                salaryVal=salaryVal+ str(l)
            else:
                peopleVal+=l
        else:
            flg = False
    return salaryVal,peopleVal







######
##LANG==JPなら1回目の数字群が期待値
##LANG==ENなら3回目の数字群が期待値
def getNumberCount(context,LANG):
    flgCount= 0 if LANG=="JP" else 2
    peopleSum=""            # 総求人数を取得。空っぽで宣言
    prevLiteral=""           #1文字前

    for l in context:  # 1文字ずつ処理
        if flgCount<0:
            break
        elif l == "," or l == "$":  # カンマとドルがSkip
            pass
        elif l.isdigit():  # 数字なら
            if flgCount==0:     #取得対象(総数の数字列のとき）
                peopleSum = peopleSum + str(l)
            else:   #   取得対象外（それいがいの数字列のとき）
                pass
            prevLiteral=l   # 処理後に今回の文字を保存して次の処理での判定に使用
        else:   # 文字なら
            if prevLiteral.isdigit():  # １つ前が数字、今が文字のとき
                flgCount -= 1 # FlgCountを１つ下げる（ex)30is6*5のiのタイミング
            prevLiteral=l   # 処理後に今回の文字を保存して次の処理での判定に使用
    return peopleSum


###テストデータ
#print(getNumberCount("""<div id="searchCount">求人検索結果 4,878 件中 1 - 10</div>""",LANG))
#print(getNumberCount("""<div id="searchCount">Jobs 1 to 20 of 3,742</div>""",LANG))


##実行
getNumber()
getSalary()

##エンドまでの確認用
print("end...thanks")
print("-----------------")
