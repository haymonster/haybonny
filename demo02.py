#判断 注意缩进
"""
a = 1
b = 2

if a == 1:
    print(True)


if a > b :
    print("a比b大")
else:
    print("b更大")

age = int(input("请输入你的年龄："))

if age > 60:
    print("退休了")
elif age > 30:
    print("责任很重吧")
elif age > 20:
    print("一定要好好规划未来")
else:
    print("读书要认真")
"""

#in的用法
"""
xx = "hello"
if xx in "hello, im hayley, nice to see you!":
    print(True)
else:
    print(False)

aa = input("请输入任意年龄：")
if aa = "":
    print("不能为空")
    exit() 

if aa in "0123456789":
    aa = int(aa)
else:
    print("请输入正确的年龄")
    exit() 
"""

# is的用法
"""
bb = {"name":"hay"}
if type(bb) is int:
    print("是数字！")
elif type(bb) is str:
    print("是字符串！")
else:
    print("其他！")
"""

# 循环
# while循环
"""
a = 1
while a < 10:
    print("hahaha",a)
    a = a + 1
"""

#练习：现在有学生的成绩需要录入到系统中，并且名字和成绩需要对应上，而且大于60的和小于60的需要分开存放。
#作业：录入学生成绩，及格和不及格分开存放

#方法1
"""
highlevel = {}
lowlevel = {}
snum = 1 
while snum <= 5:
    name = input("请输入姓名：")
    score = int(input("请输入成绩："))
    snum = snum+1
    if score >= 60:
        highlevel[name]= score 
    else:
        lowlevel[name] = score
print("highlevel:",highlevel)
print("lowlevel:",lowlevel)
"""
#方法2
"""
high = {}
low = {}
studentlist = ["张三","李四","二狗","王麻子","亚索","花花"]
a = 0
while a < len(studentlist):
    score = int(input("请输入"+studentlist[a]+"的成绩："))
    if score >= 60:
        high[studentlist[a]] = score
    else:
        low[studentlist[a]] = score
    a = a + 1
print("high:",high) 
print("low:",low)
"""
# 方法3，利用for循环
"""
high = {}
low = {}
studentlist = ["张三","李四","二狗","王麻子","亚索","花花"]
for i in studentlist:
    score = int(input("请输入"+i+"的成绩："))
    if score >= 60:
        high[i] = score
    else:
        low[i] = score
print("high:",high) 
print("low:",low)
"""

# for循环，遍历
"""
a = "你好，今天你吃了吗？"
for i in a:
    print(i)

# range()，左闭右开
b = list(range(0,100,2)) #自动生成一个数列，步进/步长
print(b)

for i in range(5):
    print(i)
"""

#练习：打印九九乘法表
"""
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+"x"+str(i)+"="+str(i*j),end="  ") #end with 空格，而不是换行
    print() #在这边换行
"""

#练习1：通过print打印，模拟一个红绿灯功能，红灯30次，绿灯35次，黄灯3次。
#方法一
"""
for i in range(1,31):
    print("红灯还有",31-i,"秒")
for j in range(1,36):
    print("绿灯还有",36-j,"秒")
for k in range(1,4):
    print("黄灯还有",4-k,"秒")
"""
#方法二
"""
for i in range(30,0,-1):
    print("红",i,"秒")
for i in range(35,0,-1):
    print("绿",i,"秒")
for i in range(3,0,-1):
    print("黄",i,"秒")
"""
#方法三
"""
light = {"red light":30,"green light":35,"yellow light":3}
for i in light:
    for j in range(light[i]):
        print(i,light[i]-j)
"""


#练习2：使用代码，实现一个注册的功能，用户输入账号和密码，要求账号长度是5~8位，密码6~12位，并且账号必须小写字母开头，储存到字典中{username：password}
"""
userinfo = {}
username = input("请输入账号名：")
while len(username)<5 or len(username)>8 or username[0] not in "qwertyuiopasdfghjklzxcvbnm":
    username = input("账号不符合要求，请重新输入：")
password = input("请输入密码：")
while len(password)<5 or len(password)>12:
    password = input("密码长度不符合要求，请重新输入：")
userinfo[username] = password
print("注册成功!您的账号和密码为：",userinfo)
"""

#循环里continue的用法
"""
for i in range(10):
    if i == 4:
        continue
    print(i) 
"""
#break的用法
"""
for i in range(10):
    if i == 4:
        break
    print(i) 
"""

#函数/方法
#自定义方法


# def checkid(username):
#     """
#     自动判断账号长度是否为5~8位，并且是否为小字母开头。
#     """
#     while len(username)<5 or len(username)>8 or username[0] not in "qwertyuiopasdfghjklzxcvbnm":
#         username = input("账号不符合要求，请重新输入：")
# checkid(input("请输入id："))


#返回值
"""
def combine(a,b):
    if type(a) is int and type(b) is int:
        return a+b
    else:
        return "您输入的数据类型不正确！"
print(combine(8,"j"))  
"""
#练习：定义一个方法，用来判断用户输入的账号密码是否符合规范。
"""
userinfo = {}
def check(username,password):
    while len(username)<5 or len(username)>8 or username[0] not in "qwertyuiopasdfghjklzxcvbnm":
        username = input("账号不符合要求，请重新输入：")
    while len(password)<5 or len(password)>12:
        password = input("密码长度不符合要求，请重新输入：")
    return username,password
a = check(input("请输入id："),input("请输入密码："))
userinfo[a[0]] = a[1]
print("注册成功!您的账号和密码为：",userinfo)
"""