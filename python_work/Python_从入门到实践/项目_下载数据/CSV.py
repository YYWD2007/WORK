from pathlib import Path
import csv

path = Path("sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)      #解析文件的每一行
header_row = next(reader)       #next会一行一行地“吐出” CSV 表格中的内容。第一次调用 next(reader)：返回第一行（也就是表头）

for index,name in enumerate(header_row):
    print(index,name)

TMAX = []
for row in reader:
    T = int(row[4]) 
    TMAX.append(T)
print(f"TMAX:{TMAX}")

Day = []
for row in reader:
    D = int(row[2]) 
    Day.append(D)
print(f"TMAX:{Day}")


