dimensions=(500,2)                        #元组是无法修改的列表
print(dimensions)
print(dimensions[0])
for dimension in dimensions:              #dimensions的for循环，输出所有数值
    print(dimension)

#Ex4.13 p59
foods=("De","Fe","Ve","Ee","Re","Pe")
for food in foods:
    print(food)
#foods[0]="LO"............................不可更改，Error 
print("Original menu:")
for food in foods:
    print(food)
print("Modified Menu:")
New=("De","Fe","MK","OP","Re","Pe")
for N in New:
    print(N)



