##
from bs4 import BeautifulSoup
import urllib.request

print("-----------------")
## input 検索単語名
print("input indeed what value.")
print("(ex) python / java / javascript / ruby / C# / php / perl / html / css / swift / objective-c")
indeedWhat=input(":")

## input 検索時の国
print("input indeed where number.")
print("1 : japan\n2 : canada\n3 : United States\n4 : Australia")
indeedWhere=input(":")

## 入力値からどのURLを使用するか
if indeedWhere == "1": # japan
    url="https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q="+indeedWhat+"&l=japan"
    LANG="JP"
elif indeedWhere == "2":
    url = "https://www.indeed.ca/jobs?q=" + indeedWhat + "&l=canada"
    LANG = "EN"
elif indeedWhere == "3":
    url = "https://www.indeed.com/jobs?q=" + indeedWhat + "&l=United+States"
    LANG = "EN"
elif indeedWhere== "4": #"Australia"
    url = "https://au.indeed.com/jobs?q="+indeedWhat+"&l=Australia"
    LANG = "EN"
else:
    print ("error")
    exit()
print("-----------------")


## varidates
#url = "https://jp.indeed.com/%E6%B1%82%E4%BA%BA?q=python&l=japan"     #日本
#url = "https://www.indeed.ca/jobs?q=python&l=canada"                           #canada
#url = "https://www.indeed.com/jobs?q=python&l=United+States"                   # usa
#url = "https://au.indeed.com/jobs?q=python&l=Australia"                        # australia

# Get Web page
req = urllib.request.Request(url)
response = urllib.request.urlopen(req)
html = response.read()
soup = BeautifulSoup(html,'html.parser')

## 掲載数
def getNumber():
    target = "searchCount"
    contextTag=soup.find(id=target)
    context=str(contextTag)
    peopleSum=getNumberCount(context,LANG)
    print("総合求人数："+peopleSum+"件")
    print("-----------------")
    return peopleSum

## 給与額面
def getSalary():
    ##
    result1=[]
    result2=[]

    ## 取得箇所
    target = "div#SALARY_rbo > ul > li > a"
    salaryList = soup.select(target)
    peopleSum=0

    for m in salaryList:
        a=getSalaryCont(m.get("title"))
        print("金額　：" + a[0]) #salaryVal
        print("求人数：" + a[1]) #peopleVal
        print("-----")
        result1.append(a[0]) #金額
        result2.append(a[1]) #求人数

    return result1,result2

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

##変数宣言
result1=[]
result2=[]

##実行
peopleSum=getNumber()
result1,result2=(getSalary())


print(peopleSum)
print(result1)
print(result2)

##エンドまでの確認用
print("end...thanks")
print("-----------------")
