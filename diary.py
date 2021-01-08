#文件的读写
import time
now = time.strftime("%y-%m-%d %H:%M:%S")
text = input("请输入今天的心情：")
with open("D:\日记.txt","a",encoding="utf8") as f:
    f.write(text+"\t"+now+"\n")
    f.write("-------------------------------\n")

#python的制表符：\t  \n