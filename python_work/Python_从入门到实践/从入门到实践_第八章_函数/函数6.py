import pizza模块          #调用文件夹里的函数模块
pizza模块.make_pizza("16","pepperoni")
pizza模块.make_pizza("12","mushrooms","green peppers","extra cheese")

from pizza模块 import make_pizza         #导入特定函数
make_pizza("12","mushrooms","green peppers","extra cheese")

from pizza模块 import make_pizza as mp           #给函数指定别名
mp("12","mushrooms","green peppers","cheese")

import pizza模块 as pmk
pmk.make_pizza("12","mushrooms","green peppers","extra cheese")

from pizza模块 import *     #导入所有函数

