requested_toppings=["mushrooms","green peppers","extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping=="mushrooms":
        print("Sorry, we are out of mushrooms right now")
    else:
        print(f"Adding {requested_topping}")

A=[]                                                                 #检查列表是否是空的
if A:
    for B in A:
        print(B)
else:
    print("Nothing")

requested_toppings=["mushrooms","extra cheese","green peppers"]
available_toppings=["mushrooms","extra cheese","pineaplle","olives"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we do not have {requested_topping}")

#Ex5.8 p78
names=["juan","laia","carolina","admin","jaden"]
for name in names:
    if name=="admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {name}， thank you for logging in again.")

#Ex5.9 p79
names=[]
if names:
    for name in names:
        print(name)
else:
    print("We need to find some users!")

#Ex 5.10
current_users=["juan","laia","carolina","admin","jaden"]
new_users=["suarez","laia","Carolina","William","jaden"]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("你的名字已被使用")
    else:
        print("注册成功")

#Ex 5.11
numbers=list(range(1,10))
print(numbers)
for number in numbers:
    print(number)
for number in numbers:
    if number==1:
        print(f"{number}st")
    elif number==2:
        print(f"{number}nd")
    elif number==3:
        print(f"{number}rd")
    else:
        print(f"{number}th")



    




