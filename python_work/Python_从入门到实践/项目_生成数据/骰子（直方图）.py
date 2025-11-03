import plotly.express as px # type: ignore

from Plotly import Die # type: ignore

die_1 = Die()
die_2 = Die()
results= []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = "Results of Rolling Two D6 1000 Times"
labels = {"x":"Result", "y":"Frequency of Result"}
fig = px.bar(x = poss_results, y = frequencies, title = title, labels= labels)  #px.bar 创建直方图
fig.update_layout(xaxis_dtick=1)   #x轴标记的间距
fig.write_html("dice_visual_d6d10.html")
fig.show()

