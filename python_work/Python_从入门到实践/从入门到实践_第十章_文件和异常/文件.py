from pathlib import Path           # pathlib 可以是一个“文件夹模块”，里面放着所有跟路径处理有关的功能文件。
                                   # 从 Python 标准库模块 pathlib 中导入一个叫 Path 的类
文件 = Path("pi_digits.txt")       
contents = 文件.read_text()        # 读取这个文本文件里的所有内容
print(contents)

#相对路径 - 在本运行文件中寻找
#绝对路径 - 从根源寻找



from pathlib import Path         
                                   
文件 = Path("pi_digits.txt")       
contents = 文件.read_text()        
lines = contents.splitlines()    #把内容按“行”分开
print(lines)                     #['3.1415926535 ', '  8979323846 ', '  2643383279']

pi = ""                          #使用pi_digits.txt 的内容
for line in lines:
    pi += line.strip()
print(pi)
print(len(pi))


from pathlib import Path         
                                   
文件 = Path("pi_million_digits.txt")       #百万数值 
contents = 文件.read_text()        
lines = contents.splitlines()     

pi = ""                          
for line in lines:
    pi += line.strip()
print(pi[:52])

birthday = input("输入生日日期(例如: 150807): ")
if birthday in pi:
    print("你的生日日期在圆周率里!")
else:
    print("你的生日日期不在圆周率里。")


#Ex10.1 p170
from pathlib import Path
path = Path("learning_python.txt")
content = path.read_text()
print(content)
content = content.strip()
lines = content.splitlines()
print(lines)
for line in lines:
    print(line)

#Ex10.2 
from pathlib import Path
path = Path("learning_python.txt")
content = path.read_text()
lines = content.splitlines()
for line in lines:
    message = line[0:]
    message = message.replace("Python","C")       #replace只支持字符串，不支持替代列表里的词，所以要先列出来再替代
    print(message)

#Ex10.3 
from pathlib import Path
path = Path("learning_python.txt")
content = path.read_text()
for line in content.splitlines():                 #可省略lines变量
    message = line[0:]
    message = message.replace("Python","C")     
    print(message)







  
            
