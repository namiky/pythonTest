# coding: utf-8
# Here your code !
print("------------------------------------------------")

'''
comment out message
'''

# math
print(10/2)
print(10//2)

# for
#for i in range(0,5):
#    print(i)

# variable
a = "apple"
b = "bottle"
c = "coin"

A = len(a)
B = len(b)
C = len(c)

print(a)
print(A)
print(str(a)+str(A))

# list[]
li1 = [1,2,3]
li2 = ["a","b","c","d"]
li3 = [1,"b",3,]
for i in li1:
    print(i)
for i in li2:
    print(i)
for i in li3:
    print(i)

# type judge
print(type(li1))
print(type(li2))
print(type(li3))

# dictionary{}
di = {"k1":"a","k2":"b","k3":"c"}
print(di["k1"])
print(di["k2"])
print(di["k3"])
print()
for key in di:
    print(key)
    print(di[key])
print()

# false or true
t = True
f = False

# if context
if f:
    print("true")
else:
    print("false")
print()

# range method
for i in range(5):
    if(i%3==0):
        print (i)
print()

# making method
def met1(str="deafult"):
    print ("hello "+str)
met1("world")
met1()
print()

# class
# class のイニシャルは大文字であること
class Class1:
    def __init__(self,name):
        self.name=name
        print("コンストラクタが呼びされました")
    def sample(self):
        print("sampleが呼び刺されました")
    def hello(self):
        print("helloが呼び刺されました")
        print("Hello",self.name)
C1=Class1("test")
C1.sample()
C1.hello()
print()

class Class2:
    def __init__(self,a1,a2,a3):
        print("コンストラクタが呼びされました")
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        print(self.a3)
    def sample(self):
        print("sampleが呼び刺されました")
        print(self.a1)
    def hello(self):
        print("helloが呼び刺されました")
        print(self.a2)

C2=Class2("test",1,"bb")
C2.sample()
C2.hello()
print()

print()
#import os
#print(os.path.expanduser('~'))

print("------------------------------------------------")


