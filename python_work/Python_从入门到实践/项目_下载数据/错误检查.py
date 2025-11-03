from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("death_valley_2021_simple.csv")      #这个文件在某一天缺少了最大温度的数据，所以生成图的时候会产生错误
lines = path.read_text().splitlines()
reader = csv.reader(lines) 
header_row = next(reader)   
for index, header_row in enumerate(header_row):
    print(index,header_row)   

TMAX, Dates,TMIN = [],[],[]
for row in reader:
    try:
        D = datetime.strptime(row[2],"%Y-%m-%d")
        T = int(row[3])                          #中间有一天没有最高温度，我们要检索错误（Try, except） 
        TM = int(row[4])
    except ValueError:
        print(f"Missing data for {D}")
    else:
        TMAX.append(T)
        Dates.append(D)
        TMIN.append(TM)



plt.style.use("tableau-colorblind10")
fig, ax = plt.subplots(figsize = (9,5))   

ax.plot(Dates, TMAX, linewidth = 1, alpha= 0.5, color="red")         #alpha 表示透明度
ax.plot(Dates, TMIN, linewidth = 1, alpha=0.5, color="blue") 
ax.fill_between(Dates, TMAX, TMIN, facecolor = "blue", alpha=0.1)
ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize = 24)
ax.set_xlabel("Dates",fontsize = 14)
ax.set_ylabel("Temperature (F)", fontsize = 14)
fig.autofmt_xdate()      

ax.tick_params(labelsize=14)            

plt.show()


