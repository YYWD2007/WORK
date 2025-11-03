message=input("Tell me something, and i will repeat it back to you:")           #要求输入信息
print(message)
name=input("Please enter your name:")
print(f"Hello, {name}")

prompt="If you share your name, we can personaliza the messages you see."       #将问题设置成变量，再用input
prompt+="\nWhat is your first name? "
name=input(prompt)
print(f"\nHello, {name}")
