try:
    print(5/0)                                #尝试这个，并且避免除0的错误
except ZeroDivisionError:
    print("You can not divide by zero")







print("Give me two numbers, and I will divide them.") 
print("Enter 'q' to quit.")
while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    N_1 = int(first_number)
    N_2 = int(second_number)
    Result = N_1/N_2                         #如果N_2 = 0 会引发错误
    print(Result)

#制止错误的发生，加入Try,except:

print("Give me two numbers, and I will divide them.") 
print("Enter 'q' to quit.")
while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    N_1 = int(first_number)
    N_2 = int(second_number)
    try:
        print(N_1/N_2)
    except ZeroDivisionError:
        print("You can not divide by zero")







#from pathlib import Path
#path = Path("alice.py")
#contents = path.read_text(encoding="utf-8")               #当你读写包含中文或其他非英语字符的文本文件时，加上 encoding="utf-8" 可以避免乱码。

#并不存在alice.py这个文件，所以会引发错误。

#改进(防止出现错误):
from pathlib import Path
path = Path("alice.py")
try:
    contents = path.read_text(encoding="utf-8")
except FileNotFoundError:
    print("\n找不到此文件")
else:                         #如果存在这个文档
    words = contents.split()  #之前的splitline是分行，split是分单词
    num_words = len(words)    #len计算单词数量(长度)
    print(num_words)

#设置函数（简化)：
from pathlib import Path
def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("\n找不到此文件")
    else:                         
        words = contents.split()  
        num_words = len(words)    
        print(num_words)
path = Path("alice.txt")
count_words(path)

#测试多个文档：
from pathlib import Path
def count_words(path):
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("\n找不到此文件")                                 #这里可以写 pass, 这样如果找不到文件不会有任何操作
    else:                         
        words = contents.split()  
        num_words = len(words)    
        print(f"\n{num_words}")
filenames = ["alice.txt", "siddhartha.txt", "moby_dick.txt"]      
for filename in filenames:
    path = Path(filename)
    count_words(path)







 #Ex 10.6, 10.7 p180
print("给我两个数字，我会加起来。") 
print("输入q退出。")
while True:
    first_number = input("First number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        print(int(first_number) + int(second_number))
    except ValueError:                                   #可以先引发错误就能看见错误的类型了， 这里是ValueError（必须输入数字）
        print("要全部输入数字!!!")
        
#Ex10.8
from pathlib import Path

def name(path):
    try:
        contents = path.read_text(encoding="utf-8")
        print(f"{path.name} 内容如下：")
        print(contents)
    except FileNotFoundError:
        print(f"{path.name} 文件不存在。")

# 分别处理 cats.txt 和 dogs.txt
cat_path = Path("cats.txt")
dog_path = Path("dogs.txt")

name(cat_path)
name(dog_path)

    



line="row,row,row,Row"
N = line.lower().count("row")
print(N)





