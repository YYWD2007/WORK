cars=["bmw","audi","toyota","subaru"]
cars.sort()                                    #列表排序(字母正序)(永久) ['audi', 'bmw', 'subaru', 'toyota']
print(cars)
cars.sort(reverse=True)                        #列表排序（字母倒序）（永久）['toyota', 'subaru', 'bmw', 'audi']
print(cars)

cars=["bmw","audi","toyota","subaru"]
print(cars)
print(sorted(cars))                            #列表排序（字母）（临时） 可返回
print(cars)
print(sorted(cars,reverse=True))   

cars=["bmw","audi","toyota","subaru"]
cars.reverse()                                 #排序，反过来
print(cars)
cars.reverse()
print(cars)


cars=["bmw","audi","toyota","subaru"]         
print(len(cars))                                 #列表长度，这里是4


#Ex3.8-Ex3.9 p39
Places=["Paris","Kyoto","Rome","New York City","Santorini"]
print(Places)
print(sorted(Places))
print(Places)
print(sorted(Places,reverse=True))
print(Places)
Places.reverse()
print(Places)
Places.reverse()
print(Places)
Places.sort()
print(Places)
Places.sort(reverse=True)
print(Places)
Places=["Paris","Kyoto","Rome","New York City","Santorini"]
print(len(Places))
print(f"我将要去{len(Places)}个地方")
















