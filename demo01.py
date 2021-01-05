
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