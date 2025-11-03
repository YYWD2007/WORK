alien_0={"color":"green","points":5}               #储存信息
print(alien_0["color"])
print(alien_0["points"])
new_points=alien_0["points"]
print(f"You just earned {new_points} points!")
alien_0={"color":"green","points":5}
alien_0["x_position"]=0                            #添加位置，额外信息
alien_0["y_position"]=25
print(alien_0)

alien_0={}                                         #创造空字典，再添加
alien_0["color"]="green"
alien_0["points"]=5
print(alien_0)

alien_0={"color":"green","points":5}
alien_0["color"]="red"                             #修改字典内的信息
print(alien_0)

alien_0={"x_position":0,"y_position":25,"speed":"fast"}         #位置根据速度移动
print(f"original position: {alien_0["x_position"]}")
print(f"Speed: {alien_0["speed"]}")
if alien_0["speed"]=="slow":
    x_increment=1
elif alien_0["speed"]=="medium":
    x_increment=2
else:
    x_increment=3
alien_0["x_position"]=alien_0["x_position"]+x_increment
print(f"New position: {alien_0["x_position"]}")

alien_0={"x_position":0,"y_position":25,"speed":"fast"}        #删除字典信息（键值对）
del alien_0["speed"]
print(alien_0)

favorite_languages={                                           #统计字典
                    "jen":"python",
                    "sarah":"c",
                    "edward":"rust",
                    "phil":"python",
                    }        
print(f"Sarah's favorite language is {favorite_languages['sarah']}.")

alien_0={"color":"green","speed":"medium"}
point_value=alien_0.get("points","No point value assigned")   #如果字典中有points，将会获得。如果没用，显示句子，不会触发错误。
print(point_value)


#Ex6.1, 6.2 p88
information_juan={"first_name":"juan","last_name":"perez","age":24,"city":"paris"}
print(information_juan["first_name"])
print(information_juan["last_name"])
print(information_juan["age"])
print(information_juan["city"])
print(f"first name: {information_juan["first_name"]}")
print(f"last name: {information_juan["last_name"]}")
print(f"age: {information_juan["age"]}")
print(f"city: {information_juan["city"]}")

#Ex 6.3
编程术语={"del":"删除数值","if":"如果","append":"添加","remove":"更改","f":"组合"}
print(f"del: {编程术语["del"]}")
# .../...













