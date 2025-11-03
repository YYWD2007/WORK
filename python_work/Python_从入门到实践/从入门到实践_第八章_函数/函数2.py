def describe_pet(animal_type, pet_name):                    #设置函数，两个形参
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet("dog", "harry")                                #根据位置给予实参（位置实参）
describe_pet("hamster", "willie")                           #再次调用函数（换值打印）
describe_pet(animal_type="hamster", pet_name="harry")       #关键字实参，不在乎顺序



def describe_pet(pet_name, animal_type = "cat"):            #默认值，animal_type 被默认为cat, 只需给 pet_name 实参即可     
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name}.")

describe_pet(pet_name="candy")
describe_pet(animal_type="hamster", pet_name="candy")       #给animal_type 提供实参，忽略默认值



#Ex8.3 p122
def make_shirt(尺码, 字样):
    print(f"\n这个T恤的尺码是{尺码}。\n印的字样是‘{字样}’。")

make_shirt("M号", "Good morning")
make_shirt(尺码='M', 字样='Good morning')

#Ex8.4
def make_shirt(尺码, 字样="I love Python"):
    print(f"\n这个T恤的尺码是{尺码}。\n印的字样是‘{字样}’。")

make_shirt("大号")
make_shirt("中号")
make_shirt("小号","Hello!") 

#Ex8.5
def describe_city (名称, 所属国):
    print(f"\n{名称} is in {所属国}.")

describe_city("Reykjavik", "Iceland")

def describe_city (名称, 所属国="China"):
    print(f"\n{名称} is in {所属国}.")

describe_city("Dalian")
describe_city("Fushun")
describe_city("Barcelona", "Spain")







