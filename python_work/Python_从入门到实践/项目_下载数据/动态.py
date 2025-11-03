import pandas as pd
import plotly.graph_objects as go
import requests


url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson"
response = requests.get(url)
data_json = response.json()

rows = []
for feature in data_json["features"]:
    mag = feature["properties"]["mag"]
    if mag is None or mag < 0:
        continue
    lon, lat = feature["geometry"]["coordinates"][:2]
    place = feature["properties"]["place"]
    rows.append((lon, lat, place, mag))

data = pd.DataFrame(rows, columns=["lon", "lat", "place", "mag"])

# 筛选亚洲区域
asia_data = data[
    (data["lon"] >= 25) & (data["lon"] <= 150) &
    (data["lat"] >= -10) & (data["lat"] <= 55)
].reset_index(drop=True)

num_points = len(asia_data)

# 按经度从左到右排序，点从左向右出现
asia_data = asia_data.sort_values(by="lon").reset_index(drop=True)

# 每帧只加一个点的动画帧，加快速度
frames = []
for i in range(1, num_points + 1):
    texts = [f"{place}<br>Magnitude: {mag:.1f}" for place, mag in zip(asia_data["place"][:i], asia_data["mag"][:i])]
    frame = go.Frame(
        data=[go.Scattergeo(
            lon=asia_data["lon"][:i],
            lat=asia_data["lat"][:i],
            mode='markers',
            marker=dict(
                size=asia_data["mag"][:i] * 3,
                color=asia_data["mag"][:i],
                colorscale='Reds',
                cmin=asia_data["mag"].min(),
                cmax=asia_data["mag"].max(),
                colorbar=dict(title="Magnitude"),
                line=dict(width=0),
                opacity=0.8
            ),
            text=texts,
            hoverinfo='text+lon+lat'
        )],
        name=str(i)
    )
    frames.append(frame)

# 初始化无点图形，调整按钮位置，设置动画参数防止循环并让动画播放后暂停
fig = go.Figure(
    data=[go.Scattergeo(
        lon=[],
        lat=[],
        mode='markers',
        marker=dict(
            size=[],
            color=[],
            colorscale='Reds',
            cmin=asia_data["mag"].min() if num_points > 0 else 0,
            cmax=asia_data["mag"].max() if num_points > 0 else 1,
            colorbar=dict(title="Magnitude"),
            line=dict(width=0),
            opacity=0.8
        ),
        text=[],
        hoverinfo='text+lon+lat'
    )],
    layout=go.Layout(
        title="Asia Earthquakes - " + data_json["metadata"]["title"],
        geo=dict(
            scope='asia',
            projection_type='natural earth',
            showland=True,
            landcolor='rgb(217, 217, 217)',
            showcountries=True,
            countrycolor='rgb(204, 204, 204)',
            bgcolor='rgba(255,255,255,0)',
        ),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            y=0.98,
            x=1.15,
            xanchor="left",
            yanchor="top",
            pad=dict(t=0, r=10),
            buttons=[dict(
                label="Play",
                method="animate",
                args=[[str(i) for i in range(1, num_points + 1)], {
                    "frame": {"duration": 100, "redraw": True},
                    "transition": {"duration": 0},
                    "fromcurrent": False,
                    "mode": "immediate",
                    "loop": False
                }]
            )]
        )]
    ),
    frames=frames
)

fig.show()
