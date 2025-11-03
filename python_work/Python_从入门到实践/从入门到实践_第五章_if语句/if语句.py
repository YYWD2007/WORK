cars=["audi","bmw","subaru","toyota"]
for car in cars:
    if car=="audi":                                   #  == 如果等于
        print(car.title())
    else:
        print(car.upper())
cars=["Audi","bmw","subaru","toyota"]
for car in cars:
    if car.lower()=="audi":
        print(car.upper())
    else:
        print(car.title())


requested_topping="mushrooms"
if requested_topping!="anchovies":                      #  != 是"不等于"
    print("Hold the anchovies")

age_1=22                                                #if语句(or, and)
age_2=18
if age_1>21 or age_2>21:
    print("True")
else:
    print("False")
if age_1>21 and age_2>21:
    print("True")
else:
    print("False")

requested_toppings=["BBB","VVV","PPP"]                  #检查一个东西是否在列表里（if...in..）
if "BBB" in requested_toppings:
    print("Ok")
else:
    print("No")
if "MMM" not in requested_topping:                       #检查是否不在（if...not in...）
    print("不在")
else:
    print("在")


#Ex5.1 p69
name="M"
if name=="Maria":
    print("True")
else:
    print("False")
if name!="Maria":
    print("Not Maria")
else:
    print("Yes")

#Ex5.2 p69
First="1,2,3,4,5"
Second="2,4,5,6,8"
if First==Second:
    print("Oh")
else:
    print("Noooo")
cars=["AUDi","Bmw","suBaru","toyOta"]
for car in cars:
    if car.upper()=="BMW":
        print(car.title())
    else:
        print((car.upper()))


cars2=["aUdi","BmW","suBaRu","toyota"]
cars=["AUDi","Bmw","suBaru","toyOta"]
for car in cars:
    car=car.lower()
for car2 in cars2:
    car2=car2.lower()
if car2==car:
     print("True")
else:
     print("False")




   
   

