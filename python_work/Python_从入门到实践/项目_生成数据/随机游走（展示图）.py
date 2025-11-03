import matplotlib.pyplot as plt
from 随机游走 import RandomWork

while True:    
    rw = RandomWork()
    rw.fill_work()

    plt.style.use("classic")
    fig,ax = plt.subplots(figsize = (15,9))     #figsizse 调整窗口大小
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c= point_numbers, cmap=plt.cm.Blues, edgecolors="none" , s=1)
    ax.set_aspect("equal")
    ax.scatter(0,0, c="green", edgecolors= "none", s = 100)   #起始点
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c= "red", edgecolors="none" , s=100)  #终点

    ax.get_xaxis().set_visible(False)    #隐藏坐标轴
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == "n":
        break



