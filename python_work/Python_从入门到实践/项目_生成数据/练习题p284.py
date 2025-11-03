import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
立方 = [1,8,27,64, 125]   

plt.style.use("tableau-colorblind10")     
fig, ax = plt.subplots()             
ax.plot(input_values, 立方, linewidth = 3)     

ax.set_title("Cube", fontsize = 24)      
ax.set_xlabel("Value",fontsize = 14)               
ax.set_ylabel("Cube of the value", fontsize = 14)   

ax.tick_params(labelsize=14)                      

plt.show()




import matplotlib.pyplot as plt

x_values = range(1,5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8-notebook')
fig,ax = plt.subplots()

ax.scatter(x_values, y_values,c=y_values, cmap=plt.cm.Greens, s=10)    

ax.set_title("Cube", fontsize = 24)      
ax.set_xlabel("Value",fontsize = 14)               
ax.set_ylabel("Cube of the value", fontsize = 14) 

ax.tick_params(labelsize = 14)

ax.axis([0,5100,0,130000000000])            

plt.savefig("cubes_plot.png", bbox_inches='tight')    
plt.show()
  
