magicians=["alice","david","carolina"]
for name in magicians:                                      #for循环打印名字
    print(name)
magicians=["alice","david","carolina"]
for name in magicians:
    print(f"{name.title()}, that was a great trick!")       #缩进代表循环执行，不缩进只执行一次
print("Thank you, everyone. That was a great magic show!")

#Ex4.1 p48
Pizzas=["Margherita","Hawaiian","Pepperoni"]
for pizza in Pizzas:
    print(pizza)
    print(f"I like {pizza} pizza.")
print("I really like pizza!")

# Ex4.2 p49
Animals=["狗","猫","仓鼠"]
for animal in Animals:
    print(animal)
    print(f"{animal}可以是很好的宠物。")
print("这些动物都可以是很好的宠物")



for number in range(1,5):                                  #for循环输出数字
    print(number)
for number in range(9):
    print(number)

numbers=list(range(1,5))                                   #输出数字列表
print(numbers)
偶数=list(range(2,11,2))
print(偶数)

squares=[]                                                 #输出1-10的平方（列表形式）方法 1
for number in range(1,11):
    square=number**2
    squares.append(square)
print(squares)                                             #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares=[]                                                 # 方法 2
for number in range(1,11):
    squares.append(number**2)
print(squares)

squares=[number**2 for number in range(1,11)]              #方法 3
print(squares)

digitals=[1,2,3,4,5,6,7,8,9]                              #找出最大，最小，相加数值
print(min(digitals))
print(max(digitals))
print(sum(digitals))


#Ex 4.3 p52
for number in range(1,21):
    print(number)

#Ex 4.4 
数字=[]
for number in range(1,1000001):
    数字.append(number)
print(数字)

#Ex 4.5
print(min(数字))
print(max(数字))
print(sum(数字))

#Ex 4.6
奇数=[]
for number in range(1,20,2):
    奇数.append(number)
print(奇数)
奇数=list(range(1,20,2))
print(奇数)
for N in 奇数:
    print(N)

#Ex4.7 p53
三的倍数=list(range(3,31,3))
for N in 三的倍数:
    print(N)

#Ex4.8 
立方=[]
for N in range(1,11):
    立=N**3
    立方.append(立)
print(立方)
for M in 立方:
    print(M)

#Ex4.9
立方=[]
for M in range(5,15):
    N=M**3
    立方.append(N)
print(立方)




