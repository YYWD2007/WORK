from pathlib import Path
import requests # type: ignore
from pathlib import Path
import json
import pandas as pd
import plotly.express as px

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(url)

path = Path("eq_data/eq_data_last30_days_m1.geojson")
path.write_text(response.text, encoding="utf-8")
try:
    contents = path.read_text()
except:
    contents = path.read_text(encoding="utf-8")

all_eq_data = json.loads(contents)

path = Path("eq_data/readable3_last30days_eq_data.geojson")
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

all_eq_dicts = all_eq_data["features"]
标题 = all_eq_data["metadata"]["title"]
print(len(all_eq_dicts))



rows = []

for info in all_eq_dicts:
    try:
        mag = info["properties"]["mag"]
        if mag is None or mag < 0:
            continue                       # 跳过负值或空值
        row = (
            info["geometry"]["coordinates"][0],  # 经度
            info["geometry"]["coordinates"][1],  # 纬度
            info["properties"]["title"],         # 位置描述
            mag,
            标题
        )
        rows.append(row)
    except (KeyError, TypeError, ValueError):
        # 如果某项数据不完整，跳过
        continue

# 构建 DataFrame
data = pd.DataFrame(rows, columns=["经度", "纬度", "位置", "震级", "标题"])

fig = px.scatter_geo(
    data,
    lon = "经度",
    lat = "纬度",
    labels = {"x":"经度", "y":"纬度"},
    width = 1000,
    height = 1000,
    title = 标题,
    size = "震级",
    size_max = 10,
    color = "震级",
    color_continuous_scale = "reds", # python, import plotly.express as px, px.colors.named_colorscales()
    hover_name = "位置",
    projection="natural earth"
)


fig.update_layout(
    geo=dict(
        showland=True,
        landcolor="rgb(217, 217, 217)",
        showcountries=True,
        countrycolor="rgb(204, 204, 204)",
    ),
    width=1000,
    height=600
)


fig.write_html("global_earthquakes.html")
fig.show()












