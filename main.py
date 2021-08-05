# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(i,j,i*j),end='  ')
#     print("\n")

#题目1
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if(i!=j)and(j!=k)and(i!=k):
#                 print(i,j,k,end='  ')
#     print("\n")

# 题目二
# year=int(input("请输入某年:>"))
# month=int(input("请输入某月(1,12):>"))
# day=int(input("请输入某日:>"))
# sum=0
# month_list=[31,28,31,30,31,30,31,31,30,31,30,31]
# if((year%4==0)and(year%100!=0)or(year%400==0)):
#     if(month>2):
#         for i in range(1,month):
#             sum=month_list[i]+sum
#         sum=sum+day+1
#         print("这一天是这一年的第%d天"%sum)
#     else:
#         sum=month_list[0]+day
#         print("这一天是这一年的第%d天"%sum)
# else:
#     if (month > 2):
#         for i in range(1, month):
#             sum = month_list[i] + sum
#         sum = sum + day
#         print("这一天是这一年的第%d天" % sum)
#     else:
#         sum = month_list[0] + day
#         print("这一天是这一年的第%d天" % sum)

# first=int(input("请输入整数:>"))
# second=int(input("请输入整数:>"))
# last=int(input("请输入整数:>"))
# temp=0
# if(a>b):
#     temp=b
#     b=a
#     a=temp
# if(b>c):
#     temp = c
#     c=b
#     b = temp
# if(a>c):
#     temp = c
#     c = a
#     a = temp

# list=[a,b,c]
# list.sort()
# print("%d<%d<%d"%(a,b,c))
# print(list)

# if((first>second)and(first>last)and(second>last)):
#     print(first,second,last)
# if((last>second)and(last>first)and(second>last)):
#     print(last,second,last)
# if((second>first)and(second>last)and(first>last)):
#     print(second,first,last)

# len=[]
# k=int(input('请输入比较的数字数目:>'))
# for i in range(k):
#     k=int(input('请逐个输入比较的数字:>'))
#     len.append(k)
# len.sort()
# print('比较后从小到大排序为:'+str(len))
    

# 题目三
#   0   1   1   2   3   5   8   13   21   34    55...
#   a   b  a=a+b
#
a = 0
b = 1
numbers=[0]
number=int(input("请输入斐波那契数列:>"))
for i in range(number):
    # 如果不采用迭代，只是用循环如何实现
    # a,b=b,a+b相当于:
    temp=b#先保存b的原值
    b=a+b#赋b新值
    a=temp#将b的原值赋予a
    numbers.append(a)
print(numbers)
    
    
    
    
    
    
    
    