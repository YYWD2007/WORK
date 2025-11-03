def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()                                   #返回标准格式
musician = formatted_name("jimi", "hendrix")
print(musician)

def formatted_name(first_name, middle_name, last_name):
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()                                 
musician = formatted_name("jimi", "Lee", "hendrix")
print(musician)


def formatted_name(first_name, last_name,  middle_name = ""): #初始把中间名设置成无
    if middle_name:                                           #如果这个人有中间名，则赋予argument
        full_name = f"{first_name} {middle_name} {last_name}"
    else:                                                     #若没有中间名，就默认为无
        full_name = f"{first_name} {last_name}"
    return full_name.title()                                 
musician = formatted_name("jimi", "hendrix", "Lee")           #Jimi Lee Hendrix
print(musician)
musician = formatted_name("jimi", "hendrix")                  #Jimi Hendrix
print(musician)


def build_person(first_name, last_name):
    person={"first":first_name, "last":last_name}             #函数+字典
    return person
musician = build_person("jimi", "hendrix")
print(musician)

def build_person(first_name, last_name, age=None):            # None 代表没有数值
    person= {"first":first_name, "last":last_name}
    if age:                                                   #如果有age值, 加到字典中
        person["age"]=age
    return person
musician= build_person("jimi", "hendrix", "29")               
print(musician)                                               #{'first': 'jimi', 'last': 'hendrix', 'age': '29'}



def formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title() 
while True:
    print("\nPlease tell me your name.")
    print("(enter 'q' at any time to quit)")
    f_name= input("First name: ")
    if f_name == "q":
        break
    l_name= input("Last name: ")                              #到这里是无限循环(输入q终止)，一直输入名字
    if l_name == "quit":
        break
    person =formatted_name(f_name, l_name)
    print(f"\nHello, {person}!")
   


#Ex8.6 p127
def city_country(name, county):
    result = f'"{name}, {county}"'
    return result.title()
message = city_country("Santiago", "Chile")
print(message)

#Ex8.7
def make_album(name_singer, name_album):
    album = {"Name of the singer":name_singer, "Name of the album":name_album}
    return album
information = make_album("Dua Lipa", "Future Nostalgia")
print(information)

#Ex8.8
def make_album(name_singer, name_album):
    album = {"Name of the singer":name_singer, "Name of the album":name_album}
    return album
while True:
    print("\nPlease introduce the information.")
    print("(enter 'q' to quit)")
    Name_of_the_singer = input("Name of the singer: ")
    if Name_of_the_singer == "q":
        break
    Name_of_the_album = input("Name of the album: ")
    if Name_of_the_album == "q":
        break
    information = make_album(Name_of_the_singer, Name_of_the_album)
    print(information)








 
