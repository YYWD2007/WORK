from random import choice   #随机选择

class RandomWork:
    def __init__(self, num_points = 50000):
        self.num_points = num_points #50000次随机

        self.x_values = [0]         #从（0，0）出发
        self.y_values = [0]

    def get_step(self):                                #随机游走设置
        direction = choice ([1,-1])                    #选择方向
        distance = choice ([0,1,2,3,4])                #选择距离，速度
        return direction * distance                    #步数等于距离×方向

    def fill_work(self):               
        while len(self.x_values) < self.num_points:          
            x_step = self.get_step()                
            y_step = self.get_step() 

            if x_step == 0 and y_step == 0:           #拒绝待在原地，其中一个的步数必须不等于0
                continue         

            x = self.x_values[-1] + x_step     #列表最后的数值添加下一个随机步数
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)








