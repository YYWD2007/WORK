height=input("How tall are you, in inches? ")
height=int(height)                                                           #当需要输入数字并比较时，用int
if height>=48:
    print("\nYou are tall enough to ride!")
else:
    print("\nYou will be able to ride when you are a little older.")



number=input("Enter a number, and i will tell you is it is even or odd: ")
number=int(number)
if number % 2 == 0:                                                          #  % 代表余数
    print(f"\nTHe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

#Ex 7.1 p105
car=input("\n你想要什么车? ")
print(f"Let me see if i can find you a {car}.")

#Ex 7.2 p105
question=input("\n几个人? ")
question=int(question)
if question>8:
    print("没有空桌了")
else:
    print("有空桌")

#Ex 7.3
number=("\n我会告诉你是不是10的倍数,")
number+=("\n请输入: ")
number=input(number)
number=int(number)
if number % 10 == 0:
    print("这是10的倍数。")
else:
    print("这不是10的倍数。")






