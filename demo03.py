#异常捕获
"""
try:
    print("1"+2)
except:
    print("上面的代码写错了")
"""
#异常类
"""
try:
    print("1"+2)
except Exception as e:
    print("上面的代码写错了",e)
"""
#异常捕获可以这么用
"""
a = input("请输入你的名字：")
b = input("请输入你的年龄：")
try:    
    if int(b) > 18:
        print(a,"成年了")
    else:
        print(a,"未成年")
except:
    print("请输入正确的年龄！")
"""
# 包 -> 自带的、第三方的，很多模块可以组成包
# 第三方包使用法：pip install 包名、pip uninstall 包名、pip list
# 常用的第三方的包：pymysql\selenium\appium\requests\xlrd\xlwt
import time
import random
import pymysql
"""
for i in range(10):
    time.sleep(1)      #利用自带的time包里的sleep，实现隔一秒打印
    print(i)  

a = random.randint(100,1000)   #利用自带的random包里的randint，实现打印随机数
print(a)  

db = pymysql.connect(host="127.0.0.1",user="root",password="",db="hayley_test") #利用安装的第三方包pymysql，连接到本地数据库，调取数据库内容
cur = db.cursor()
try:
    cur.execute("select * from t_student;")
    res = cur.fetchall()
    print(res) 
except:
    print("sql语句错误！")
"""

# 模块 -> py文件就是模块

# 类 -> 类的名字首字母需要大写
# 面向对象编程
# 类里面所有的方法，都必须要传一个参数，叫self
"""
class GirlFriend():
    def __init__(self,sex,high,weight,hair,age):
        self.sex = sex
        self.high = high
        self.weight = weight
        self.hair = hair
        self.age = age
    
    def talent(self,num):
        print("你身高为"+self.high+"体重为"+self.weight+"头发"+self.hair+"的"+self.sex+"朋友：",end="")
        if num == 1:
            print("she can draw")
        elif num == 2:
            print("she can sing")
        else:
            print("she can cook")
    
    def personality(self):
        print("你身高为"+self.high+"体重为"+self.weight+"头发"+self.hair+"的"+self.sex+"朋友：",end="")
        print("she is smart and nice, and funny!")

    def work(self):
        print("你身高为"+self.high+"体重为"+self.weight+"头发"+self.hair+"的"+self.sex+"朋友是一名：",end="")
        print("designer")

class House():
    def __init__(self,city,spot,scale,style):
        self.city = city
        self.spot = spot
        self.scale = scale
        self.style = style
    
    def people(self):
        print("you own the house but you live with your lovely girlfriend")
    
    def pet(self):
        print("you have one dog and one cat")
    
#类的实例化
halen = GirlFriend("femal","169cm","55kg","short","24")
halen.talent(1)
halen.work()
print(halen.high) 
halen.personality()

dream = House("杭州","滨江繁华区能从窗户看到美丽的钱塘江风景","三室两卫一厅","干净整洁性冷淡")
dream.people()
#类的继承
#重写、多态
class Friend(GirlFriend):   #括号里是父类，类名是子类
    def work(self):
        print("software engineer")
friend = Friend("女","160","50","long","25")
friend.work()
#祖宗类 object：重写__init__ 
"""
# 方法 -> 变量
