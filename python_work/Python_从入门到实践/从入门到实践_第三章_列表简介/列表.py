bicycles=["trek",'redline',"specialized"]  #列表[]
print(bicycles)

print(bicycles[0])   #访问列表元素, trek
print(bicycles[0].title())    #Trek
#位置（索引）从0开始，不是1

print(bicycles[-1])    #访问最后一个元素，-2返回倒数第二个

message=f"My first bicycle was a {bicycles[2]}"
print(message)


bicycles[0]="AAA"       #更改元素 ['AAA",'redline','specialized']
print(bicycles)

bicycles[0]="trek"
bicycles.append('AAA')   #添加元素（末尾）
print(bicycles)
bicycles=[]               #创建空列表，再添加
bicycles.append("trek")
bicycles.append("redline")
print(bicycles)

bicycles=["trek",'redline',"specialized"] 
bicycles.insert(1,"AAA")                           #添加元素（随意位置）
print(bicycles)

bicycles=["trek",'redline',"specialized"] 
del bicycles[0]                                    #删除元素（随意位置），不能再使用
print(bicycles)

bicycles=["trek",'redline',"specialized"] 
popped_bicycle=bicycles.pop()                      #删除元素（末尾）
print(bicycles)
print(popped_bicycle)                              #但是还能使用， specialized
bicycles=["trek",'redline',"specialized"]          
last_owned=bicycles.pop()                          #我最后买的=删除最后一个
print(f"The last motorcycle i owned was a {last_owned.title()}")

bicycles=["trek",'redline',"specialized"]
popped_bicycle=bicycles.pop(1)                     #删除元素，还能用，任意位置
print(bicycles)
print(popped_bicycle)                              #重现，redline

bicycles=["trek",'redline',"specialized"]
bicycles.remove("redline")                         #删除元素（不知道位置，知道名称）
print(bicycles)
bicycles=["trek",'redline',"specialized"]
Best="trek"                                        #先设成变量再remove, 还可以使用
bicycles.remove("trek")
print(bicycles)
print(Best)



#Ex3.4-3.7 p36
People=["James","John","David","Robert","Daniel"]
print(People)
Message=f"{People[0]}, 你可以来一起共进晚餐吗？"
print(Message)
Message=f"{People[-2]}, 你可以来一起共进晚餐吗？"
print(Message)
print(f"{People[2]}无法赴约")
People[2]="William"        #David无法赴约，替换
print(People)
Message=f"{People[2]}, 你可以来一起共进晚餐吗？"
print(Message)
People.insert(0,"Richard")
print(People)
People.insert(2,"AAA")
print(People)
People.append("BBB")
print(People)
print("我只能邀请两位共进晚餐")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")
popped_People=People.pop(-1)
print(People)
print(f"抱歉{popped_People}，我无法邀请你了")  #只剩两个人
print(f"{People[0]}和{People[1]}你们依然在我的邀请列表里面")
print("晚餐取消了")
del People[0]    
del People[0]
print(People)
