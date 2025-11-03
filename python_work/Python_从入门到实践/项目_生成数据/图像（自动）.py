import matplotlib.pyplot as plt

x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8-notebook')
fig,ax = plt.subplots()

ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Blues, s=10)    #这里设了渐变色（colormap:颜色渐变）。 也可设置全部一个颜色 EX: color= (0,0.8,0)

ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of value", fontsize = 14)

ax.tick_params(labelsize = 14)

ax.axis([0,1100,0,1100000])             #指定每个坐标的取值范围
# ax.ticklabel_format(style="plain")      #数值过大时，它会使用科学计数法。这行代码可以保持原数字


plt.savefig("squares_plot.png", bbox_inches='tight')    #保存绘图，第一个实参是文件名，第二个是裁剪白边
plt.show()
  


