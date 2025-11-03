def great_users(names):                                #函数+列表
    for name in names:
        message = f"Hello, {name}!\n"
        print(message)
users = ["hannah", "ty", "margot"]                     #给函数parameter赋予一个列表
great_users(users)



unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]  #无函数，列表转移
completed_models = []
while unprinted_designs:
    current_designs = unprinted_designs.pop()
    print(f"Printing model: {current_designs}")
    completed_models.append(current_designs)
print("\nThe following models have been printed: ")
for completed_model in completed_models:
    print(completed_model)

#把列表换成函数
def print_designs(unprinted_designs, completed_models):                #列表转移（函数）
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing model: {current_designs}")
        completed_models.append(current_designs)
unprinted_designs= ["phone case", "robot pendant", "dodecahedron"] 
completed_models = []
print_designs(unprinted_designs[:],completed_models)                    # [:]代表不修改unprinted_designs列表，保留
def printed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)
printed_models(completed_models)

#Ex 8.9 p131
def show_messages(messages):
    for message in messages:
        print(f"\n{message}")
messages = ["Hello!", "Bye!", "Good morning!"]
show_messages(messages)

#Ex 8.10, 8.11 p131
def messages(Show_messages, send_messages):
    while Show_messages:
        t_messages = Show_messages.pop(0)
        send_messages.append(t_messages)
Show_messages = ["Hello!", "Bye!", "Good morning!"]
send_messages = []
messages(Show_messages[:], send_messages)
def M(send_messages):
    for send_message in send_messages:
        print(send_message)
M(send_messages)
for show_message in Show_messages:
    print(show_message)











    

