from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

path = Path ("sitka_weather_2021_full.csv")
lines = path.read_text().splitlines()
reader = csv.reader(lines)
header_row = next(reader)
for index, header_row in enumerate(header_row):
    print(index, header_row)

PRCP, Date = [], []
for row in reader:
    try:
        D = datetime.strptime(row[2],"%Y-%m-%d")
        P = float(row[5])
    except ValueError:
        print(f"Missing data for {D}")
    else:
        PRCP.append(P)
        Date.append(D)


plt.style.use("tableau-colorblind10")
fig, ax = plt.subplots(figsize = (9,5))   

ax.bar(Date, PRCP, linewidth = 2, alpha= 0.5, color="blue")         #alpha 表示透明度
ax.set_title("Rainfall in Sitka, 2021", fontsize = 24)
ax.set_xlabel("Dates",fontsize = 14)
ax.set_ylabel("Rainfall(inches)", fontsize = 14)
fig.autofmt_xdate()      

ax.tick_params(labelsize=14)            

plt.show()



