def make_pizza(*toppings):                 # '*'加形参可以赋予多个实参
    print(toppings)
make_pizza("pepperoni")
make_pizza("A","B","L")
def make_pizza(*toppings):
    for topping in toppings:
        print(f"- {topping}")
make_pizza("A","B","L")

def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_pizza("12", "mushrooms", "green peppers", "extra cheese")


def profile(first_name, last_name, **user_info):                                        # **代表创造字典
    user_info["f_name"] = first_name                                                    #先将名和姓加入字典
    user_info["l_name"] = last_name
    return user_info
user_profile = profile("Albert", "Einstein", location = "princeton", field = "physics") #赋予对应值，还可多加
print(user_profile)

#Ex8.12 p134
def 三明治(*食材):
    print("\n这个三明治添加了以下食材：")
    for shicai in 食材:
        print(f"- {shicai}")
三明治("蘑菇","芝士","西红柿")

#Ex8.13
def build_profile(first_name, last_name, **user_info):
    user_info["first_name"] = first_name
    user_info["last_name"] = last_name
    return user_info
information = build_profile("Qingbin","Zhou", address="Barcelona", nationality = "China", hobby = "python")  
print(information)
for key,value in information.items():
    print(f"{key}: {value}")

#Ex8.14
def make_car(制造商, 型号, **汽车信息):
    汽车信息["制造商"] = 制造商
    汽车信息["型号"] = 型号
    return 汽车信息
car = make_car("Subaru","Outback",Color="Blue", Tow_package = True)
print(car)
for value in car.values():
    print(value)



