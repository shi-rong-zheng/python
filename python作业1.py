#第一题
"""
s=0
for i in range(1,101):
    s=s+i
print("s=",s)
"""
#第二题
"""
s=0
for i in range(1,50):
    m=1/(2*i-1)
    s=s+m
print("s=",s)
"""
#第四题
#方法一:
"""
s=0
a=2
b=1
i=1
while i<21:
    s=s+a/b
    m=a
    a=a+b
    b=m
    i=i+1
print("s=",s)
"""
#方法二:
"""
s=0
a=2
b=1
for i in range(1,21):
    s = s + a / b
    m = a
    a = a + b
    b = m
print("s=",s)
"""
#第五题
"""
i=1
sum=0
count=0
while i:
    i=i+1
    n=float(input("请输入平时成绩:"))
    if n<0 or n>100:
        print("無效成績,結束輸入")
        break
    else:
       sum=sum+n
       count+=1
       i = i + 1
print("average=",sum/count)
"""
#第八题
"""
def fib(n):
    fibs=[1,3,5]
    for i in range(n-2):
         fibs.append(fibs[-1]+fibs[-2])
    return fibs
s=1
for i in range(1,20):
    s=s+fib(19)[i]
print(fib(19))
print("前20项之和s为:",end="")
print("s=",s)
"""
#第十一题
"""
year=0
xiaohua=12
mother=32
while mother/xiaohua!=2:
    xiaohua+=1
    mother+=1
    year+=1
print("year=",year)
"""
#第十四题
"""
def fun():
    h=80
    for i in range(1,11):
        h=h/2
    return h
def fun1():
    h=80
    sum=0
    for i in range(1,11):
        m=h
        h=h/2
        sum=sum+h+m
    return sum
m=fun1()
n=fun()
print("第十次反弹有%f米"%(n))
print("第十次落地时一共经过%f米"%(m))
"""
"""
shen=["广东","四川","贵州"]
cs=[["广州","深圳","惠州","珠海"],["成都","内江","乐山"],["贵阳","六盘水","遵义"]]
def fun(s):
    for i in range(len(cs)):
        for x in cs[i]:
            if x==s:
                print(s,"在",shen[i]+"省")
                return
    print("未查询到！")
s=input("请输入城市:")
fun(s)
"""
#strip()函数的用法
"""
s=input("请输入:")
print(s,len(s))
b=s.strip()
print(b,len(b))
"""
"""
def max(a,b):
    return a if a>b else b
a=int(input("a="))
b=int(input("b="))
print("Max：",max(a,b))
"""
"""
s=(1,3,2,3,4,5)
print(s)
print(type(s))
"""
"""
week=("日","一","二","三","四","五","六")
print(week)
w=int(input("请输入:"))
if w>=0 and w<=6:
    print("星期"+week[w])
else:
    print("错误输入")
"""
"""
def fun(x,y,*args):
    print(x,y)
    print(args)
fun(1,2)
fun(1,2,3)
fun(1,2,3,4)
fun(1,2,3,4,5)
"""
#使用tuple()元组比较大小
"""
def max(*args):
    print(args)
    m=args[0]
    for i in range(len(args)):
        if m<args[i]:
            m=args[i]
    return m
print(max(4,8))
print(max(1,2,0,3))
"""
"""
def max(*args):
    print(args)
    m = args[0]
    for i in range(len(args)):
        if m<args[i]:
            m=args[i]
    return m
print(max(3,5))
"""
# list=[0,1,1]
# n=int(input("请输入:>"))
# for i in range(3,n):
#     list.append(list[-1]+list[-2])
# print(list)

# a=0
# b=1
# list=[]
# n=int(input("请输入:>"))
# for i in range(0,n):
#     a,b=b,a+b
#     print(a)
























