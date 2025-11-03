age=18
if age>=18:
    print("You are old enough to vote!")
else:
    print("Sorry, you are too young to vote.")


age=18
if age<4:
    price="0"
elif age<18:                                               #可多次使用elif
    price="10"
else:
    price="11"
print(f"Your admission cost is ${price}.")

age=18
if age<4:
    price="0"
elif age<18:                                             
    price="10"
elif age>=18:                                               #elif 可以代替 else
    price="11"
print(f"Your admission cost is ${price}.")

#if-elif-else 语句只能在有一个代码块时运行，有列表的时候if...in 不能elif...in 

#Ex 5.3，Ex5.4 p75
alien_color=["green","yellow","red"]
玩家消灭的="red"
if 玩家消灭的=="green":
    print("你获得了五分.")
else:
    print("你获得了十分.")
#Ex 5.5
if 玩家消灭的=="green":
    print("你获得了5分")
elif 玩家消灭的=="yellow":
    print("你获得了10分")
else:
    print("你获得了15分.")

#Ex 5.6
age=18
if age<2:
    print("这个人是婴儿")
elif age>=2 and age<4:
    print("这个人是幼儿")
elif age>=4 and age<13:
    print("这个人是儿童")
elif age>=13 and age<18:
    print("这个人是少年")
elif age>=18 and age<65:
    print("这个人是中青年人")
else:
    print("这个人是老年人")

#Ex 5.7
favorite_fruits=["apple","orange","watermelon"]
if "bananas" in favorite_fruits:
    print("You really like bananas.")
if "apple" in favorite_fruits:
    print("You really like apples.")
















