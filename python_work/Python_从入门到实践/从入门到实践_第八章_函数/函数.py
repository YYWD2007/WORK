def greet_user():                               #定义一个函数
    print("Hello!")

greet_user()


def greet_user(username):                       #可以给username赋予任何值
    print(f"Hello, {username.title()}.")

greet_user("Jesse")                             #username: parameter, Jesse: argument


#Ex8.1 p117
def display_message(主题):
    print(f"这章的主题是{主题}。")

display_message("函数")

#Ex8.2 p117
def favorite_book(title):
    print(f"One of my favorite books is {title}.")

favorite_book("Alice in Wonderland")









