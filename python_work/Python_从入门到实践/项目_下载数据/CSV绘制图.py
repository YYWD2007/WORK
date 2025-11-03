from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

first_date = datetime.strptime("2021-07-01", "%Y-%m-%d")


path = Path("sitka_weather_07-2021_simple.csv")
lines = path.read_text().splitlines()

reader = csv.reader(lines)      #解析文件的每一行
header_row = next(reader)       #next会一行一行地“吐出” CSV 表格中的内容。第一次调用 next(reader)：返回第一行（也就是表头）

for index,name in enumerate(header_row):
    print(index,name)

TMAX, Dates = [],[]
for row in reader:
    T = int(row[4])
    D = datetime.strptime(row[2],"%Y-%m-%d") 
    TMAX.append(T)
    Dates.append(D)



plt.style.use("tableau-colorblind10")
fig, ax = plt.subplots(figsize = (9,5))   

ax.plot(Dates, TMAX, linewidth = 3) 

ax.set_title("Daily High Temperatures, July 2021", fontsize = 24)
ax.set_xlabel("Dates",fontsize = 14)
ax.set_ylabel("Temperature (F)", fontsize = 14)
fig.autofmt_xdate()      #斜制标签

ax.tick_params(labelsize=14)            

plt.show()


