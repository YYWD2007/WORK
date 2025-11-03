from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path("sitka_weather_2021_simple.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines) 
header_row = next(reader)      

TMAX, Dates,TMIN = [],[],[]
for row in reader:
    T = int(row[4])
    D = datetime.strptime(row[2],"%Y-%m-%d") 
    TM = int(row[5])
    TMAX.append(T)
    Dates.append(D)
    TMIN.append(TM)



plt.style.use("tableau-colorblind10")
fig, ax = plt.subplots(figsize = (9,5))   

ax.plot(Dates, TMAX, linewidth = 1, alpha= 0.5, color="red")         #alpha 表示透明度
ax.plot(Dates, TMIN, linewidth = 1, alpha=0.5, color="blue") 
ax.fill_between(Dates, TMAX, TMIN, facecolor = "blue", alpha=0.1)
ax.set_title("Daily High and Low Temperatures, 2021", fontsize = 24)
ax.set_xlabel("Dates",fontsize = 14)
ax.set_ylabel("Temperature (F)", fontsize = 14)
fig.autofmt_xdate()      

ax.tick_params(labelsize=14)            

plt.show()


