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
标题 = all_eq_data["metadata"]["title"]
print(len(all_eq_dicts))

data = pd.DataFrame(
    [
        (
            info["geometry"]["coordinates"][0],
            info["geometry"]["coordinates"][1],
            info["properties"]["title"],
            info["properties"]["mag"],
            标题
        )
        for info in all_eq_dicts
    ],
    columns=["经度", "纬度", "位置", "震级","标题"]
)

fig = px.scatter(
    data,
    x = "经度",
    y = "纬度",
    labels = {"x":"经度", "y":"纬度"},
    range_x = [-200,200],
    range_y =[-90,90],
    width = 800,
    height = 800,
    title = 标题,
    size = "震级",
    size_max = 10,
    color = "震级",
    color_continuous_scale = "blues", # python, import plotly.express as px, px.colors.named_colorscales()
    hover_name = "位置"
)


fig.write_html("global_earthquakes.html")
fig.show()

