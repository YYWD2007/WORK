class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

Car1 = Car("audi", "a4", "2024") 
print(Car1.get_descriptive_name())                                             #执行加打印
Car1.odometer_reading = 23                                                     #此处可修改默认键
Car1.read_odometer()




class Car:
    def __init__(self, make, model, year, odometer_reading = 0):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer_reading
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def update_odometer(self, mileage):                                #无视默认键，自设值
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:                                                          #值不可小于默认值
            print("You can not roll back an odometer!")
        print(f"This car has {self.odometer_reading} miles on it.")   
    def increment_odometer(self, increment):                           # mileage加上多跑的
            self.odometer_reading += increment
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")                                     

Car1 = Car("audi", "a4", "2024") 
print(f"\n{Car1.get_descriptive_name()}")                                         
Car1.update_odometer(23500)
Car1.increment_odometer(100)
Car1.read_odometer()



#Ex9.4 
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








