from pathlib import Path
import json
import plotly.express as px
import pandas as pd

path = Path("eq_data/eq_data_30_day_m1.geojson")
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding="utf-8")

all_eq_data = json.loads(contents)

path = Path("eq_data/readable2_eq_data.geojson")  # 创建新的文件路径（准备保存格式化后的数据）
readable_contents = json.dumps(all_eq_data, indent=4)  #indent 参数的意思是 “缩进”
path.write_text(readable_contents)   # 将格式化后的 JSON 数据写入新文件

all_eq_dicts = all_eq_data["features"]
print(len(all_eq_dicts))

地震级别, 地点, 经度, 纬度 = [],[],[],[]
for info in all_eq_dicts:
    级别 = info["properties"]["mag"]
    方位 = info["properties"]["title"]
    经 = info["geometry"]["coordinates"][0]
    纬 = info["geometry"]["coordinates"][1]
    地震级别.append(级别)
    地点.append(方位)
    经度.append(经)
    纬度.append(纬)

print(地震级别[:10])
print(地点[:2])
print(经度[:5])
print(纬度[:5])

data = pd.DataFrame(data = zip(经度, 纬度, 地点, 地震级别), columns= ["经度","纬度","位置","震级"])
data.head()

fig = px.scatter(
    data,
    x = "经度",
    y = "纬度",
    labels = {"x":"经度", "y":"纬度"},
    range_x = [-200,200],
    range_y =[-90,90],
    width = 800,
    height = 800,
    title = "全球地震散点图",
    size = "震级",
    size_max = 10,
    color = "震级",
    color_continuous_scale = "blues", # python, import plotly.express as px, px.colors.named_colorscales()
    hover_name = "位置"
)


fig.write_html("global_earthquakes.html")
fig.show()

