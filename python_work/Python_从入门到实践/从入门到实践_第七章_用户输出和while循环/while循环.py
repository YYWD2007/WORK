number = 1
while number <= 5:                               #一直while循环，直到不满足条件
    print(number)
    number += 1                                  #number 等于原数加一的缩写 (number=number+1 )

prompt=("\nTell me something, and i will repeat it back to you: ")
prompt+=("\nEnter 'quit' to end the program  ")
M=input(prompt)
while M != "quit":
    M=input(prompt)
    if M != "quit":
        print(M)



prompt=("\nTell me something, and i will repeat it back to you: ")
prompt+=("\nEnter 'quit' to end the program  ")
active=True                                                                #当要设置很多条件使while循环终止时，将True设成active.
while active:
    message = input(prompt)
    if message == "quit":
        active = False                                                     #设置条件，如果是quit，active=false，终止循环，可以添加更多条件
    else:
        print(message)



prompt=("\nTell me something, and i will repeat it back to you: ")
prompt+=("\nEnter 'quit' to end the program  ")
while True:
    Message=input(prompt)
    if Message == "quit":
        break                                                              #利用break直接结束while循环
    else:
        print(Message)





