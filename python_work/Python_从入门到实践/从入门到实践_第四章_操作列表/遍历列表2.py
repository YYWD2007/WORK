players=["charles","martina","michael","florence","eli"]
print(players[1:3])                                        #打印部分列表['martina', 'michael']
print(players[2:4])
print(players[:5])
print(players[2:])
print(players[-3:])
print(players[0:5:2])                                      #[]里三个数值，跳着打印

for player in players[1:3]:                                #for循环打印部分名字
    print(player)

my_foods=["pizza","falafel","carrot cake"]
friend_foods=my_foods[:]                                   #复制列表
friend_foods.append("ice cream")
print(friend_foods)
print(my_foods)

#Ex4.10 p57
players=["charles","martina","michael","florence","eli"]
print("The first three items in the list are:")
print(players[0:3])
print("Three items from the middle of the list are:")
print(players[1:-1])
print("The last three items in the list are:")
print(players[2:])

#Ex4.11 
Pizzas=["Margherita","Hawaiian","Pepperoni"]
friend_pizzas=Pizzas[:]
Pizzas.append("D")
friend_pizzas.append("S")
print("My favorite pizzas are:")
for Pizza in Pizzas:
    print(Pizza)
print("My friend's favorite pizzas are:")
for Pizza in friend_pizzas:
    print(Pizza)



