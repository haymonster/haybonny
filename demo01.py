
#python里的各种数据格式
"""
print("hello world!")   #字符串str
print(2333) #整数int
print(2.333) #小数float
print(()) #元组tuple
print([]) #数组list
print({}) #字典dict
print(True) #布尔值bool
print(False) #布尔值
print(None) #空NoneType
"""

#print用法
"""
print( ( (1+2)*100-99 )/2 ) 
print(2,90,88，uuu)
print("hahaha"+"hehehe")
print("LMAO"*5)
"""




#type用法
#input的用法
#input以字符串类型获取内容，数据格式转换方法

"""
t = 100
print(type(t))

a = input("input a word please:") 
b = input("input another word:")
c = len(a)+len(b) #计算数据长度，只支持字符串、元组、数组、字典
d = int(a)+float(b)
print("the combine is:",c,d)    
"""




#元组,下标，从零开始
"""
a = (1,2,3,"hello","bye","bye",True,False) 
print(a[5]) 
print(a[-1]) 

#切片
print(a[0:4])  #左闭右开
print(a[4:])
print(a[:5])
print(a[:])



print(a.index("hello")) #查找某个值得下标，只能使用在一维元组
print(a.count("bye")) #统计某个值得数量，只能使用在一维元组

#二维元组
b = (a,"joy",555) 
print(b[0][3])
"""

#数组
"""
a = [1,2,3,"hello","bye","bye","joy","sadness",True,False]
print(a[3])

#元组一旦写好不可以修改，而数组可以修改
#元组的优点就是不可以修改
a.append("append") #追加数据
a.insert(0,"insert") #插入数据在下标前面 
b = a.pop(8) #剪切数据

xx = [666,777]
a.extend(xx) #跟append不同，可以将数组里的值追加进去 
print(a+xx) #只能追加数组

a.remove("bye") #删除数据
print(a) 

a.index("joy")
print(a.count(False))

del a[0] #删除通过下标
a.clear() #清空
"""

#字典
#1、字典中的值没有顺序 
#2、字典的结构必须是键值对的结构 key:value
"""
a ={"name":"atom",0:"fun","age":26}
print(a["name"]) #取值，如果没有对应值，代码会报错
a["height"] = "183cm" #新增
a["name"] = "max" #修改

a.get("name") #取值，如果没有对应值，会返回空
b = a.pop(0) #拿走
print(b) 
a.update(weight = "60kg") #更新
print(a) 

del a["name"] #删除通过key
"""

#作业： 获取用户个人信息，并存储到字典中，包括了name，age，sex
a = input("insert a name please: ")
b = input("inset an age please: ")
c = input("insert sex please: ")

custom_info = {"name": a,"age":b,"sex":c}
print(custom_info) 





#作业：录入学生成绩，及格和不及格分开存放

"""
highlevel = {}
lowlevel = {}
aaa = 1 
while aaa <= 5:
    name = input("请输入姓名：")
    score = int(input("请输入成绩："))
    aaa = aaa+1
    if score >= 60:
        highlevel[name] = score 
    else:
        lowlevel[name] = score
print("highlevel:",highlevel)
print("lowlevel:",lowlevel)

"""