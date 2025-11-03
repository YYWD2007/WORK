import matplotlib.pyplot as plt       # 导入pyplot模块（用于生成图形或函数）

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]    

plt.style.use("tableau-colorblind10")     #设置图像风格。库自带，终端寻找:python,  import matplotlib.pyplot as plt, plt.style.available
fig, ax = plt.subplots()             #subplots可生成函数， fig,ax 是定制绘图的常用变量
ax.plot(input_values, squares, linewidth = 3)      #lienwidth 设置线宽度, 前面是x轴，后面是y轴

ax.set_title("Square Numbers", fontsize = 24)      #添加主题
ax.set_xlabel("Value",fontsize = 14)               #添加x轴信息
ax.set_ylabel("Square of value", fontsize = 14)    #添加y轴信息

ax.tick_params(labelsize=14)                       #标记样式

plt.show()



