print("\tpython")
print("Languages:\nPython\nC\nJavaScript")

s = "hello!!!"
print(s.rstrip("!"))  # 输出: "hello"

M="\tpython"
print(M.strip("\t"))
message=" py "
print(message.strip())

#strip删空白，标点..._lstrip删前_rstrip()删后

#ex2.7 p21
Name="\teric\n"
print(Name)
print(Name.lstrip("\t").rstrip("\n"))
print(Name.strip("\t\n"))




