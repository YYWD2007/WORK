from pathlib import Path
path = Path("programming.txt")
path.write_text("I love programming.")  #向另一个文件输入信息

from pathlib import Path
content = "\nI love..."
content += "\nI love creating..."
content += "\nI love working..."
path = Path("programming.txt")
path.write_text(f"I love programming.{content}")

#Ex10.4
name = input("输入你的名字：")
from pathlib import Path
path = Path("guest_book.txt")
path.write_text(f"Name: {name}")

#Ex10.5
from pathlib import Path
path = Path("guest_book.txt")
while True:
    N = input("输入你的名字：")  
    with path.open(mode="a") as file:   # a = append  不会覆盖原内容
        file.write(f"\nName: {N}")








