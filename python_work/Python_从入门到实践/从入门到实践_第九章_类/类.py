class Dog:                                        #所有狗...
    def __init__(self, name, age):                #self 代表所有狗
        self.name = name 
        self.age = age                            #这些狗有名和姓

    def info1(self):
        print(f"\nThis dog is called {self.name}.")    

    def info2(self):
        print(f"{self.name} is {self.age} years old.")

    def sit(self):                                #这些狗执行的行动
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

  
dog1 = Dog("Willie", 6)  
dog1.info1() 
dog1.info2()
dog1.sit()
dog1.roll_over()

dog2 = Dog("Lucy", 3)
dog2.info1() 
dog2.info2()
dog2.sit()
dog2.roll_over()



#Ex9.1 p144
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisuine_type = cuisine_type
    def description(self):
        print(f"\nThis restaurant is called {self.name}, its cooking style is {self.cuisuine_type}.")
    def open(self):
        print(f"{self.name} is in business.")
R1 = Restaurant("R1", "Chinese cuisine")
R1.description()
R1.open()

#Ex9.3
class User:
    def __init__(self, first_name, last_name, greetings = f"Hello, "):
        self.first_name = first_name
        self.last_name = last_name
        self.greetings = greetings
    def describe_user(self):
        print(f"\n用户名为 {self.first_name} {self.last_name}.")
    def greet_user(self):
        print(f"{self.greetings}{self.first_name} {self.last_name}!")
User_1 = User("Qingbin","Zhou")
User_1.describe_user()
User_1.greet_user()















